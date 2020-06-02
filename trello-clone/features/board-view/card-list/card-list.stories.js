import React from 'react';
import { storiesOf } from '@storybook/react';
import { DragDropContext, Droppable } from 'react-beautiful-dnd';

import { withBaseStyles } from '../board-view.styles';
import { withMockStoreProvider } from '../../../utils/provider.utils';

import CardList from './card-list.component';
import CardListDroppable from './card-list.droppable';

export const cardListData = {
  cards: [
    {
      index: 0,
      id: 'card-01',
      name: 'Card 1',
      boardId: 'board-01',
      boardName: 'Board 1'
    },
    {
      index: 1,
      id: 'card-02',
      name: 'Card 2',
      boardId: 'board-01',
      boardName: 'Board 1'
    },
    {
      index: 2,
      id: 'card-03',
      name: 'Card 3',
      boardId: 'board-02',
      boardName: 'Board 2'
    },
    {
      index: 3,
      id: 'card-04',
      name:
        'A card really long text to test if the overflow hidden is working correctly',
      boardId: 'board-01',
      boardName: 'Board 1'
    }
  ],
  id: '0',
  index: 0,
  board: { id: 'board-01', name: 'Board 1' },
  list: {
    id: 'list-1',
    name: 'list 1',
    boardId: 'TEST_BOARD_ID',
    cardIds: ['card-1', 'card-2', 'card-3', 'card-4']
  },
  createCardFormIndexToOpen: 0,
  isCreateCardFormOpen: false,
  boardViewActions: {},
  modelsActions: {}
};

storiesOf('Services|TrelloClone/components/board-view/card-list', module)
  .addDecorator(withBaseStyles)
  .addDecorator(withMockStoreProvider)
  .add('default', () => (
    <DragDropContext>
      <Droppable droppableId="droppable">
        {provided => (
          <div {...provided.droppableProps} ref={provided.innerRef}>
            <CardList {...cardListData} />
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  ))
  .add('droppable', () => (
    <DragDropContext>
      <CardListDroppable id="card-list-01" {...cardListData} />
    </DragDropContext>
  ))
  .add('with create card open', () => (
    <DragDropContext>
      <CardListDroppable
        id="card-list-01"
        {...cardListData}
        isCreateCardFormOpen
      />
    </DragDropContext>
  ));
