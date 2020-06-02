import React from 'react';
import { storiesOf } from '@storybook/react';
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

import { withBaseStyles } from '../board-view.styles';
import { withMockStoreProvider } from '../../../utils/provider.utils';

import Card from './card.component';
import CardDraggable from './card.draggable';
import { action } from '@storybook/addon-actions';

const card = { id: 'card-01', name: 'Card name', boardName: 'Board 1' };
const cardWithLongName = {
  ...card,
  name:
    'A card really long text to test if the overflow hidden is working correctly'
};
const cardWithDescription = {
  ...card,
  description: 'A simple card description...'
};
const cardWithLabel = {
  ...card,
  labels: [{ name: 'label 1', color: 'green' }]
};
const cardWithTwoLabels = {
  ...card,
  labels: [
    { name: 'label 1', color: 'green' },
    { name: 'label 2', color: 'pink' }
  ]
};
const cardWithAllLabels = {
  ...card,
  labels: [
    // { name: 'green', color: 'green' },
    // { name: 'yellow', color: 'yellow' },
    { name: 'orange', color: 'orange' },
    { name: 'red', color: 'red' },
    { name: 'blue', color: 'blue' },
    { name: 'sky', color: 'sky' },
    { name: 'lime', color: 'lime' },
    { name: 'pink', color: 'pink' },
    { name: 'black', color: 'black' }
  ]
};
const cardWithEverything = {
  ...cardWithAllLabels,
  description: 'A simple card description...'
};

const props = {
  card: card,
  boardViewActions: {
    updateCard: action('updateCard'),
    setActiveCard: action('setActiveCard')
  },
  cardViewActions: {
    openCardView: action('openCardView')
  }
};

storiesOf('Services|TrelloClone/components/board-view/card', module)
  .addDecorator(withBaseStyles)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <Card {...props} />)
  .add('with long text', () => <Card {...props} card={cardWithLongName} />)
  .add('with description badge', () => (
    <Card {...props} card={cardWithDescription} />
  ))
  .add('with header', () => <Card {...props} isHeaderVisible />)
  .add('with label', () => <Card {...props} card={cardWithLabel} />)
  .add('with two labels', () => <Card {...props} card={cardWithTwoLabels} />)
  .add('with all labels', () => <Card {...props} card={cardWithAllLabels} />)
  .add('with header and label', () => (
    <Card {...props} card={cardWithLabel} isHeaderVisible />
  ))
  .add('with header, all labels and badges', () => (
    <Card {...props} card={cardWithEverything} isHeaderVisible />
  ))
  .add('draggable', () => (
    <DragDropContext>
      <Droppable droppableId="droppable">
        {provided => (
          <div {...provided.droppableProps} ref={provided.innerRef}>
            <CardDraggable id={'item1'} index={0} {...props} />
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  ))
  .add('draggable with header', () => (
    <DragDropContext>
      <Droppable droppableId="droppable">
        {provided => (
          <div {...provided.droppableProps} ref={provided.innerRef}>
            <CardDraggable id={'item1'} index={0} {...props} isHeaderVisible />
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  ));
