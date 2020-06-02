import React, { Component } from 'react';

import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import App from './app.component';

import {
  modalsActionCreators,
  boardsMenuActionCreators,
  popOverActionCreators,
  sessionActionCreators,
  boardViewActionCreators,
  modelsActionCreators
} from './redux';

import {
  TEST_USER_ID,
  TEST_BOARD_ID,
  LIVE_USER_ID,
  LIVE_BOARD_ID
} from './utils/constants';

// Todo: remove this temporary hack
function getBoardId(userId) {
  let boardId = '';

  boardId = userId === TEST_USER_ID ? TEST_BOARD_ID : boardId;
  boardId = userId === LIVE_USER_ID ? LIVE_BOARD_ID : boardId;

  return boardId;
}

class AppContainer extends Component {
  componentDidMount() {
    const {
      sessionActions,
      boardViewActions,
      modelsActions,
      user
    } = this.props;
    const boardId = getBoardId(user.id);

    sessionActions.updateUser({
      userId: user.id,
      userName: user.displayName
    });

    boardViewActions.setBoardId({ id: boardId });
    modelsActions.addBoardListeners({ id: boardId });
  }

  componentDidUpdate(prevProps) {
    // Todo: test and fix this...
    if (
      this.props.userId !== prevProps.userId ||
      this.props.boardId !== prevProps.boardId
    ) {
      const { boardId, modelsActions } = this.props;
      modelsActions.removeBoardListeners({ id: boardId });
      modelsActions.addBoardListeners({ id: boardId });
      // modelsActions.removeOldCardsInDoneList({ boardId });
      // modelsActions.moveOldTodayCardsToDoingList({ moveAll: false });
    }
  }

  componentWillUnmount() {
    // Todo: test and fix this...
    const { boardId, modelsActions } = this.props;
    modelsActions.removeBoardListeners({ id: boardId });
  }

  render() {
    return <App {...this.props} />;
  }
}

const mapStateToProps = state => {
  const { isHomeViewOpen } = state.views.homeView;
  const { isFocusOnBoardsMenu, isBoardsMenuOpen } = state.views.boardsMenu;
  const { isFocusOnPopOver, isPopOverOpen } = state.views.popOver;
  const { isFocusOnModal, isModalOpen } = state.views.modals;
  const { isCardViewOpen } = state.views.cardView;

  return {
    isHomeViewOpen,

    isFocusOnBoardsMenu,
    isBoardsMenuOpen,

    isFocusOnPopOver,
    isPopOverOpen,

    isFocusOnModal,
    isModalOpen,

    isCardViewOpen
  };
};

const mapDispatchToProps = dispatch => {
  return {
    boardsMenuActions: bindActionCreators(boardsMenuActionCreators, dispatch),
    popOverActions: bindActionCreators(popOverActionCreators, dispatch),
    modalActions: bindActionCreators(modalsActionCreators, dispatch),
    sessionActions: bindActionCreators(sessionActionCreators, dispatch),
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    modelsActions: bindActionCreators(modelsActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(AppContainer);
