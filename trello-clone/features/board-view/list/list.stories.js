import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { DragDropContext, Droppable } from 'react-beautiful-dnd';

import { withBaseStyles } from '../board-view.styles';
import { withMockStoreProvider } from '../../../utils/provider.utils';

import List from './list.component';
import ListDraggable from './list.draggable';

import { cardListData } from '../card-list/card-list.stories';

const props = {
  board: { id: 'board-01', name: 'Board 1' },
  list: {
    id: 'list-1',
    name: 'list 1',
    boardId: 'TEST_BOARD_ID',
    cardIds: ['card-1', 'card-2', 'card-3', 'card-4']
  },
  cards: cardListData.cards,
  index: 0,
  isUpdateListNameFormOpen: false,
  updateListNameFormIndexToOpen: -1,
  isCreateCardFormOpen: false,
  createCardFormIndexToOpen: -1,
  boardViewActions: {
    openUpdateBoardNameForm: action('openUpdateBoardNameForm'),
    openCreateCardForm: action('openCreateCardForm')
  },
  modelsActions: {
    addCard: action('addCard')
  }
};

storiesOf('Services|TrelloClone/components/board-view/list', module)
  .addDecorator(withBaseStyles)
  .addDecorator(withMockStoreProvider)
  .add('default', () => (
    <DragDropContext>
      <List {...props} />
    </DragDropContext>
  ))
  .add('with add card form open', () => (
    <DragDropContext>
      <List {...props} isCreateCardFormOpen createCardFormIndexToOpen={0} />
    </DragDropContext>
  ))
  .add('with update list name form open', () => (
    <DragDropContext>
      <List {...props} isEditingListName />
    </DragDropContext>
  ))
  .add('draggable', () => (
    <DragDropContext>
      <Droppable droppableId="droppable" type="list">
        {provided => (
          <div {...provided.droppableProps} ref={provided.innerRef}>
            <ListDraggable index={0} {...props} />
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </DragDropContext>
  ));
