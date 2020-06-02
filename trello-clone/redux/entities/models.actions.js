import { createAction } from '@reduxjs/toolkit';

// ================================================================================
// Card actions
// ================================================================================

export const addCard = createAction(
  'models/addCard',
  ({ name, description, isClosed, boardName, boardId, listId }) => ({
    payload: { name, description, isClosed, boardName, boardId, listId }
  })
);

export const updateCard = createAction('models/updateCard', ({ id, data }) => ({
  payload: { id, data }
}));

export const archiveCard = createAction('models/archiveCard', ({ id }) => ({
  payload: { id }
}));

export const deleteCard = createAction('models/deleteCard', ({ id }) => ({
  payload: { id }
}));

export const moveCard = createAction(
  'models/moveCard',
  ({ dragResult, boardId, batch = null, isMultiMoveComplete = false }) => ({
    payload: {
      dragResult: { ...dragResult, boardId },
      batch,
      isMultiMoveComplete
    }
  })
);

export const toggleCardLabel = createAction(
  'models/toggleCardLabel',
  ({ labelColor }) => ({
    payload: { labelColor }
  })
);

// ================================================================================
// List actions
// ================================================================================

export const addList = createAction(
  'models/addList',
  ({ name, isClosed, boardId, cardIds }) => ({
    payload: { name, isClosed, boardId, cardIds }
  })
);

export const updateList = createAction('models/updateList', ({ id, data }) => ({
  payload: { id, data }
}));

export const archiveList = createAction('models/archiveList', ({ id }) => ({
  payload: { id }
}));

export const increment = createAction('models/increment', ({ id }) => ({
  payload: { id }
}));

export const moveList = createAction('models/moveList', ({ dragResult }) => ({
  payload: { dragResult }
}));

export const resetLists = createAction('models/resetLists', () => ({
  payload: {}
}));

// ================================================================================
// board actions
// ================================================================================

export const addBoardListeners = createAction(
  'models/addBoardListeners',
  ({ id }) => ({ payload: { id } })
);

export const removeBoardListeners = createAction(
  'models/removeBoardListeners',
  ({ id }) => ({ payload: { id } })
);

export const addBoard = createAction(
  'models/addBoard',
  ({ name, domainId, domainName }) => ({
    payload: {
      name,
      domainId,
      domainName,
      description: '',
      isClosed: false,
      isStarred: false,
      listIds: []
    }
  })
);

export const updateBoard = createAction(
  'models/updateBoard',
  ({ id, data }) => ({
    payload: { id, data }
  })
);

export const removeOldCardsInDoneList = createAction(
  'models/removeOldCardsInDoneList',
  ({ boardId }) => ({ payload: { boardId } })
);

export const moveOldTodayCardsToDoingList = createAction(
  'models/moveOldTodayCardsToDoingList',
  ({ moveAll }) => ({ payload: { moveAll } })
);

export const sendWellDoneMessage = createAction(
  'models/sendWellDoneMessage',
  () => ({ payload: {} })
);

// ================================================================================
// domain actions
// ================================================================================

export const addDomain = createAction('models/addDomain', ({ name }) => ({
  payload: { name, description: '', boardIds: [] }
}));
