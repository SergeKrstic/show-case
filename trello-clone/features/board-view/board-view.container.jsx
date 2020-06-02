import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import BoardView from './board-view.component';
import useBoardStyles from './board-view.styles';

import { selectUserId } from '../../redux/session/session.selectors';
import { modelsActionCreators, boardViewActionCreators } from '../../redux';

const BoardViewWrapper = props => {
  const classes = useBoardStyles();
  return (
    <div className={classes.boardWrapper}>
      <BoardView {...props} />
    </div>
  );
};

class BoardViewContainer extends Component {
  // componentDidMount() {
  //   if (this.props.userId) {
  //     const { boardId, modelsActions } = this.props;
  //     modelsActions.addBoardListeners(boardId);
  //   }
  // }

  componentDidUpdate(prevProps) {
    if (
      this.props.userId !== prevProps.userId ||
      this.props.boardId !== prevProps.boardId
    ) {
      const { boardId, modelsActions } = this.props;
      // modelsActions.removeBoardListeners(boardId);
      // modelsActions.addBoardListeners(boardId);
      modelsActions.removeOldCardsInDoneList({ boardId });
      modelsActions.moveOldTodayCardsToDoingList({ moveAll: false });
    }
  }

  // componentWillUnmount() {
  //   const { boardId, modelsActions } = this.props;
  //   modelsActions.removeBoardListeners(boardId);
  // }

  render() {
    return <BoardViewWrapper {...this.props} />;
  }
}

const mapStateToProps = state => {
  const boardView = state.views.boardView;

  return {
    userId: selectUserId(state),
    boardId: boardView.boardId,

    isCreateCardFormOpen: boardView.isCreateCardFormOpen,
    isFocusOnCreateCardForm: boardView.isFocusOnCreateCardForm,

    isCreateListFormOpen: boardView.isCreateListFormOpen,
    isFocusOnCreateListForm: boardView.isFocusOnCreateListForm,

    isUpdateListNameFormOpen: boardView.isUpdateListNameFormOpen,
    isFocusOnUpdateListNameForm: boardView.isFocusOnUpdateListNameForm,

    isUpdateBoardNameFormOpen: boardView.isUpdateBoardNameFormOpen,
    isFocusOnUpdateBoardNameForm: boardView.isFocusOnUpdateBoardNameForm
  };
};

const mapDispatchToProps = dispatch => {
  return {
    modelsActions: bindActionCreators(modelsActionCreators, dispatch),
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(BoardViewContainer);
