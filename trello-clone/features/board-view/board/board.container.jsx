import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import { boardViewActionCreators, modelsActionCreators } from '../../../redux';

import { selectCurrentBoard } from '../../../redux/views/board-view/board-view.selectors';

import Board from './board.component';

const mapStateToProps = state => {
  const boardView = state.views.boardView;
  return {
    board: selectCurrentBoard(state),
    searchTerm: boardView.searchTerm,
    isCreateListFormOpen: boardView.isCreateListFormOpen
  };
};

const mapDispatchToProps = dispatch => {
  return {
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    modelsActions: bindActionCreators(modelsActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Board);
