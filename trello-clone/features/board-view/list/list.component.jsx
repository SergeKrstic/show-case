import React, { useState } from 'react';
import PropTypes from 'prop-types';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus, faEllipsisH } from '@fortawesome/free-solid-svg-icons';

import UpdateListName from '../../forms/update-list-name/update-list-name.container';

import ListMenu from '../../menus/list-menu/list-menu.component';
import CardListDroppable from '../card-list/card-list.droppable';
import useListStyles from './list.styles';

const List = ({
  index,
  board,
  list,
  isUpdateListNameFormOpen,
  updateListNameFormIndexToOpen,
  isCreateCardFormOpen,
  createCardFormIndexToOpen,
  boardViewActions,
  modelsActions,
  dragHandleProps
}) => {
  const classes = useListStyles();
  const [anchorElement, setAnchorElement] = useState(null);

  const handleOpenMenu = event => {
    setAnchorElement(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setAnchorElement(null);
  };

  const renderUpdateListName = () => {
    if (isMirrorBoard()) return <h2>{list.name}</h2>;

    if (isUpdateListNameFormOpen && updateListNameFormIndexToOpen === index) {
      return (
        <UpdateListName
          form={'list-' + list.id}
          initialValues={{ name: list.name }}
          onSubmit={updateListName}
        />
      );
    } else {
      return <h2 onClick={handleOpenUpdateListNameForm}>{list.name}</h2>;
    }
  };

  const handleOpenUpdateListNameForm = () => {
    boardViewActions.openUpdateListNameForm({ listIndex: index });
  };

  const updateListName = formInput => {
    modelsActions.updateList({
      id: list.id,
      data: { name: formInput.name }
    });
  };

  const renderAddCard = () => {
    if (isMirrorBoard()) return null;
    const newCardCaption =
      list.cardIds.length === 0 ? 'Add a card' : 'Add another card';
    if (!isCreateCardFormOpen || createCardFormIndexToOpen !== index) {
      return (
        <div className={classes.addCard} onClick={handleOpenCreateCardForm}>
          <div className={classes.addCardContent}>
            <FontAwesomeIcon icon={faPlus} className={classes.addIcon} />
            {newCardCaption}
          </div>
        </div>
      );
    }
  };

  const isMirrorBoard = () => {
    return board.name === 'Today' || board.name === 'Next';
  };

  const handleOpenCreateCardForm = () => {
    boardViewActions.openCreateCardForm({ listIndex: index });
  };

  return (
    <div className={classes.list}>
      <div className={classes.listContent}>
        <div {...dragHandleProps}>
          <div className={classes.listContentHeader}>
            {renderUpdateListName()}
            <div
              className={classes.listContentHeaderMenu}
              onClick={handleOpenMenu}
            >
              <FontAwesomeIcon icon={faEllipsisH} />
            </div>
          </div>
        </div>
        <ListMenu anchorElement={anchorElement} handleClose={handleCloseMenu} />
        <CardListDroppable
          id={list.id}
          index={index}
          board={board}
          list={list}
          createCardFormIndexToOpen={createCardFormIndexToOpen}
          isCreateCardFormOpen={isCreateCardFormOpen}
          boardViewActions={boardViewActions}
          modelsActions={modelsActions}
        />
        <div className={classes.listContentFooter}>{renderAddCard()}</div>
      </div>
    </div>
  );
};

List.propTypes = {
  index: PropTypes.number.isRequired,
  board: PropTypes.object.isRequired,
  list: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    cardIds: PropTypes.array.isRequired
  }),
  isUpdateListNameFormOpen: PropTypes.bool.isRequired,
  updateListNameFormIndexToOpen: PropTypes.number.isRequired,
  isCreateCardFormOpen: PropTypes.bool.isRequired,
  createCardFormIndexToOpen: PropTypes.number.isRequired,
  boardViewActions: PropTypes.object.isRequired,
  modelsActions: PropTypes.object.isRequired
};

List.defaultProps = {
  dragHandleProps: {}
};

export default List;
