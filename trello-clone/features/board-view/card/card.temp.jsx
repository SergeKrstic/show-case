import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import { selectCardById } from '../../../redux/entities/cards/cards.selectors';

import Card from './card.component';

import {
  cardViewActionCreators,
  boardViewActionCreators
} from '../../../redux';

const mapStateToProp = (state, props) => {
  return {
    card: selectCardById(state, props.id)
  };
};

const mapDispatchToProps = dispatch => {
  return {
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    cardViewActions: bindActionCreators(cardViewActionCreators, dispatch)
  };
};

export default connect(mapStateToProp, mapDispatchToProps)(Card);
