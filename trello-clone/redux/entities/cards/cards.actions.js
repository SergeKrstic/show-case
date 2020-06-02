import { api } from '../../../api';

import * as actions from 'firebase/redux/firestore.actions';
import { Timestamp } from 'firebase/utils/firebase.utils';
import { metaTypes } from '../models.types';

export function addCard(
  userId,
  cardId,
  { id, name, description, isClosed, boardName, boardId, listId } = {},
  batch = null,
  hasTimestamp = true
) {
  let setFunc = api(userId).cards.set;
  let data = {
    id,
    name,
    description,
    isClosed,
    boardName,
    boardId,
    listId,
    labels: [],
    due: null,
    dueCompleted: false,
    dateCreated: hasTimestamp ? Timestamp.now() : '',
    dateModified: hasTimestamp ? Timestamp.now() : '',
    dateListChanged: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.setDocument(metaTypes.cards, setFunc, cardId, data, batch);
}

export function updateCard(
  userId,
  cardId,
  data,
  batch = null,
  hasTimestamp = true
) {
  let updateFunc = api(userId).cards.update;
  let dataWithTimestamp = {
    ...data,
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.updateDocument(
    metaTypes.cards,
    updateFunc,
    cardId,
    dataWithTimestamp,
    batch
  );
}

export function deleteCard(userId, card, batch = null) {
  let deleteFunc = api(userId).cards.delete;
  return actions.removeDocument(
    metaTypes.cards,
    deleteFunc,
    card.id,
    card,
    batch
  );
}

export function listenToAllCards(userId) {
  let ref = api(userId).cardsRef;
  return actions.addListener(metaTypes.cards, ref);
}

export function listenToCards(userId, boardId) {
  let ref = api(userId).cardsRef.where('boardId', '==', boardId);
  return actions.addListener(metaTypes.cards, ref);
}

export function removeCardsListener() {
  return actions.removeListener(metaTypes.cards, false);
}
