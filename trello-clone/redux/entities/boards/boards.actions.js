import { api } from '../../../api';

import * as actions from 'firebase/redux/firestore.actions';
import { Timestamp } from 'firebase/utils/firebase.utils';
import { metaTypes } from '../models.types';

export function addBoard(
  userId,
  boardId,
  {
    id,
    name,
    description,
    isClosed,
    isStarred,
    domainName,
    domainId,
    listIds
  } = {},
  batch = null,
  hasTimestamp = true
) {
  let setFunc = api(userId).boards.set;
  let data = {
    id,
    name,
    description,
    isClosed,
    isStarred,
    domainName,
    domainId,
    listIds,
    dateCreated: hasTimestamp ? Timestamp.now() : '',
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.setDocument(metaTypes.boards, setFunc, boardId, data);
}

export function updateBoard(
  userId,
  boardId,
  data,
  batch = null,
  hasTimestamp = true
) {
  let updateFunc = api(userId).boards.update;
  let dataWithTimestamp = {
    ...data,
    dateModified: hasTimestamp ? Timestamp.now() : ''
  };
  return actions.updateDocument(
    metaTypes.boards,
    updateFunc,
    boardId,
    dataWithTimestamp,
    batch
  );
}

export function deleteBoard(userId, board, batch = null) {
  let deleteFunc = api(userId).boards.delete;
  return actions.removeDocument(
    metaTypes.boards,
    deleteFunc,
    board.id,
    board,
    batch
  );
}

export function listenToAllBoards(userId) {
  let ref = api(userId).boardsRef;
  return actions.addListener(metaTypes.boards, ref);
}

export function removeBoardsListener() {
  return actions.removeListener(metaTypes.boards, false);
}
