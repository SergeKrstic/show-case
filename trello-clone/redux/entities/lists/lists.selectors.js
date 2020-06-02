import { createSelector } from 'reselect';
import createCachedSelector from 're-reselect';
import { convertArrayToObject } from '../../../utils/utils';

export const selectListsMap = state => {
  return state.entities.lists.items;
};

export const selectLists = createSelector(
  // inputs
  selectListsMap,
  // resultFunc
  lists => Object.keys(lists).map(id => lists[id])
);

export const selectListMapByBoardId = createSelector(
  // inputs
  (state, boardId) => selectListsByBoardId(state, boardId),
  // result
  lists => convertArrayToObject(lists, 'id')
);

export const selectListsByBoardId = createCachedSelector(
  // inputs
  (state, boardId) => boardId,
  (state, boardId) => selectLists(state),
  // result
  (boardId, lists) => lists.filter(list => list.boardId === boardId)
)((state, boardId) => boardId);

export const selectListById = (state, id) => {
  let lists = selectListsMap(state);
  return lists[id];
};

export function selectListByName(state, listName, board) {
  if (!board) return;
  for (let listId of board.listIds) {
    // Note: cannot use createCachedSelector since state is referenced
    // in a loop (state will always change between calls)
    const list = selectListById(state, listId);
    if (list.name === listName) return list;
  }
}
