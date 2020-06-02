import React from 'react';
import PropTypes from 'prop-types';
import Div100vh from 'react-div-100vh';
import { HotKeys } from 'react-hotkeys';

import {
  HomeView,
  AllBoardsMenu,
  PopOver,
  BoardView,
  CardView
} from './features/index';
import { keyMap, useHandlers } from './app.shortcuts';
import ErrorToast from 'redux/error/error-toast.container';

import useAppStyles from './app.styles';

const App = ({
  isHomeViewOpen,

  isFocusOnBoardsMenu,
  isBoardsMenuOpen,

  isFocusOnPopOver,
  isPopOverOpen,

  isFocusOnModal,
  isModalOpen,

  isCardViewOpen,

  ...actions
}) => {
  const classes = useAppStyles();
  const handlers = useHandlers(actions);

  // document.body.style.overflow = 'unset';

  const handleDocumentClick = () => {
    if (!isFocusOnModal && isModalOpen) {
      actions.modalActions.closeAllModals();
    }

    if (!isFocusOnPopOver && isPopOverOpen) {
      actions.popOverActions.hidePopOver();
    }

    if (!isFocusOnBoardsMenu && isBoardsMenuOpen) {
      actions.boardsMenuActions.hideBoardsMenu();
    }
  };

  const handleEscKey = event => {
    if (event.keyCode === 27) {
      if (isModalOpen) {
        actions.modalActions.closeAllModals();
      }

      if (isPopOverOpen) {
        actions.popOverActions.hidePopOver();
      }

      if (isBoardsMenuOpen) {
        actions.boardsMenuActions.hideBoardsMenu();
      }
    }
  };

  const renderMainView = () => {
    return isHomeViewOpen ? <HomeView /> : <BoardView />;
  };

  const renderPopOver = () => {
    return isPopOverOpen ? <PopOver /> : null;
  };

  const renderBoardsMenu = () => {
    return isBoardsMenuOpen ? <AllBoardsMenu /> : null;
  };

  const renderCardView = () => {
    return isCardViewOpen ? <CardView /> : null;
  };

  return (
    <HotKeys keyMap={keyMap} handlers={handlers}>
      <Div100vh
        className={classes.app}
        tabIndex="0"
        onClickCapture={handleDocumentClick}
        onKeyDown={handleEscKey}
      >
        <div className={classes.container}>
          {renderMainView()}
          {renderPopOver()}
          {renderBoardsMenu()}
          {renderCardView()}
          <ErrorToast />
        </div>
      </Div100vh>
    </HotKeys>
  );
};

App.propTypes = {
  isHomeViewOpen: PropTypes.bool.isRequired,

  isFocusOnBoardsMenu: PropTypes.bool.isRequired,
  isBoardsMenuOpen: PropTypes.bool.isRequired,

  isFocusOnPopOver: PropTypes.bool.isRequired,
  isPopOverOpen: PropTypes.bool.isRequired,

  isFocusOnModal: PropTypes.bool.isRequired,
  isModalOpen: PropTypes.bool.isRequired,

  boardsMenuActions: PropTypes.object.isRequired,
  popOverActions: PropTypes.object.isRequired,
  modalActions: PropTypes.object.isRequired,

  isCardViewOpen: PropTypes.bool.isRequired
};

export default App;
