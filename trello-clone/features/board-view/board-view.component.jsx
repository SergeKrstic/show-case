import React from 'react';
import PropTypes from 'prop-types';
import Div100vh from 'react-div-100vh';

import Toolbar from './toolbar/toolbar.container';
import BoardHeader from './board-header/board-header.container';
import Board from './board/board.container';
import useBoardStyles from './board-view.styles';

const BoardView = ({
  isFocusOnUpdateBoardNameForm,
  isUpdateBoardNameFormOpen,

  isFocusOnUpdateListNameForm,
  isUpdateListNameFormOpen,

  isFocusOnCreateListForm,
  isCreateListFormOpen,

  isFocusOnCreateCardForm,
  isCreateCardFormOpen,

  boardViewActions
}) => {
  const classes = useBoardStyles();

  const handleDocumentClick = () => {
    if (!isFocusOnUpdateBoardNameForm && isUpdateBoardNameFormOpen) {
      boardViewActions.closeUpdateBoardNameForm();
    }

    if (!isFocusOnUpdateListNameForm && isUpdateListNameFormOpen) {
      boardViewActions.closeUpdateListNameForm();
    }

    if (!isFocusOnCreateListForm && isCreateListFormOpen) {
      boardViewActions.closeCreateListForm();
    }

    if (!isFocusOnCreateCardForm && isCreateCardFormOpen) {
      boardViewActions.closeCreateCardForm();
    }
  };

  const handleEscKey = event => {
    if (event.keyCode === 27) {
      if (isUpdateBoardNameFormOpen) {
        boardViewActions.closeUpdateBoardNameForm();
      }

      if (isUpdateListNameFormOpen) {
        boardViewActions.closeUpdateListNameForm();
      }

      if (isCreateListFormOpen) {
        boardViewActions.closeCreateListForm();
      }

      if (isCreateCardFormOpen) {
        boardViewActions.closeCreateCardForm();
      }
    }
  };

  return (
    <Div100vh
      className={classes.boardCanvas}
      onClickCapture={handleDocumentClick}
      onKeyDown={handleEscKey}
      tabIndex="0"
    >
      <Toolbar />
      <BoardHeader />
      <Board />
    </Div100vh>
  );
};

BoardView.propTypes = {
  isFocusOnUpdateBoardNameForm: PropTypes.bool.isRequired,
  isUpdateBoardNameFormOpen: PropTypes.bool.isRequired,

  isFocusOnUpdateListNameForm: PropTypes.bool.isRequired,
  isUpdateListNameFormOpen: PropTypes.bool.isRequired,

  isFocusOnCreateListForm: PropTypes.bool.isRequired,
  isCreateListFormOpen: PropTypes.bool.isRequired,

  isFocusOnCreateCardForm: PropTypes.bool.isRequired,
  isCreateCardFormOpen: PropTypes.bool.isRequired,

  boardViewActions: PropTypes.object.isRequired
};

export default BoardView;
