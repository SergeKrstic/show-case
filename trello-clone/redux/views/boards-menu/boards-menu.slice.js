import { createSlice } from '@reduxjs/toolkit';

const boardsMenuSlice = createSlice({
  name: 'boardsMenu',
  initialState: {
    isFocusOnBoardsMenu: false,
    isBoardsMenuOpen: false,
    userInput: ''
  },
  reducers: {
    openBoardsMenu(state, action) {
      state.isBoardsMenuOpen = true;
    },
    hideBoardsMenu(state, action) {
      state.isBoardsMenuOpen = false;
      state.userInput = '';
    },
    focusOnBoardsMenu(state, action) {
      state.isFocusOnBoardsMenu = true;
    },
    blurOnBoardsMenu(state, action) {
      state.isFocusOnBoardsMenu = false;
    },
    saveUserInput(state, action) {
      state.userInput = action.payload;
    }
  }
});

export const {
  openBoardsMenu,
  hideBoardsMenu,
  focusOnBoardsMenu,
  blurOnBoardsMenu,
  saveUserInput
} = boardsMenuSlice.actions;

export default boardsMenuSlice.reducer;
