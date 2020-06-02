import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { formValueSelector } from 'redux-form';

import CreateCard from './create-card.component';

import { boardViewActionCreators as actions } from '../../../redux';
// import { getCreateCardFormName } from '../../../redux/ui/board-view/board-view.selectors';

const selector = formValueSelector('createCardForm');

const mapStateToProps = state => {
  return {
    name: selector(state, 'name')
    // cardName: getCreateCardFormName(state)
  };
};

function mapDispatchToProps(dispatch) {
  return {
    onFocus: bindActionCreators(actions.focusOnCardForm, dispatch),
    onBlur: bindActionCreators(actions.blurOnCardForm, dispatch),
    // onChange: bindActionCreators(actions.updateCreateCardForm, dispatch),
    onClose: bindActionCreators(actions.closeCreateCardForm, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(CreateCard);
