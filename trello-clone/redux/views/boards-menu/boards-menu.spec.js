import types from './boards-menu.types';
import * as actions from './boards-menu.actions';
import reducer from './boards-menu.reducer';

describe('boardsMenu actions', () => {
  it('should create openBoardsMenu action', () => {
    const expectedAction = {
      type: types.OPEN_BOARDS_MENU
    };

    expect(actions.openBoardsMenu()).toEqual(expectedAction);
  });

  it('should create hideBoardsMenu action', () => {
    const expectedAction = {
      type: types.HIDE_BOARDS_MENU
    };

    expect(actions.hideBoardsMenu()).toEqual(expectedAction);
  });

  it('should create focusOnBoardsMenu action', () => {
    const expectedAction = {
      type: types.FOCUS_BOARDS_MENU
    };

    expect(actions.focusOnBoardsMenu()).toEqual(expectedAction);
  });

  it('should create blurOnBoardsMenu action', () => {
    const expectedAction = {
      type: types.BLUR_BOARDS_MENU
    };

    expect(actions.blurOnBoardsMenu()).toEqual(expectedAction);
  });

  it('should create saveUserInput action', () => {
    const expectedAction = {
      type: types.SAVE_USER_INPUT,
      payload: 'b'
    };

    expect(actions.saveUserInput('b')).toEqual(expectedAction);
  });
});

describe('boardsMenu reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      isFocusOnBoardsMenu: false,
      isBoardsMenuOpen: false,

      userInput: ''
    });
  });

  it('should handle OPEN_BOARDS_MENU', () => {
    const action = actions.openBoardsMenu();
    expect(reducer({}, action)).toEqual({
      isBoardsMenuOpen: true
    });
  });

  it('should handle HIDE_BOARDS_MENU', () => {
    const action = actions.hideBoardsMenu();
    expect(reducer({}, action)).toEqual({
      isBoardsMenuOpen: false,
      userInput: ''
    });
  });

  it('should handle FOCUS_BOARDS_MENU', () => {
    const action = actions.focusOnBoardsMenu();
    expect(reducer({}, action)).toEqual({
      isFocusOnBoardsMenu: true
    });
  });

  it('should handle BLUR_BOARDS_MENU', () => {
    const action = actions.blurOnBoardsMenu();
    expect(reducer({}, action)).toEqual({
      isFocusOnBoardsMenu: false
    });
  });

  it('should handle SAVE_USER_INPUT', () => {
    const payload = 'b';
    const action = actions.saveUserInput(payload);
    expect(reducer({}, action)).toEqual({
      userInput: payload
    });
  });
});
