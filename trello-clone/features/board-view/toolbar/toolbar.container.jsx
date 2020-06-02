import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import Toolbar from './toolbar.component';

import { selectBoards } from '../../../redux/entities/boards/boards.selectors';
import { selectCurrentBoardId } from '../../../redux/views/board-view/board-view.selectors';

import {
  homeViewActionCreators,
  boardViewActionCreators,
  boardsMenuActionCreators
} from '../../../redux';

const mapStateToProps = state => {
  return {
    boards: selectBoards(state),
    activeBoardId: selectCurrentBoardId(state)
  };
};

const mapDispatchToProps = dispatch => {
  return {
    homeViewActions: bindActionCreators(homeViewActionCreators, dispatch),
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    boardsMenuActions: bindActionCreators(boardsMenuActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Toolbar);
