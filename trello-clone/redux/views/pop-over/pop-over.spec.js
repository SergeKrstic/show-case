import types from './pop-over.types';
import * as actions from './pop-over.actions';
import reducer from './pop-over.reducer';

describe('popOver actions', () => {
  it('should create showPopOver action', () => {
    const expectedAction = {
      type: types.SHOW_POP_OVER
    };

    expect(actions.showPopOver()).toEqual(expectedAction);
  });

  it('should create hidePopOver action', () => {
    const expectedAction = {
      type: types.HIDE_POP_OVER
    };

    expect(actions.hidePopOver()).toEqual(expectedAction);
  });

  it('should create focusOnPopOver action', () => {
    const expectedAction = {
      type: types.FOCUS_POP_OVER
    };

    expect(actions.focusOnPopOver()).toEqual(expectedAction);
  });

  it('should create blurOnPopOver action', () => {
    const expectedAction = {
      type: types.BLUR_POP_OVER
    };

    expect(actions.blurOnPopOver()).toEqual(expectedAction);
  });
});

describe('popOver reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      isPopOverOpen: false,
      isFocusOnPopOver: false
    });
  });

  it('should handle SHOW_POP_OVER', () => {
    const action = actions.showPopOver();
    expect(reducer({}, action)).toEqual({
      isPopOverOpen: true
    });
  });

  it('should handle HIDE_POP_OVER', () => {
    const action = actions.hidePopOver();
    expect(reducer({}, action)).toEqual({
      isPopOverOpen: false
    });
  });

  it('should handle FOCUS_POP_OVER', () => {
    const action = actions.focusOnPopOver();
    expect(reducer({}, action)).toEqual({
      isFocusOnPopOver: true
    });
  });

  it('should handle BLUR_POP_OVER', () => {
    const action = actions.blurOnPopOver();
    expect(reducer({}, action)).toEqual({
      isFocusOnPopOver: false
    });
  });
});
