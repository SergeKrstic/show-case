import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import ListDraggable from './list.draggable';

import { selectBoardById } from '../../../redux/entities/boards/boards.selectors';
import { selectListById } from '../../../redux/entities/lists/lists.selectors';
import {
  boardViewActionCreators,
  modelsActionCreators
} from '../../../redux/index';

const mapStateToProps = (state, props) => {
  const boardView = state.views.boardView;

  return {
    isUpdateListNameFormOpen: boardView.isUpdateListNameFormOpen,
    updateListNameFormIndexToOpen: boardView.updateListNameFormIndexToOpen,
    isCreateCardFormOpen: boardView.isCreateCardFormOpen,
    createCardFormIndexToOpen: boardView.createCardFormIndexToOpen,
    board: selectBoardById(state, boardView.boardId),
    list: selectListById(state, props.id)
  };
};

const mapDispatchToProps = dispatch => {
  return {
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    modelsActions: bindActionCreators(modelsActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(ListDraggable);
