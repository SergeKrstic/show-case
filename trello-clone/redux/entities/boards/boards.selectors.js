import { createSelector } from 'reselect';

export const selectBoardsMap = state => {
  return state.entities.boards.items;
};

export const selectBoards = createSelector(
  // inputs
  selectBoardsMap,
  // result
  boards => {
    let boardsArray = Object.keys(boards).map(id => boards[id]);

    return boardsArray.sort((a, b) => {
      var x = a.name.toLowerCase();
      var y = b.name.toLowerCase();
      if (x < y) return -1;
      if (x > y) return 1;
      return 0;
    });
  }
);

export const selectBoardById = (state, id) => {
  let boards = selectBoardsMap(state);
  return boards[id];
};

export function selectBoardByName(state, boardName) {
  let boards = selectBoards(state);
  for (let board of boards) {
    if (board.name === boardName) return board;
  }
}
