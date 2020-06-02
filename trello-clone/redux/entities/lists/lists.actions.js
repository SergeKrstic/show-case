import { api } from '../../../api';

import * as actions from 'firebase/redux/firestore.actions';
import { Timestamp } from 'firebase/utils/firebase.utils';
import { metaTypes } from '../models.types';

export function addList(
  userId,
  listId,
  { id, name, isClosed, boardId, cardIds } = {},
  batch = null,
  hasTimestamp = true
) {
  let setFunc = api(userId).lists.set;
  let data = {
    id,
    name,
    isClosed,
    boardId,
    cardIds,
    dateCreated: hasTimestamp ? Timestamp.now() : '',
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.setDocument(metaTypes.lists, setFunc, listId, data, batch);
}

export function updateList(
  userId,
  listId,
  data,
  batch = null,
  hasTimestamp = true
) {
  const updateFunc = api(userId).lists.update;
  let dataWithTimestamp = {
    ...data,
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.updateDocument(
    metaTypes.lists,
    updateFunc,
    listId,
    dataWithTimestamp,
    batch
  );
}

export function deleteList(userId, list, batch = null) {
  const deleteFunc = api(userId).lists.delete;
  return actions.removeDocument(
    metaTypes.lists,
    deleteFunc,
    list.id,
    list,
    batch
  );
}

export function listenToAllLists(userId) {
  const ref = api(userId).listsRef;
  return actions.addListener(metaTypes.lists, ref);
}

export function removeListsListener() {
  return actions.removeListener(metaTypes.lists, false);
}
