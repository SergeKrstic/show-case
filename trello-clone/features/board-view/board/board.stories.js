import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../utils/provider.utils';
import { withBaseStyles } from '../board-view.styles';

import Board from './board.component';
import BoardContainer from './board.container';

import { TEST_BOARD_ID } from '../../../utils/constants';

const boardData = {
  board: {
    id: TEST_BOARD_ID,
    name: 'Project 1',
    description: '',
    domainId: 'domain-1',
    domainName: 'Domain 1',
    isClosed: false,
    isStarred: true,
    listIds: ['list-1', 'list-2', 'list-3']
  }
};

const actions = {
  isCreateListFormOpen: false,
  modelsActions: {
    addList: action('addList'),
    moveList: action('moveList'),
    moveCard: action('moveCard')
  },
  boardViewActions: {
    openCreateListForm: action('openCreateListForm'),
    openCreateCardForm: action('openCreateCardForm')
  }
};

storiesOf('Services|TrelloClone/components/board-view/board', module)
  .addDecorator(withBaseStyles)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <Board {...boardData} {...actions} />)
  .add('with add list open', () => (
    <Board {...boardData} {...actions} isCreateListFormOpen />
  ))
  .add('container', () => <BoardContainer />);
