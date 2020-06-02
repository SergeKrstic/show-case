import React from 'react';
import PropTypes from 'prop-types';

import { Droppable } from 'react-beautiful-dnd';

// import CardList, { getRenderCard } from './card-list.component';
import CardList from './card-list.component';
import useCardListStyles from './card-list.styles';

const CardListDroppable = ({ id, board, list, ...rest }) => {
  const classes = useCardListStyles();

  // const renderCard = getRenderCard(board, list.cardIds);

  return (
    // <Droppable droppableId={id} type="card" renderClone={renderCard}>
    <Droppable droppableId={id} type="card">
      {provided => (
        <div
          id={id}
          className={classes.cardList}
          ref={provided.innerRef}
          {...provided.droppableProps}
        >
          <CardList id={id} board={board} list={list} {...rest} />
          {provided.placeholder}
        </div>
      )}
    </Droppable>
  );
};

CardListDroppable.propTypes = {
  id: PropTypes.string.isRequired,
  ...CardList.propTypes
};

export default CardListDroppable;
