import React from 'react';
import PropTypes from 'prop-types';
// import ScrollContainer from 'react-indiana-drag-scroll';
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

import List from '../list/list.container';
import CreateList from '../../forms/create-list/create-list.container';
import useBoardStyles from './board.styles';
import { hasNotMoved } from './board.utils';

const Board = ({
  board,
  searchTerm,
  isCreateListFormOpen,
  boardViewActions,
  modelsActions
}) => {
  const classes = useBoardStyles();

  const handleDragEnd = dragResult => {
    if (hasNotMoved(dragResult)) return;

    if (dragResult.type === 'list') {
      modelsActions.moveList({ dragResult });
    } else {
      modelsActions.moveCard({ dragResult, boardId: board.id });
    }
  };

  const handleAddList = formInput => {
    const list = {
      name: formInput.name.trim(),
      isClosed: false,
      boardId: board.id,
      cardIds: []
    };
    modelsActions.addList(list);
  };

  const handleOpenCreateList = () => {
    boardViewActions.openCreateListForm();
  };

  const renderLists = () => {
    return board.listIds.map((listId, index) => (
      <List index={index} key={listId} id={listId} />
    ));
  };

  const renderAddList = () => {
    if (board.name === 'Today' || board.name === 'Next') return null;
    if (isCreateListFormOpen) {
      return (
        <div>
          <CreateList onSubmit={handleAddList} />
        </div>
      );
    } else {
      const listCaption =
        Object.keys(board.listIds).length === 0
          ? 'Add a list...'
          : 'Add another list...';
      return (
        <div className={classes.addList} onClick={handleOpenCreateList}>
          <span>
            <FontAwesomeIcon icon={faPlus} className={classes.addIcon} />
            {listCaption}
          </span>
        </div>
      );
    }
  };

  if (!board) return null;

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <Droppable droppableId={board.id} direction="horizontal" type="list">
        {provided => (
          <div
            className={classes.board}
            ref={provided.innerRef}
            {...provided.droppableProps}
          >
            {renderLists()}
            {provided.placeholder}
            <div>{renderAddList()}</div>
          </div>
        )}
      </Droppable>
    </DragDropContext>
  );
};

Board.propTypes = {
  board: PropTypes.object,
  isCreateListFormOpen: PropTypes.bool.isRequired,
  boardViewActions: PropTypes.object.isRequired,
  modelsActions: PropTypes.object.isRequired,
  searchTerm: PropTypes.string
};

Board.defaultProps = {
  searchTerm: ''
};

export default Board;
