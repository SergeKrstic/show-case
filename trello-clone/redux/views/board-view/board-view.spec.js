import { expectSaga } from 'redux-saga-test-plan';
import { createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga';

import types from './board-view.types';
import * as actions from './board-view.actions';
import * as selectors from './board-view.selectors';
import reducer from './board-view.reducer';
import { calculateNewCardOrder } from '../../entities/models.utils';

import rootReducer from '../../root.reducer';
import rootSaga from '../../root.saga';
import { mockFirebase } from '../../../utils/mock-firestore';
import { MOCK_USER_ID } from '../../../utils/constants';
import { convertCollectionsSnapshotToMap } from 'firebase/utils/firestore.utils';

// const initialState = {
//   data: {
//     boards: {
//       inProgress: false,
//       error: '',
//       items: {
//         'b-project': {
//           id: 'b-project',
//           name: 'Project',
//           listIds: [
//             'b-project-l-backlog',
//             'b-project-l-next',
//             'b-project-l-today',
//             'b-project-l-doing',
//             'b-project-l-done',
//             'b-project-l-discarded'
//           ],
//           isClosed: false,
//           isStarred: true,
//           domainId: ''
//         },
//         'b-next': {
//           id: 'b-next',
//           name: 'Next',
//           listIds: ['b-next-l-next', 'b-next-l-doing', 'b-next-l-today'],
//           isClosed: false,
//           isStarred: true,
//           domainId: ''
//         },
//         'b-today': {
//           id: 'b-today',
//           name: 'Today',
//           listIds: [
//             'b-today-l-today',
//             'b-today-l-in-progress',
//             'b-today-l-done'
//           ],
//           isClosed: false,
//           isStarred: true,
//           domainId: ''
//         }
//       }
//     },
//     lists: {
//       inProgress: false,
//       error: '',
//       items: {
//         // Project board lists
//         'b-project-l-backlog': {
//           id: 'b-project-l-backlog',
//           name: 'Backlog',
//           cardIds: ['card-1', 'card-26', 'card-27'],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         'b-project-l-next': {
//           id: 'b-project-l-next',
//           name: 'Next',
//           cardIds: ['card-4', 'card-5', 'card-10'],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         'b-project-l-today': {
//           id: 'b-project-l-today',
//           name: 'Today',
//           cardIds: ['card-3', 'card-7', 'card-11'],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         'b-project-l-doing': {
//           id: 'b-project-l-doing',
//           name: 'Doing',
//           cardIds: ['card-2', 'card-12', 'card-13'],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         'b-project-l-done': {
//           id: 'b-project-l-done',
//           name: 'Done',
//           cardIds: ['card-8', 'card-14', 'card-15'],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         'b-project-l-discarded': {
//           id: 'b-project-l-discarded',
//           name: 'Discarded',
//           cardIds: [],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         // Other project board lists
//         'b-other-l-backlog': {
//           id: 'b-other-l-backlog',
//           name: 'Backlog',
//           cardIds: ['card-28', 'card-29', 'card-30'],
//           boardId: 'b-project',
//           isClosed: false
//         },
//         'b-other-l-next': {
//           id: 'b-other-l-next',
//           name: 'Next',
//           cardIds: ['card-6', 'card-16', 'card-17'],
//           boardId: 'b-other',
//           isClosed: false
//         },
//         'b-other-l-today': {
//           id: 'b-other-l-today',
//           name: 'Today',
//           cardIds: ['card-18', 'card-19', 'card-20'],
//           boardId: 'b-other',
//           isClosed: false
//         },
//         'b-other-l-doing': {
//           id: 'b-other-l-doing',
//           name: 'Doing',
//           cardIds: ['card-21', 'card-22', 'card-23'],
//           boardId: 'b-other',
//           isClosed: false
//         },
//         'b-other-l-done': {
//           id: 'b-other-l-done',
//           name: 'Done',
//           cardIds: ['card 9', 'card-24', 'card-25'],
//           boardId: 'b-other',
//           isClosed: false
//         },
//         'b-other-l-discarded': {
//           id: 'b-other-l-discarded',
//           name: 'Discarded',
//           cardIds: [],
//           boardId: 'b-other',
//           isClosed: false
//         },
//         // Next board lists
//         'b-next-l-next': {
//           id: 'b-next-l-next',
//           name: 'Next',
//           cardIds: [
//             'card-4',
//             'card-5',
//             'card-6',
//             'card-10',
//             'card-16',
//             'card-17'
//           ],
//           boardId: 'b-next',
//           isClosed: false
//         },
//         'b-next-l-today': {
//           id: 'b-next-l-today',
//           name: 'Today',
//           cardIds: [
//             'card-3',
//             'card-7',
//             'card-11',
//             'card-18',
//             'card-19',
//             'card-20'
//           ],
//           boardId: 'b-next',
//           isClosed: false
//         },
//         'b-next-l-doing': {
//           id: 'b-next-l-doing',
//           name: 'Doing',
//           cardIds: [
//             'card-2',
//             'card-12',
//             'card-13',
//             'card-21',
//             'card-22',
//             'card-23'
//           ],
//           boardId: 'b-next',
//           isClosed: false
//         },
//         'b-next-l-done': {
//           id: 'b-next-l-done',
//           name: 'Done',
//           cardIds: [
//             'card-8',
//             'card-9',
//             'card-14',
//             'card-15',
//             'card-24',
//             'card-25'
//           ],
//           boardId: 'b-next',
//           isClosed: false
//         },
//         // Today board lists
//         'b-today-l-today': {
//           id: 'b-today-l-today',
//           name: 'Today',
//           cardIds: ['card-3', 'card-7', 'card-11', 'card-18', 'card-19'],
//           boardId: 'b-today',
//           isClosed: false
//         },
//         'b-today-l-in-progress': {
//           id: 'b-today-l-in-progress',
//           name: 'In Progress',
//           cardIds: ['card-20'],
//           boardId: 'b-today',
//           isClosed: false
//         },
//         'b-today-l-done': {
//           id: 'b-today-l-done',
//           name: 'Done',
//           cardIds: [
//             'card-8',
//             'card-9',
//             'card-14',
//             'card-15',
//             'card-24',
//             'card-25'
//           ],
//           boardId: 'b-today',
//           isClosed: false
//         }
//       }
//     },
//     cards: {
//       inProgress: false,
//       error: '',
//       items: {
//         'card-1': {
//           id: 'card-1',
//           name: 'card 1',
//           listId: 'b-project-l-backlog',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-2': {
//           id: 'card-2',
//           name: 'card 2',
//           listId: 'b-project-l-doing',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-3': {
//           id: 'card-3',
//           name: 'card 3',
//           listId: 'b-project-l-today',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-4': {
//           id: 'card-4',
//           name: 'card 4',
//           listId: 'b-project-l-next',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-5': {
//           id: 'card-5',
//           name: 'card 5',
//           listId: 'b-project-l-next',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-6': {
//           id: 'card-6',
//           name: 'card 6',
//           listId: 'b-other-l-next',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-7': {
//           id: 'card-7',
//           name: 'card 7',
//           listId: 'b-project-l-today',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-8': {
//           id: 'card-8',
//           name: 'card 8',
//           listId: 'b-project-l-done',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-9': {
//           id: 'card-9',
//           name: 'card 9',
//           listId: 'b-other-l-done',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-10': {
//           id: 'card-10',
//           name: 'card 10',
//           listId: 'b-project-l-next',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-11': {
//           id: 'card-11',
//           name: 'card 11',
//           listId: 'b-project-l-today',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-12': {
//           id: 'card-12',
//           name: 'card 12',
//           listId: 'b-project-l-doing',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-13': {
//           id: 'card-13',
//           name: 'card 13',
//           listId: 'b-project-l-doing',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-14': {
//           id: 'card-14',
//           name: 'card 14',
//           listId: 'b-project-l-done',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-15': {
//           id: 'card-15',
//           name: 'card 15',
//           listId: 'b-project-l-done',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-16': {
//           id: 'card-16',
//           name: 'card 16',
//           listId: 'b-other-l-next',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-17': {
//           id: 'card-17',
//           name: 'card 17',
//           listId: 'b-other-l-next',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-18': {
//           id: 'card-18',
//           name: 'card 18',
//           listId: 'b-other-l-today',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-19': {
//           id: 'card-19',
//           name: 'card 19',
//           listId: 'b-other-l-today',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-20': {
//           id: 'card-20',
//           name: 'card 20',
//           listId: 'b-other-l-today',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-21': {
//           id: 'card-21',
//           name: 'card 21',
//           listId: 'b-other-l-doing',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-22': {
//           id: 'card-22',
//           name: 'card 22',
//           listId: 'b-other-l-doing',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-23': {
//           id: 'card-23',
//           name: 'card 23',
//           listId: 'b-other-l-doing',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-24': {
//           id: 'card-24',
//           name: 'card 24',
//           listId: 'b-other-l-done',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-25': {
//           id: 'card-25',
//           name: 'card 25',
//           listId: 'b-other-l-done',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-26': {
//           id: 'card-26',
//           name: 'card 26',
//           listId: 'b-project-l-backlog',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-27': {
//           id: 'card-27',
//           name: 'card 27',
//           listId: 'b-project-l-backlog',
//           boardId: 'b-project',
//           isClosed: false,
//           description: ''
//         },
//         'card-28': {
//           id: 'card-28',
//           name: 'card 28',
//           listId: 'b-other-l-backlog',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-29': {
//           id: 'card-29',
//           name: 'card 29',
//           listId: 'b-other-l-backlog',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         },
//         'card-30': {
//           id: 'card-30',
//           name: 'card 30',
//           listId: 'b-other-l-backlog',
//           boardId: 'b-other',
//           isClosed: false,
//           description: ''
//         }
//       }
//     }
//   },
//   session: { userId: MOCK_USER_ID, userName: 'Mock User' },
//   form: {},
//   ui: {
//     boardView: {
//       boardId: 'b-project',
//       isCreateCardFormOpen: false,
//       isFocusOnCreateCardForm: false,
//       createCardFormIndexToOpen: 0,
//       isCreateListFormOpen: false,
//       isFocusOnCreateListForm: false,
//       isUpdateListNameFormOpen: false,
//       isFocusOnUpdateListNameForm: false,
//       updateListNameFormIndexToOpen: 0,
//       isUpdateBoardNameFormOpen: false,
//       isFocusOnUpdateBoardNameForm: false
//     },
//     home: {
//       errorMessage: '',
//       isFetchingHomeSuccessful: false,
//       isFetchingHome: false,
//       isFetching: false
//     },
//     modals: {
//       isCreateDomainModalOpen: false,
//       isCreateBoardModalOpen: false,
//       isFocusOnModal: false,
//       isModalOpen: false
//     },
//     popOver: { isPopOverOpen: false, isFocusOnPopOver: false },
//     notification: { errorMessages: [] },
//     domain: {
//       isFetchingDomain: false,
//       isFetchingDomainSuccessful: false,
//       errorMessage: '',
//       isModalOpen: false,
//       domains: []
//     },
//     boardsMenu: {
//       isFocusOnBoardsMenu: false,
//       isBoardsMenuOpen: false,
//       userInput: ''
//     },
//     starredBoard: {
//       isFetchingStarredBoard: false,
//       isFetchingStarredBoardSuccessful: false,
//       errorMessage: '',
//       starredBoards: []
//     }
//   }
// };

describe('boardView actions', () => {
  describe('create card form', () => {
    it('should create openCreateCardForm action', () => {
      const payload = {};
      const expectedAction = {
        type: types.OPEN_CREATE_CARD_FORM,
        payload
      };

      expect(actions.openCreateCardForm(payload)).toEqual(expectedAction);
    });

    it('should create closeCreateCardForm action', () => {
      const expectedAction = {
        type: types.CLOSE_CREATE_CARD_FORM
      };

      expect(actions.closeCreateCardForm()).toEqual(expectedAction);
    });

    it('should create focusOnCardForm action', () => {
      const expectedAction = {
        type: types.FOCUS_CREATE_CARD_FORM
      };

      expect(actions.focusOnCardForm()).toEqual(expectedAction);
    });

    it('should create blurOnCardForm action', () => {
      const expectedAction = {
        type: types.BLUR_CREATE_CARD_FORM
      };

      expect(actions.blurOnCardForm()).toEqual(expectedAction);
    });
  });

  describe('create list form', () => {
    it('should create openCreateListForm action', () => {
      const expectedAction = {
        type: types.OPEN_CREATE_LIST_FORM
      };
      expect(actions.openCreateListForm()).toEqual(expectedAction);
    });

    it('should create closeCreateListForm action', () => {
      const expectedAction = {
        type: types.CLOSE_CREATE_LIST_FORM
      };
      expect(actions.closeCreateListForm()).toEqual(expectedAction);
    });

    it('should create focusOnListForm action', () => {
      const expectedAction = {
        type: types.FOCUS_CREATE_LIST_FORM
      };
      expect(actions.focusOnListForm()).toEqual(expectedAction);
    });

    it('should create blurOnListForm action', () => {
      const expectedAction = {
        type: types.BLUR_CREATE_LIST_FORM
      };
      expect(actions.blurOnListForm()).toEqual(expectedAction);
    });
  });

  describe('update list name form', () => {
    it('should create focusOnUpdateListNameForm action', () => {
      const expectedAction = {
        type: types.FOCUS_ON_UPDATE_LIST_NAME_FORM
      };
      expect(actions.focusOnUpdateListNameForm()).toEqual(expectedAction);
    });

    it('should create blurOnUpdateListNameForm action', () => {
      const expectedAction = {
        type: types.BLUR_ON_UPDATE_LIST_NAME_FORM
      };
      expect(actions.blurOnUpdateListNameForm()).toEqual(expectedAction);
    });
  });

  describe('update board name form', () => {
    it('should create openUpdateBoardNameForm action', () => {
      const expectedAction = {
        type: types.OPEN_UPDATE_BOARD_NAME_FORM
      };
      expect(actions.openUpdateBoardNameForm()).toEqual(expectedAction);
    });

    it('should create closeUpdateBoardNameForm action', () => {
      const expectedAction = {
        type: types.CLOSE_UPDATE_BOARD_NAME_FORM
      };
      expect(actions.closeUpdateBoardNameForm()).toEqual(expectedAction);
    });

    it('should create focusOnUpdateBoardNameForm action', () => {
      const expectedAction = {
        type: types.FOCUS_ON_UPDATE_BOARD_NAME_FORM
      };
      expect(actions.focusOnUpdateBoardNameForm()).toEqual(expectedAction);
    });

    it('should create blurOnUpdateBoardNameForm action', () => {
      const expectedAction = {
        type: types.BLUR_ON_UPDATE_BOARD_NAME_FORM
      };
      expect(actions.blurOnUpdateBoardNameForm()).toEqual(expectedAction);
    });
  });

  describe('card', () => {
    const cardId = 'card-01';

    it('should create addCard action', () => {
      const payload = {
        name: 'card 1',
        description: 'card description',
        isClosed: false,
        boardId: 'board-01',
        listId: 'list-01'
      };
      const expectedAction = {
        type: types.ADD_CARD,
        payload
      };
      expect(actions.addCard(payload)).toEqual(expectedAction);
    });

    it('should create updateCard action', () => {
      const modifiedData = { name: 'new card name' };
      const expectedAction = {
        type: types.UPDATE_CARD,
        payload: {
          id: cardId,
          data: modifiedData
        }
      };
      expect(actions.updateCard(cardId, modifiedData)).toEqual(expectedAction);
    });

    it('should create archiveCard action', () => {
      const expectedAction = {
        type: types.ARCHIVE_CARD,
        payload: { id: cardId }
      };
      expect(actions.archiveCard(cardId)).toEqual(expectedAction);
    });

    it('should create deleteCard action', () => {
      const expectedAction = {
        type: types.DELETE_CARD,
        payload: { id: cardId }
      };
      expect(actions.deleteCard(cardId)).toEqual(expectedAction);
    });

    it('should create moveCard action', () => {
      const previousAndNextPositions = {};
      const expectedAction = {
        type: types.MOVE_CARD,
        payload: {
          dragResult: {},
          isSerial: false
        }
      };
      expect(actions.moveCard(previousAndNextPositions)).toEqual(
        expectedAction
      );
    });
  });

  describe('list', () => {
    const listId = 'card-01';

    it('should create addList action', () => {
      const payload = {
        name: 'card 1',
        isClosed: false,
        boardId: 'board-01'
      };
      const expectedAction = {
        type: types.ADD_LIST,
        payload
      };
      expect(actions.addList(payload)).toEqual(expectedAction);
    });

    it('should create updateList action', () => {
      const modifiedData = { name: 'new list name' };
      const expectedAction = {
        type: types.UPDATE_LIST,
        payload: {
          id: listId,
          data: modifiedData
        }
      };
      expect(actions.updateList(listId, modifiedData)).toEqual(expectedAction);
    });

    it('should create archiveList action', () => {
      const expectedAction = {
        type: types.ARCHIVE_LIST,
        payload: { id: listId }
      };
      expect(actions.archiveList(listId)).toEqual(expectedAction);
    });

    it('should create deleteList action', () => {
      const expectedAction = {
        type: types.DELETE_LIST,
        payload: { id: listId }
      };
      expect(actions.deleteList(listId)).toEqual(expectedAction);
    });

    it('should create moveList action', () => {
      const previousAndNextPositions = {};
      const expectedAction = {
        type: types.MOVE_LIST,
        payload: {
          dragResult: {}
        }
      };
      expect(actions.moveList(previousAndNextPositions)).toEqual(
        expectedAction
      );
    });
  });
});

describe('boardView reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      boardId: '',
      // Create card form
      isCreateCardFormOpen: false,
      isFocusOnCreateCardForm: false,
      createCardFormIndexToOpen: 0,
      // Search cards form
      searchTerm: '',
      // Create list form
      isCreateListFormOpen: false,
      isFocusOnCreateListForm: false,
      // Update list name form
      isUpdateListNameFormOpen: false,
      isFocusOnUpdateListNameForm: false,
      updateListNameFormIndexToOpen: 0,
      // Update board name form
      isUpdateBoardNameFormOpen: false,
      isFocusOnUpdateBoardNameForm: false
    });
  });

  describe('create card form', () => {
    it('should handle OPEN_CREATE_CARD_FORM', () => {
      const payload = 0;
      const action = actions.openCreateCardForm(0);
      expect(reducer({}, action)).toEqual({
        createCardFormIndexToOpen: payload,
        isCreateCardFormOpen: true
      });
    });

    it('should handle CLOSE_CREATE_CARD_FORM', () => {
      const action = actions.closeCreateCardForm();
      expect(reducer({}, action)).toEqual({
        createCardFormIndexToOpen: 0,
        isCreateCardFormOpen: false
      });
    });

    it('should handle FOCUS_CREATE_CARD_FORM', () => {
      const action = actions.focusOnCardForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnCreateCardForm: true
      });
    });

    it('should handle BLUR_CREATE_CARD_FORM', () => {
      const action = actions.blurOnCardForm();

      expect(reducer({}, action)).toEqual({
        isFocusOnCreateCardForm: false
      });
    });
  });

  describe('create list form', () => {
    it('should handle OPEN_CREATE_LIST_FORM', () => {
      const action = actions.openCreateListForm();
      expect(reducer({}, action)).toEqual({
        isCreateListFormOpen: true
      });
    });

    it('should handle CLOSE_CREATE_LIST_FORM', () => {
      const action = actions.closeCreateListForm();
      expect(reducer({}, action)).toEqual({
        isCreateListFormOpen: false
      });
    });

    it('should handle FOCUS_CREATE_LIST_FORM', () => {
      const action = actions.focusOnListForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnCreateListForm: true
      });
    });

    it('should handle BLUR_CREATE_LIST_FORM', () => {
      const action = actions.blurOnListForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnCreateListForm: false
      });
    });
  });

  describe('update board name form', () => {
    it('should handle FOCUS_ON_UPDATE_LIST_NAME_FORM', () => {
      const action = actions.focusOnUpdateListNameForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnUpdateListNameForm: true
      });
    });

    it('should handle BLUR_ON_UPDATE_LIST_NAME_FORM', () => {
      const action = actions.blurOnUpdateListNameForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnUpdateListNameForm: false
      });
    });
  });

  describe('update board name form', () => {
    it('should handle OPEN_UPDATE_BOARD_NAME_FORM', () => {
      const action = actions.openUpdateBoardNameForm();
      expect(reducer({}, action)).toEqual({
        isUpdateBoardNameOpen: true
      });
    });

    it('should handle CLOSE_UPDATE_BOARD_NAME_FORM', () => {
      const action = actions.closeUpdateBoardNameForm();
      expect(reducer({}, action)).toEqual({
        isUpdateBoardNameOpen: false
      });
    });

    it('should handle FOCUS_ON_UPDATE_BOARD_NAME_FORM', () => {
      const action = actions.focusOnUpdateBoardNameForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnUpdateBoardNameForm: true
      });
    });

    it('should handle BLUR_ON_UPDATE_BOARD_NAME_FORM', () => {
      const action = actions.blurOnUpdateBoardNameForm();
      expect(reducer({}, action)).toEqual({
        isFocusOnUpdateBoardNameForm: false
      });
    });
  });

  // describe('card', () => {
  //   it('should handle ADD_CARD', () => {});
  //   it('should handle UPDATE_CARD', () => {});
  //   it('should handle ARCHIVE_CARD', () => {});
  //   it('should handle ARCHIVE_CARD', () => {});
  //   it('should handle DELETE_CARD', () => {});
  //   it('should handle MOVE_CARD', () => {});
  // });

  // describe('list', () => {
  //   it('should handle ADD_LIST', () => {});
  //   it('should handle UPDATE_LIST', () => {});
  //   it('should handle ARCHIVE_LIST', () => {});
  //   it('should handle DELETE_LIST', () => {});
  //   it('should handle MOVE_LIST', () => {});
  // });
});

describe('boardView selectors', () => {
  it('should select the current board id', () => {
    const currentBoardId = selectors.selectCurrentBoardId(initialState);
    expect(currentBoardId).toBe('b-project');
  });

  // it('should select');
});
