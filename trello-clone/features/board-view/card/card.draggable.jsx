import React from 'react';
import PropTypes from 'prop-types';
import { Draggable } from 'react-beautiful-dnd';

import Card from './card.component';

const CardDraggable = ({ index, card, ...rest }) => {
  if (!card) return null;
  return (
    <Draggable draggableId={card.id} index={index}>
      {provided => (
        <Card
          card={card}
          innerRef={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          {...rest}
          // style={{ cursor: 'pointer' }}
        />
      )}
    </Draggable>
  );
};

CardDraggable.propTypes = {
  id: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  ...Card.propTypes
};

CardDraggable.defaultProps = {
  ...Card.defaultProps
};

export default CardDraggable;
