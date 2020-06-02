import { cloneDeep } from 'lodash';

import { selectBoardById, selectBoards } from './boards/boards.selectors';
import { selectListById, selectLists } from './lists/lists.selectors';
import { selectCardById } from './cards/cards.selectors';

// Add card function

export function calculateAddNewCardOrders(state, newCardId, sourceListId) {
  const sourceList = selectListById(state, sourceListId);
  let cardOrders = [
    { listId: sourceList.id, cardIds: [...sourceList.cardIds, newCardId] }
  ];

  if (isMonitoredList(sourceList, 'Next')) {
    const nextBoardId = getBoardId(state, 'Next');
    const nextBoardList = getListByName(state, nextBoardId, sourceList.name);
    if (nextBoardList) {
      cardOrders.push({
        listId: nextBoardList.id,
        cardIds: [...nextBoardList.cardIds, newCardId]
      });
    }
  }

  if (isMonitoredList(sourceList, 'Today')) {
    const todayBoardId = getBoardId(state, 'Today');
    const todayBoardList = getListByName(state, todayBoardId, sourceList.name);
    if (todayBoardList) {
      cardOrders.push({
        listId: todayBoardList.id,
        cardIds: [...todayBoardList.cardIds, newCardId]
      });
    }
  }

  return cardOrders;
}

// Re-ordering functions

export function calculateNewListOrder(state, dragResult) {
  const { destination, source } = dragResult;
  const board = selectBoardById(state, source.droppableId);
  const newListOrder = reorder(board.listIds, source.index, destination.index);
  return { boardId: board.id, listIds: newListOrder };
}

export function calculateNewCardOrders(state, dragResult) {
  if (hasCardMovedBetweenLists(state, dragResult)) {
    return calculateNewCardOrdersBetweenLists(state, dragResult);
  } else {
    return calculateNewCardOrdersWithinSameList(state, dragResult);
  }
}

export function calculateNewCardOrdersWithinSameList(state, dragResult) {
  const { source, destination, draggableId } = dragResult;
  const sourceList = selectListById(state, source.droppableId);

  const newCardIds = reorder(
    sourceList.cardIds,
    source.index,
    destination.index
  );

  return {
    cardDetails: {
      cardId: draggableId,
      listId: destination.droppableId
    },
    cardOrders: [{ listId: sourceList.id, cardIds: newCardIds }]
  };
}

export function calculateNewCardOrdersBetweenLists(state, dragResult) {
  const dragResultForProjectBoard = createMirroredDragResult(
    state,
    dragResult,
    selectCardById(state, dragResult.draggableId).boardId
  );

  const dragResultForTodayBoard = createMirroredDragResult(
    state,
    dragResult,
    getBoardId(state, 'Today')
  );

  const dragResultForNextBoard = createMirroredDragResult(
    state,
    dragResult,
    getBoardId(state, 'Next')
  );

  return {
    cardDetails: {
      cardId: dragResultForProjectBoard.draggableId,
      listId: dragResultForProjectBoard.destination.droppableId
    },
    cardOrders: [
      ...calculateCardOrdersInProjectBoard(state, dragResultForProjectBoard),
      ...calculateCardOrdersInMirroredBoard(
        state,
        dragResultForTodayBoard,
        'Today'
      ),
      ...calculateCardOrdersInMirroredBoard(
        state,
        dragResultForNextBoard,
        'Next'
      )
    ]
  };
}

export function calculateCardOrdersInProjectBoard(state, dragResult) {
  if (dragResult.reason === 'CANCELLED') return [];

  let { source, destination, draggableId } = dragResult;
  let sourceList = selectListById(state, source.droppableId);
  let destinationList = selectListById(state, destination.droppableId);

  let newSourceCardIds = remove(sourceList.cardIds, source.index);
  let newDestinationCardIds = insert(
    destinationList.cardIds,
    destination.index,
    draggableId
  );

  return [
    { listId: sourceList.id, cardIds: newSourceCardIds },
    { listId: destinationList.id, cardIds: newDestinationCardIds }
  ];
}

export function calculateCardOrdersInMirroredBoard(
  state,
  dragResult,
  boardName
) {
  if (dragResult.reason === 'CANCELLED') return [];

  let { source, destination, draggableId } = dragResult;
  let sourceList = selectListById(state, source.droppableId);
  let destinationList = selectListById(state, destination.droppableId);

  if (isMovedIntoAMonitoredList(state, dragResult, boardName)) {
    let newCardIds = insert(
      destinationList.cardIds,
      destination.index,
      draggableId
    );
    return [{ listId: destinationList.id, cardIds: newCardIds }];
  }

  if (isMovedOutOfAMonitoredList(state, dragResult, boardName)) {
    let newCardIds = remove(sourceList.cardIds, source.index);
    return [{ listId: sourceList.id, cardIds: newCardIds }];
  }

  if (isMovedBetweenMonitoredLists(state, dragResult, boardName)) {
    let newSourceCardIds = remove(sourceList.cardIds, source.index);
    let newCardDestIds = insert(
      destinationList.cardIds,
      destination.index,
      draggableId
    );
    return [
      { listId: sourceList.id, cardIds: newSourceCardIds },
      { listId: destinationList.id, cardIds: newCardDestIds }
    ];
  }

  return [];
}

// Helper functions

export function hasCardMovedBetweenLists(state, dragResult) {
  const { source, destination } = dragResult;
  const sourceList = selectListById(state, source.droppableId);
  const destinationList = selectListById(state, destination.droppableId);

  return sourceList.id !== destinationList.id;
}

export function createMirroredDragResult(state, dragResult, mirroredBoardId) {
  // Todo: consider refactoring this monster into something more readable

  // No need to create a mirrored DragResult for the same
  // board, it's already been processed
  if (dragResult.boardId === mirroredBoardId) return dragResult;

  const mirroredDragResult = cloneDeep(dragResult);
  const { source, destination, draggableId } = dragResult;

  // source
  let mirroredSourceList = getMirroredList(
    state,
    mirroredBoardId,
    source.droppableId
  );
  if (mirroredSourceList) {
    mirroredDragResult.source.droppableId = mirroredSourceList.id;
    let mirroredSourceIndex = mirroredSourceList.cardIds.indexOf(draggableId);
    if (mirroredSourceIndex >= 0) {
      mirroredDragResult.source.index = mirroredSourceIndex;
    } else {
      // Card not found, source list is "Today", so search the "In Progress" list in mirror
      mirroredSourceList = getListByName(state, mirroredBoardId, 'In Progress');
      if (mirroredSourceList) {
        mirroredDragResult.source.droppableId = mirroredSourceList.id;
        mirroredSourceIndex = mirroredSourceList.cardIds.indexOf(draggableId);
        mirroredDragResult.source.index = mirroredSourceIndex;
      }
    }
  } else {
    let sourceList = selectListById(state, source.droppableId);
    if (sourceList.name === 'In Progress') {
      mirroredSourceList = getListByName(state, mirroredBoardId, 'Today');
      if (mirroredSourceList) {
        mirroredDragResult.source.droppableId = mirroredSourceList.id;
        let mirroredSourceIndex = mirroredSourceList.cardIds.indexOf(
          draggableId
        );
        mirroredDragResult.source.index = mirroredSourceIndex;
      }
    }
  }

  // destination
  let mirroredDestList = getMirroredList(
    state,
    mirroredBoardId,
    destination.droppableId
  );
  let sourceList = selectListById(state, source.droppableId);
  let destinationList = selectListById(state, destination.droppableId);
  if (mirroredDestList) {
    if (sourceList.name === 'In Progress' && destinationList.name === 'Today') {
      mirroredDragResult.reason = 'CANCELLED';
      mirroredDragResult.destination.droppableId = mirroredSourceList.id;
    } else {
      mirroredDragResult.destination.droppableId = mirroredDestList.id;
      mirroredDragResult.destination.index =
        mirroredDestList.name === 'Done' ? 0 : mirroredDestList.cardIds.length;
    }
  } else {
    if (destinationList.name === 'In Progress') {
      if (mirroredSourceList.name === 'Today') {
        mirroredDragResult.reason = 'CANCELLED';
        mirroredDragResult.destination.droppableId = mirroredSourceList.id;
      } else {
        mirroredDestList = getListByName(state, mirroredBoardId, 'Today');
        mirroredDragResult.destination.droppableId = mirroredDestList.id;
        mirroredDragResult.destination.index = mirroredDestList.cardIds.length;
      }
    }
  }

  return mirroredDragResult;
}

export function createDragResultAction(
  boardId,
  cardId,
  sourceIndex,
  sourceList,
  destinationList,
  index = 0
) {
  return {
    boardId: boardId,
    draggableId: cardId,
    type: 'card',
    reason: 'DROP',
    source: {
      droppableId: sourceList.id,
      index: sourceIndex
    },
    destination: {
      droppableId: destinationList.id,
      index: index
    }
  };
}

export function getMirroredList(state, mirroredBoardId, sourceListId) {
  let sourceList = selectListById(state, sourceListId);
  let mirroredList = getListByName(state, mirroredBoardId, sourceList.name);
  return mirroredList;
}

export function getListByName(state, boardId, listName) {
  let allLists = selectLists(state);
  let boardLists = allLists.filter(list => list.boardId === boardId);
  let mirroredList = boardLists.find(list => list.name === listName);
  return mirroredList;
}

export function getBoardId(state, boardName) {
  let allBoards = selectBoards(state);
  let nextBoard = allBoards.find(board => board.name === boardName);
  return nextBoard.id;
}

export function isEventFromProjectBoard(state, dragResult) {
  return !isEventFromMirroredBoard(state, dragResult);
}

export function isEventFromMirroredBoard(state, dragResult) {
  let sourceList = selectListById(state, dragResult.source.droppableId);
  let sourceBoard = selectBoardById(state, sourceList.boardId);
  let mirroredBoardName = ['Today', 'Next'];
  return mirroredBoardName.includes(sourceBoard.name);
}

export function isMovedIntoAMonitoredList(state, dragResult, boardName) {
  const { source, destination } = dragResult;
  const sourceList = selectListById(state, source.droppableId);
  const destinationList = selectListById(state, destination.droppableId);

  return (
    !isMonitoredList(sourceList, boardName) &&
    isMonitoredList(destinationList, boardName)
  );
}

export function isMovedOutOfAMonitoredList(state, dragResult, boardName) {
  const { source, destination } = dragResult;
  const sourceList = selectListById(state, source.droppableId);
  const destinationList = selectListById(state, destination.droppableId);

  return (
    isMonitoredList(sourceList, boardName) &&
    !isMonitoredList(destinationList, boardName)
  );
}

export function isMovedBetweenMonitoredLists(state, dragResult, boardName) {
  const { source, destination } = dragResult;
  const sourceList = selectListById(state, source.droppableId);
  const destinationList = selectListById(state, destination.droppableId);

  return (
    isMonitoredList(sourceList, boardName) &&
    isMonitoredList(destinationList, boardName)
  );
}

export function isMonitoredList(list, boardName) {
  let monitoredLists = [];
  if (boardName === 'Next') monitoredLists = ['Next', 'Today', 'Doing', 'Done'];
  if (boardName === 'Today') monitoredLists = ['Today', 'In Progress', 'Done'];
  return monitoredLists.includes(list.name);
}

// Utility functions

export function reorder(list, startIndex, endIndex) {
  const result = Array.from(list);
  const [removed] = result.splice(startIndex, 1);
  result.splice(endIndex, 0, removed);

  return result;
}

export function remove(list, index) {
  const result = Array.from(list);
  result.splice(index, 1);

  return result;
}

export function insert(list, index, item) {
  let result = Array.from(list);
  result.splice(index, 0, item);

  return result;
}

export function append(list, item) {
  return [...list, item];
}
