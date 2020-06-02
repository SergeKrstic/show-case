import { createSelector } from 'reselect';
import createCachedSelector from 're-reselect';
import { convertArrayToObject } from '../../../utils/utils';

export const selectCardsMap = state => {
  return state.entities.cards.items;
};

export const selectCards = createSelector(
  // inputs
  selectCardsMap,
  // result
  cards => Object.keys(cards).map(id => cards[id])
);

export const selectCardsMapByBoardId = createSelector(
  // inputs
  (state, boardId) => selectCardsByBoardId(state, boardId),
  // result
  cards => convertArrayToObject(cards, 'id')
);

export const selectCardsByBoardId = createCachedSelector(
  // inputs
  (state, boardId) => boardId,
  (state, boardId) => selectCards(state),
  // result
  (boardId, cards) => cards.filter(card => card.boardId === boardId)
)((state, boardId) => boardId);

export const selectCardById = (state, id) => {
  let cards = selectCardsMap(state);
  return cards[id];
};
