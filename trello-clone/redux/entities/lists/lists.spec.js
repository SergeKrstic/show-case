import { firestoreTypes } from 'firebase/redux/firestore.types';
import { metaTypes } from '../models.types';
import * as actions from './lists.actions';

import { TEST_USER_ID } from '../../../utils/constants';

describe('lists actions', () => {
  const metaType = { type: metaTypes.lists };
  const listId = 'list-01';
  const listData = {
    id: listId,
    name: 'New list',
    isClosed: false,
    cardIds: [],
    boardId: 'board-01',
    dateCreated: '',
    dateModified: ''
  };

  it('should create addList action', () => {
    const action = actions.addList(TEST_USER_ID, listId, listData, null, false);
    expect(action.type).toEqual(firestoreTypes.SET_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.data).toEqual(listData);
  });

  it('should create updateList action', () => {
    const listData = {
      name: 'List name updated',
      description: 'List description updated',
      dateModified: ''
    };
    const action = actions.updateList(
      TEST_USER_ID,
      listId,
      listData,
      null,
      false
    );
    expect(action.type).toEqual(firestoreTypes.UPDATE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(listId);
    expect(action.payload.data).toEqual(listData);
  });

  it('should create deleteList action', () => {
    const action = actions.deleteList(TEST_USER_ID, listData);
    expect(action.type).toEqual(firestoreTypes.REMOVE_DOCUMENT_REQUEST);
    expect(action.meta).toEqual(metaType);
    expect(action.payload.id).toEqual(listId);
    expect(action.payload.data).toEqual(listData);
  });

  it('should create listenToLists action', () => {
    const action = actions.listenToAllLists(TEST_USER_ID);
    expect(action.type).toEqual(firestoreTypes.ADD_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });

  it('should create removeListsListener action', () => {
    const action = actions.removeListsListener();
    expect(action.type).toEqual(firestoreTypes.REMOVE_LISTENER_REQUEST);
    expect(action.meta).toEqual(metaType);
  });
});
