import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import CardView from './card-view.component';

import { selectCardById } from '../../redux/entities/cards/cards.selectors';
import { modelsActionCreators, cardViewActionCreators } from '../../redux';

const mapStateToProps = state => {
  const { cardView } = state.views;

  return {
    card: selectCardById(state, cardView.openCardId),
    isOpen: cardView.isCardViewOpen
  };
};

const mapDispatchToProps = dispatch => {
  return {
    modelsActions: bindActionCreators(modelsActionCreators, dispatch),
    cardViewActions: bindActionCreators(cardViewActionCreators, dispatch)
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(CardView);
