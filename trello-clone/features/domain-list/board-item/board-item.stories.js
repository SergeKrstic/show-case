import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import BoardItem from './board-item.component';

const board = {
  boardName: 'Board 1',
  domainName: 'Domain 1',
  isStarred: false,
  openBoard: () => {},
  toggleBoardStar: () => {}
};

const boardWithStar = {
  ...board,
  isStarred: true,
  isStarIconVisible: true
};

const boardWithDomainName = {
  ...board,
  isDomainNameVisible: true
};

const boardWithAll = {
  ...boardWithStar,
  isDomainNameVisible: true
};

const boardPlaceholder = {
  ...board,
  isPlaceHolder: true,
  placeHolderText: 'placeholder text'
};

storiesOf('Services|TrelloClone/components/domain-list/board-item', module)
  .addDecorator(withMockStoreProvider)
  // Grid
  .add('Grid: item', () => <BoardItem mode="grid" {...board} />)
  .add('Grid: item with star', () => (
    <BoardItem mode="grid" {...boardWithStar} />
  ))
  .add('Grid: item with domain', () => (
    <BoardItem mode="grid" {...boardWithDomainName} />
  ))
  .add('Grid: item with all adornments', () => (
    <BoardItem mode="grid" {...boardWithAll} />
  ))
  .add('Grid: item as placeholder', () => (
    <BoardItem mode="grid" {...boardPlaceholder} />
  ))
  // List
  .add('List: item', () => <BoardItem mode="list" {...board} />)
  .add('List: item with star', () => (
    <BoardItem mode="list" {...boardWithStar} />
  ))
  .add('List: item with domain', () => (
    <BoardItem mode="list" {...boardWithDomainName} />
  ))
  .add('List: item with all adornments', () => (
    <BoardItem mode="list" {...boardWithAll} />
  ));
