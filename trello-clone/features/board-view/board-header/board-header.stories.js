import React from 'react';
import { storiesOf } from '@storybook/react';

import { withBaseStyles } from '../board-view.styles';
import { withMockStoreProvider } from '../../../utils/provider.utils';

import BoardHeader from './board-header.component';

const board = {
  name: 'Board Title',
  domainName: '',
  isStarred: false
};

const boardWithStar = {
  ...board,
  isStarred: true
};

const boardWithAll = {
  ...boardWithStar,
  domainName: 'Domain 1'
};

storiesOf('Services|TrelloClone/components/board-view/board-header', module)
  .addDecorator(withBaseStyles)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <BoardHeader board={board} />)
  .add('is starred', () => <BoardHeader board={boardWithStar} />)
  .add('with domain', () => <BoardHeader board={boardWithAll} />);
