import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import HomeView from './home-view.component';

import { selectDomains } from '../../redux/entities/domains/domains.selectors';
import { selectBoards } from '../../redux/entities/boards/boards.selectors';
import { homeViewActionCreators } from '../../redux';

const mapStateToProps = state => {
  return {
    domains: selectDomains(state),
    boards: selectBoards(state),
    activeBoardId: state.views.boardView.boardId
  };
};

const mapDispatchToProps = dispatch => {
  return {
    homeViewActions: bindActionCreators(homeViewActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(HomeView);
