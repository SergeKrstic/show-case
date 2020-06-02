import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import { selectCardById } from '../../../redux/entities/cards/cards.selectors';
import { selectCurrentBoardId } from '../../../redux/views/board-view/board-view.selectors';

import CardDraggable from './card.draggable';

import {
  cardViewActionCreators,
  boardViewActionCreators
} from '../../../redux';

const filterCard = (state, props) => {
  const { searchTerm } = state.views.boardView;
  const card = selectCardById(state, props.id);
  return card
    ? card.name.toLowerCase().includes(searchTerm.toLowerCase())
      ? card
      : null
    : null;
};

const mapStateToProp = (state, props) => {
  return {
    card: filterCard(state, props),
    currentBoardId: selectCurrentBoardId(state)
  };
};

const mapDispatchToProps = dispatch => {
  return {
    boardViewActions: bindActionCreators(boardViewActionCreators, dispatch),
    cardViewActions: bindActionCreators(cardViewActionCreators, dispatch)
  };
};

export default connect(mapStateToProp, mapDispatchToProps)(CardDraggable);
