import moment from 'moment';
import {
  all,
  fork,
  take,
  takeEvery,
  put,
  select,
  call,
  actionChannel
} from 'redux-saga/effects';

import firebase from 'firebase/app';
import 'firebase/firestore';

import { firestoreTypes } from 'firebase/redux/firestore.types';

import {
  calculateAddNewCardOrders,
  calculateNewListOrder,
  calculateNewCardOrders,
  hasCardMovedBetweenLists,
  createDragResultAction
} from './models.utils';

import * as boardViewActions from '../views/board-view/board-view.slice';
import * as modelActions from './models.actions';

import { api } from '../../api';
import { AutoId } from '../../../../../firebase/redux/firestore.utils';
import * as errorActions from 'redux/error/error.slice';
import * as cardActions from './cards/cards.actions';
import * as listActions from './lists/lists.actions';
import * as boardActions from './boards/boards.actions';
import * as domainActions from './domains/domains.actions';

import { selectUserId } from '../session/session.selectors';
import { selectBoardById, selectBoardByName } from './boards/boards.selectors';
import { selectListById, selectListByName } from './lists/lists.selectors';
import { selectCardById } from './cards/cards.selectors';
import { selectActiveCardId } from '../views/board-view/board-view.selectors';
import { selectDomain } from 'views/services/trello-clone/redux/entities/domains/domains.selectors';

// export const isDevelopment = process.env.NODE_ENV === 'development';
export const isDevelopment = true; // always crash loudly for now, till we are stable in production

export function* watchAll() {
  // Note: takeEvery passes in the action object
  yield all([
    // Card sagas
    takeEvery(modelActions.addCard.type, addCard),
    takeEvery(modelActions.updateCard.type, updateCard),
    takeEvery(modelActions.toggleCardLabel.type, toggleCardLabel),
    fork(watchMoveCard),
    // List sagas
    takeEvery(modelActions.addList.type, addList),
    takeEvery(modelActions.updateList.type, updateList),
    takeEvery(modelActions.moveList.type, moveList),
    // Board sagas
    takeEvery(modelActions.addBoard.type, addBoard),
    takeEvery(modelActions.updateBoard.type, updateBoard),
    takeEvery(modelActions.addBoardListeners.type, addBoardListeners),
    takeEvery(modelActions.removeBoardListeners.type, removeBoardListeners),
    takeEvery(
      modelActions.removeOldCardsInDoneList.type,
      removeOldCardsInDoneList
    ),
    takeEvery(
      modelActions.moveOldTodayCardsToDoingList.type,
      moveOldTodayCardsToDoingList
    ),
    takeEvery(modelActions.sendWellDoneMessage.type, sendWellDoneMessage),
    // Domain sagas
    takeEvery(modelActions.addDomain.type, addDomain)
  ]);
}

// const commitBatchWrites = batch =>
// batch.commit().then(/* wait till completed */);

async function commitBatchWrites(batch) {
  return await batch.commit();
}

/////////////////////////////////////////////////////////////////////////////////////////
// Card sagas
/////////////////////////////////////////////////////////////////////////////////////////

export function* addCard({ payload }) {
  const userId = yield select(selectUserId);
  const batch = api(userId).firestore.batch();
  // Update UI
  yield put(boardViewActions.closeCreateCardForm());
  // Add a new card
  const newCardId = AutoId.newId();
  yield put(
    cardActions.addCard(userId, newCardId, { id: newCardId, ...payload }, batch)
  );
  // Update the lists
  const cardOrders = yield select(
    calculateAddNewCardOrders,
    newCardId,
    payload.listId
  );
  for (const cardOrder of cardOrders) {
    const { listId, cardIds } = cardOrder;
    yield put(listActions.updateList(userId, listId, { cardIds }, batch));
  }
  // End batch write
  yield call(commitBatchWrites, batch);
}

export function* updateCard({ payload }) {
  const userId = yield select(selectUserId);
  yield put(cardActions.updateCard(userId, payload.id, payload.data));
}

export function* watchMoveCard() {
  // Ensure the moveCard action is processed serially
  const requestChannel = yield actionChannel(modelActions.moveCard.type);
  while (true) {
    const action = yield take(requestChannel);
    yield call(moveCard, action);
  }
}

export function* moveCard({ payload }) {
  let { batch, dragResult, isMultiMoveComplete } = payload;

  const error = new Error('testing toasts again...');
  yield put(errorActions.reportError({ error: 'something bad happened' }));
  // yield put(errorActions.reportError({ error }));
  // throw error

  if (isMultiMoveComplete) {
    yield put({ type: 'MULTI_MOVE_COMPLETED' });
    return;
  }

  const isLocalBatch = batch === null;
  const userId = yield select(selectUserId);
  batch = isLocalBatch ? api(userId).firestore.batch() : batch;

  const result = yield select(calculateNewCardOrders, dragResult);
  const { cardDetails, cardOrders } = result;

  // Update the card
  const cardMovedBetweenLists = yield select(
    hasCardMovedBetweenLists,
    dragResult
  );
  let cardData = { listId: cardDetails.listId };
  if (cardMovedBetweenLists) {
    cardData = {
      ...cardData,
      dateListChanged: firebase.firestore.Timestamp.now()
    };
  }
  yield put(
    cardActions.updateCard(userId, cardDetails.cardId, cardData, batch)
  );
  yield take([
    firestoreTypes.UPDATE_DOCUMENT_SUCCESS,
    firestoreTypes.UPDATE_DOCUMENT_FAILURE
  ]);

  // Update the lists
  for (const cardOrder of cardOrders) {
    const { listId, cardIds } = cardOrder;
    yield put(listActions.updateList(userId, listId, { cardIds }, batch));
    yield take([
      firestoreTypes.UPDATE_DOCUMENT_SUCCESS,
      firestoreTypes.UPDATE_DOCUMENT_FAILURE
    ]);
  }

  // End batch write
  if (isLocalBatch) {
    yield call(commitBatchWrites, batch);
  }

  // Send "Well done!" if task complete
  const list = yield select(selectListById, cardDetails.listId);
  if (list && list.name === 'Done') {
    yield put(modelActions.sendWellDoneMessage());
  }
}

export function* toggleCardLabel({ payload }) {
  const userId = yield select(selectUserId);
  const activeCardId = yield select(selectActiveCardId);
  if (activeCardId) {
    const { labelColor } = payload;
    const card = yield select(selectCardById, activeCardId);
    const board = yield select(selectBoardById, card.boardId);
    let labelName = '';
    if (board.labels) {
      const boardLabel = board.labels.find(label => label.color === labelColor);
      labelName = boardLabel ? boardLabel.name : '';
    }
    const label = card.labels.find(label => label.color === labelColor);
    const labels = label
      ? card.labels.filter(label => label.color !== labelColor)
      : [...card.labels, { color: labelColor, name: labelName }];
    yield put(cardActions.updateCard(userId, card.id, { labels }));
  }
}

/////////////////////////////////////////////////////////////////////////////////////////
// List sagas
/////////////////////////////////////////////////////////////////////////////////////////

export function* addList({ payload }) {
  const userId = yield select(selectUserId);
  const batch = api(userId).firestore.batch();
  const board = yield select(selectBoardById, payload.boardId);
  const newListId = AutoId.newId();
  const listIds = [...board.listIds, newListId];
  yield put(
    listActions.addList(userId, newListId, { id: newListId, ...payload }, batch)
  );
  yield put(boardActions.updateBoard(userId, board.id, { listIds }, batch));
  yield put(boardViewActions.closeCreateListForm());
  yield call(commitBatchWrites, batch);
}

export function* updateList({ payload }) {
  const userId = yield select(selectUserId);
  yield put(listActions.updateList(userId, payload.id, payload.data));
  yield put(boardViewActions.closeUpdateListNameForm());
}

export function* moveList({ payload }) {
  const userId = yield select(selectUserId);
  const listOrder = yield select(calculateNewListOrder, payload.dragResult);
  const { boardId, listIds } = listOrder;
  yield put(boardActions.updateBoard(userId, boardId, { listIds }));
}

/////////////////////////////////////////////////////////////////////////////////////////
// Board sagas
/////////////////////////////////////////////////////////////////////////////////////////

export function* addBoard({ payload }) {
  const userId = yield select(selectUserId);
  const batch = api(userId).firestore.batch();
  // add the board
  const newBoardId = AutoId.newId();
  yield put(
    boardActions.addBoard(
      userId,
      newBoardId,
      { id: newBoardId, ...payload },
      batch
    )
  );
  // update the domain
  const domain = yield select(selectDomain, payload.domainId);
  yield put(
    domainActions.updateDomain(
      userId,
      payload.domainId,
      { boardIds: [...domain.boardIds, newBoardId] },
      batch
    )
  );
  yield call(commitBatchWrites, batch);
}

export function* updateBoard({ payload }) {
  const userId = yield select(selectUserId);
  yield put(boardActions.updateBoard(userId, payload.id, payload.data));
}

export function* addBoardListeners({ payload }) {
  // const boardId = payload.id;
  const userId = yield select(selectUserId);
  yield put(domainActions.listenToAllDomains(userId));
  yield put(boardActions.listenToAllBoards(userId));
  yield put(listActions.listenToAllLists(userId));
  yield put(cardActions.listenToAllCards(userId));
  // yield put(cardActions.listenToCards(userId, boardId));
}

export function* removeBoardListeners() {
  yield put(domainActions.removeDomainsListener());
  yield put(boardActions.removeBoardsListener());
  yield put(listActions.removeListsListener());
  yield put(cardActions.removeCardsListener());
}

export function* removeOldCardsInDoneList({ payload }) {
  const board = yield select(selectBoardById, payload.boardId);

  // Skip if not 'Today' or 'Next' boards
  const mirroredBoards = ['Today', 'Next'];
  if (!board || !mirroredBoards.includes(board.name)) return;

  const userId = yield select(selectUserId);
  const list = yield select(selectListByName, 'Done', board);
  const keepDate = moment().startOf('day');

  let newCardIds = [];
  for (let cardId of list.cardIds) {
    const card = yield select(selectCardById, cardId);
    if (moment(card.dateListChanged).isAfter(keepDate)) {
      newCardIds.push(cardId);
    }
  }
  yield put(listActions.updateList(userId, list.id, { cardIds: newCardIds }));
}

export function* moveOldTodayCardsToDoingList({ payload }) {
  const userId = yield select(selectUserId);
  const batch = api(userId).firestore.batch();
  const nextBoard = yield select(selectBoardByName, 'Next');
  const todayList = yield select(selectListByName, 'Today', nextBoard);
  const doingList = yield select(selectListByName, 'Doing', nextBoard);
  const keepDate = moment().startOf('day');
  const { moveAll } = payload;
  if (!todayList) return;
  for (let index = 0; index < todayList.cardIds.length; index++) {
    const sourceIndex = todayList.cardIds.length - index - 1;
    const cardId = todayList.cardIds[sourceIndex];
    const card = yield select(selectCardById, cardId);
    if (card) {
      if (moveAll || moment(card.dateListChanged).isBefore(keepDate)) {
        const dragResultAction = createDragResultAction(
          nextBoard.id,
          cardId,
          sourceIndex,
          todayList,
          doingList
        );
        yield put(
          modelActions.moveCard({
            dragResult: dragResultAction,
            boardId: nextBoard.id,
            batch
          })
        );
      }
    }
  }
  yield put(
    modelActions.moveCard({
      dragResult: null,
      boardId: null,
      isMultiMoveComplete: true
    })
  );
  yield take('MULTI_MOVE_COMPLETED');
  yield call(commitBatchWrites, batch);
}

export function* sendWellDoneMessage() {
  const userId = yield select(selectUserId);
  const commands = api(userId).commands;
  try {
    const response = yield call(commands.sendWellDoneMessageToUser);
    if (!response.ok) {
      throw Error(response.statusText);
    }
  } catch (error) {
    if (isDevelopment) throw error;
  }
}

/////////////////////////////////////////////////////////////////////////////////////////
// Domain sagas
/////////////////////////////////////////////////////////////////////////////////////////

export function* addDomain({ payload }) {
  const userId = yield select(selectUserId);
  const newDomainId = AutoId.newId();
  yield put(
    domainActions.addDomain(userId, newDomainId, {
      id: newDomainId,
      ...payload
    })
  );
}
