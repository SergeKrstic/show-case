import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import { boardsMenuActionCreators } from '../../../redux';

import AllBoardsMenu from './all-boards-menu.component';

const mapDispatchToProps = dispatch => {
  return {
    boardsMenuActions: bindActionCreators(boardsMenuActionCreators, dispatch)
  };
};

export default connect(null, mapDispatchToProps)(AllBoardsMenu);
