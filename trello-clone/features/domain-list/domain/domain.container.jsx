import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import Domain from './domain.component';

import {
  homeViewActionCreators,
  boardViewActionCreators,
  boardsMenuActionCreators,
  modelsActionCreators
} from '../../../redux';

const mapDispatchToProps = dispatch => {
  return {
    homeViewActions: bindActionCreators(homeViewActionCreators, dispatch),
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    modelsActions: bindActionCreators(modelsActionCreators, dispatch),
    boardsMenuActions: bindActionCreators(boardsMenuActionCreators, dispatch)
  };
};

export default connect(null, mapDispatchToProps)(Domain);
