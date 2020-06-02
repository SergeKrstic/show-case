import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import { modelsActionCreators } from '../../../redux';

import { selectCurrentBoard } from '../../../redux/views/board-view/board-view.selectors';

import BoardHeader from './board-header.component';

const mapStateToProps = state => {
  const boardView = state.views.boardView;
  return {
    board: selectCurrentBoard(state),
    isFocusOnUpdateBoardNameForm: boardView.isFocusOnUpdateBoardNameForm,
    isUpdateBoardNameOpen: boardView.isUpdateBoardNameOpen
  };
};

const mapDispatchToProps = dispatch => {
  return {
    modelsActions: bindActionCreators(modelsActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(BoardHeader);
