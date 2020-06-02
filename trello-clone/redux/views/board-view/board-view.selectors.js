import { selectBoardById } from '../../entities/boards/boards.selectors';
import { selectListMapByBoardId } from '../../entities/lists/lists.selectors';
import { selectCardsMapByBoardId } from '../../entities/cards/cards.selectors';

export function selectBoardView(state) {
  return state.views.boardView;
}

export function selectCurrentBoardId(state) {
  return selectBoardView(state).boardId;
}

export function selectActiveCardId(state) {
  return selectBoardView(state).activeCardId;
}

export function selectCurrentBoard(state) {
  const boardId = selectCurrentBoardId(state);
  return selectBoardById(state, boardId);
}

export function selectCurrentLists(state) {
  const boardId = selectCurrentBoardId(state);
  return selectListMapByBoardId(state, boardId);
}

export function selectCurrentCards(state) {
  const boardId = selectCurrentBoardId(state);
  return selectCardsMapByBoardId(state, boardId);
}

export function selectCreateCardFormName(state) {
  const boardView = state.ui.boardView;
  const listId = boardView.createCardFormListId;
  if (boardView.potentialNewCards[listId])
    return boardView.potentialNewCards[listId].cardName;
  else return '';
}
