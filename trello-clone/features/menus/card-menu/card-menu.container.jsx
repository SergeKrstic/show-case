import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import CardMenu from './card-menu.component';

import { modelsActionCreators } from '../../../redux/index';

const mapDispatchToProps = dispatch => {
  return {
    modelsActions: bindActionCreators(modelsActionCreators, dispatch)
  };
};

export default connect(null, mapDispatchToProps)(CardMenu);
