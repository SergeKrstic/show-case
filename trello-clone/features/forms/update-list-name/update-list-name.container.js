import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import UpdateListName from './update-list-name.component';

import { boardViewActionCreators as actions } from '../../../redux';

function mapDispatchToProps(dispatch) {
  return {
    onFocus: bindActionCreators(actions.focusOnUpdateListNameForm, dispatch),
    onBlur: bindActionCreators(actions.blurOnUpdateListNameForm, dispatch)
  };
}

export default connect(null, mapDispatchToProps)(UpdateListName);
