import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import Toolbar from './toolbar.component';

const props = {
  boards: [
    { id: 'board-01', name: 'Today' },
    { id: 'board-02', name: 'Next' },
    { id: 'board-03', name: 'Board 1', isStarred: true },
    { id: 'board-04', name: 'Board 2', isStarred: false },
    { id: 'board-05', name: 'Board 3', isStarred: true }
  ]
};

storiesOf('Services|TrelloClone/components/board-view/toolbar', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <Toolbar {...props} />);
