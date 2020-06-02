import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import DomainList from './domain-list.component';

import { selectDomains } from '../../redux/entities/domains/domains.selectors';
import { selectBoards } from '../../redux/entities/boards/boards.selectors';
import { modelsActionCreators } from '../../redux';

const mapStateToProps = state => {
  return {
    domains: selectDomains(state),
    boards: selectBoards(state),
    boardFilterText: state.views.boardsMenu.userInput
  };
};

const mapDispatchToProps = dispatch => {
  return {
    modelsActions: bindActionCreators(modelsActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(DomainList);
