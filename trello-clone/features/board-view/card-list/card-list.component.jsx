import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { animateScroll } from 'react-scroll';

import CreateCard from '../../forms/create-card/create-card.container';
import Card from '../card/card.container';

// export const getRenderCard = (cardIds) => (
//   provided,
//   snapshot,
//   rubric
// ) => {
//   const index = rubric.source.index;
//   const cardId = cardIds[index];
//   return (
//     <CardComponent
//       index={index}
//       key={cardId}
//       id={cardId}
//       innerRef={provided.innerRef}
//       {...provided.draggableProps}
//       {...provided.dragHandleProps}
//     />
//   );
// };

const CardList = ({
  id,
  index,
  board,
  list,
  createCardFormIndexToOpen,
  isCreateCardFormOpen,
  boardViewActions,
  modelsActions
}) => {
  useEffect(() => {
    if (isCreateCardFormOpen && createCardFormIndexToOpen === index) {
      // ensure CreateCard component is visible by scrolling to the bottom
      animateScroll.scrollToBottom({ containerId: id, duration: 0 });
    }
  }, [isCreateCardFormOpen, createCardFormIndexToOpen, index, id]);

  const renderCreateCard = () => {
    if (isCreateCardFormOpen && createCardFormIndexToOpen === index) {
      // boardViewActions.updateCreateCardForm({list.id, cardName: ''});
      return <CreateCard listId={list.id} onSubmit={handleCreateCard} />;
    }
  };

  const handleCreateCard = formInput => {
    const cardNames = formInput.name.split('\n');

    let createMultipleCards = false;
    let numberOfCardsToCreate = cardNames.reduce((count, cardName) => {
      return cardName.trim().length ? count + 1 : count;
    }, 0);
    if (cardNames.length > 1) {
      createMultipleCards = window.confirm(
        `If you want, we can create a card for every new line (${numberOfCardsToCreate}). ` +
          `You can also create one card with a long title.\n\n` +
          `Create ${numberOfCardsToCreate} cards?`
      );
    }

    if (createMultipleCards) {
      cardNames.forEach(cardName => {
        createCard(cardName.trim());
      });
    } else {
      createCard(formInput.name.trim());
    }
  };

  const createCard = cardName => {
    if (!cardName.length) return;

    modelsActions.addCard({
      name: cardName,
      description: '',
      isClosed: false,
      boardName: board.name,
      boardId: board.id,
      listId: list.id
    });
  };

  return (
    <>
      {list.cardIds.map((cardId, index) => (
        <Card index={index} key={cardId} id={cardId} />
      ))}
      {renderCreateCard()}
    </>
  );
};

CardList.propTypes = {
  id: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  board: PropTypes.object.isRequired,
  list: PropTypes.object.isRequired,
  createCardFormIndexToOpen: PropTypes.number.isRequired,
  isCreateCardFormOpen: PropTypes.bool.isRequired,
  boardViewActions: PropTypes.object.isRequired,
  modelsActions: PropTypes.object.isRequired
};

export default React.memo(CardList);
