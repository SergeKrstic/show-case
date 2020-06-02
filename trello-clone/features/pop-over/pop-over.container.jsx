import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

// import { popOverActionCreators, loginActionCreators } from '../../redux';
import { popOverActionCreators } from '../../redux';

import PopOver from './pop-over.component';

const mapStateToProps = state => {
  const { fullName } = state.ui.app;

  return {
    fullName
  };
};

const mapDispatchToProps = dispatch => {
  return {
    // loginActions: bindActionCreators(loginActionCreators, dispatch),
    popOverActions: bindActionCreators(popOverActionCreators, dispatch)
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(PopOver);
