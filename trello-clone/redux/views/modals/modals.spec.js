import types from './modals.types';
import * as actions from './modals.actions';
import reducer from './modals.reducer';

describe('modals actions', () => {
  it('should create openCreateBoardModal action', () => {
    const expectedAction = {
      type: types.OPEN_CREATE_BOARD_MODAL
    };

    expect(actions.openCreateBoardModal()).toEqual(expectedAction);
  });

  it('should create openCreateDomainModal action', () => {
    const expectedAction = {
      type: types.OPEN_CREATE_DOMAIN_MODAL
    };

    expect(actions.openCreateDomainModal()).toEqual(expectedAction);
  });

  it('should create closeCreateBoardModal action', () => {
    const expectedAction = {
      type: types.CLOSE_CREATE_BOARD_MODAL
    };

    expect(actions.closeCreateBoardModal()).toEqual(expectedAction);
  });

  it('should create closeCreateDomainModal action', () => {
    const expectedAction = {
      type: types.CLOSE_CREATE_DOMAIN_MODAL
    };

    expect(actions.closeCreateDomainModal()).toEqual(expectedAction);
  });

  it('should create closeAllModals action', () => {
    const expectedAction = {
      type: types.CLOSE_ALL_MODALS
    };

    expect(actions.closeAllModals()).toEqual(expectedAction);
  });

  it('should create focusOnModal action', () => {
    const expectedAction = {
      type: types.FOCUS_MODAL
    };

    expect(actions.focusOnModal()).toEqual(expectedAction);
  });

  it('should create blurOnModal action', () => {
    const expectedAction = {
      type: types.BLUR_MODAL
    };

    expect(actions.blurOnModal()).toEqual(expectedAction);
  });
});

describe('modals reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      isCreateDomainModalOpen: false,
      isCreateBoardModalOpen: false,
      isFocusOnModal: false,
      isModalOpen: false
    });
  });

  it('should handle OPEN_CREATE_BOARD_MODAL', () => {
    const action = actions.openCreateBoardModal();
    expect(reducer({}, action)).toEqual({
      isCreateBoardModalOpen: true,
      isModalOpen: true
    });
  });

  it('should handle OPEN_CREATE_DOMAIN_MODAL', () => {
    const action = actions.openCreateDomainModal();
    expect(reducer({}, action)).toEqual({
      isCreateDomainModalOpen: true,
      isModalOpen: true
    });
  });

  it('should handle CLOSE_CREATE_BOARD_MODAL', () => {
    const action = actions.closeCreateBoardModal();
    expect(reducer({}, action)).toEqual({
      isCreateBoardModalOpen: false,
      isModalOpen: false
    });
  });

  it('should handle CLOSE_CREATE_DOMAIN_MODAL', () => {
    const action = actions.closeCreateDomainModal();
    expect(reducer({}, action)).toEqual({
      isCreateDomainModalOpen: false,
      isModalOpen: false
    });
  });

  it('should handle CLOSE_ALL_MODALS', () => {
    const action = actions.closeAllModals();
    expect(reducer({}, action)).toEqual({
      isCreateDomainModalOpen: false,
      isCreateBoardModalOpen: false,
      isModalOpen: false
    });
  });

  it('should handle FOCUS_MODAL', () => {
    const action = actions.focusOnModal();
    expect(reducer({}, action)).toEqual({
      isFocusOnModal: true
    });
  });

  it('should handle BLUR_MODAL', () => {
    const action = actions.blurOnModal();
    expect(reducer({}, action)).toEqual({
      isFocusOnModal: false
    });
  });
});
