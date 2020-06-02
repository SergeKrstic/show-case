import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import SearchCards from './search-cards.component';

import { boardViewActionCreators as actions } from '../../../redux';

function mapStateToProps(state) {
  return {
    searchTerm: state.views.boardView.searchTerm
  };
}

function mapDispatchToProps(dispatch) {
  return {
    onSearchTermChange: bindActionCreators(actions.updateSearchTerm, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(SearchCards);
