import { firestoreTypes } from 'firebase/redux/firestore.types';
import { metaTypes } from '../models.types';
import * as actions from './boards.actions';

import { TEST_USER_ID } from '../../../utils/constants';

describe('boards actions', () => {
  const metaType = { type: metaTypes.boards };
  const boardId = 'board-01';
  const boardData = {
    id: boardId,
    name: 'New board',
    description: 'New board description',
    isClosed: false,
    isStarred: true,
    domainName: 'Domain 1',
    domainId: 'Domain-01',
    listIds: [],
    dateCreated: '',
    dateModified: ''
  };

  it('should create addBoard action', () => {
    const action = actions.addBoard(
      TEST_USER_ID,
      boardId,
      boardData,
      null,
      false
    );
    expect(action.type).toEqual(firestoreTypes.SET_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.data).toEqual(boardData);
  });

  it('should create updateBoard action', () => {
    const boardData = {
      name: 'Board name updated',
      description: 'Board description updated',
      dateModified: ''
    };
    const action = actions.updateBoard(
      TEST_USER_ID,
      boardId,
      boardData,
      null,
      false
    );
    expect(action.type).toEqual(firestoreTypes.UPDATE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(boardId);
    expect(action.payload.data).toEqual(boardData);
  });

  it('should create deleteBoard action', () => {
    const action = actions.deleteBoard(TEST_USER_ID, boardData);
    expect(action.type).toEqual(firestoreTypes.REMOVE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(boardId);
    expect(action.payload.data).toEqual(boardData);
  });

  it('should create listenToAllBoards action', () => {
    const action = actions.listenToAllBoards(TEST_USER_ID);
    expect(action.type).toEqual(firestoreTypes.ADD_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });

  it('should create removeBoardsListener action', () => {
    const action = actions.removeBoardsListener();
    expect(action.type).toEqual(firestoreTypes.REMOVE_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });
});
