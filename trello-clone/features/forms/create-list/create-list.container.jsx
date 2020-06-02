import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { formValueSelector } from 'redux-form';

import CreateList from './create-list.component';

import { boardViewActionCreators as actions } from '../../../redux';

const selector = formValueSelector('createListForm');

const mapStateToProps = state => {
  return {
    name: selector(state, 'name')
  };
};

function mapDispatchToProps(dispatch) {
  return {
    onFocus: bindActionCreators(actions.focusOnListForm, dispatch),
    onBlur: bindActionCreators(actions.blurOnListForm, dispatch),
    onClose: bindActionCreators(actions.closeCreateListForm, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(CreateList);
