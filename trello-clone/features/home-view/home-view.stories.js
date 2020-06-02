import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../utils/provider.utils';

import HomeView from './home-view.component';

const props = {
  domains: [
    { name: 'Domain 1' },
    { name: 'Domain 2 (with a really long title)' }
  ],
  boards: [
    {
      id: 'board-98',
      name: 'Today',
      domainName: '',
      isStarred: false
    },
    {
      id: 'board-99',
      name: 'Next',
      domainName: '',
      isStarred: false
    },
    {
      id: 'board-1',
      name: 'Board 1',
      domainName: 'Domain 1',
      isStarred: true
    },
    {
      id: 'board-2',
      name:
        'Board 2 (with a really long title to test that it clips properly and still looks good)',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-3',
      name: 'Board 3',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-4',
      name:
        'Board 4 (with a really long title to test that it clips properly and still looks good)',
      domainName: 'Domain 1',
      isStarred: true
    },
    {
      id: 'board-5',
      name: 'Board 5',
      domainName: 'Domain 2 (with a really long title)',
      isStarred: true
    },
    {
      id: 'board-6',
      name: 'Board 6',
      domainName: 'Domain 2 (with a really long title)',
      isStarred: false
    },
    {
      id: 'board-7',
      name: 'Board 7',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-8',
      name: 'Board 8',
      domainName: 'Domain 1',
      isStarred: false
    }
  ]
};

storiesOf('Services|TrelloClone/components/home-view', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <HomeView {...props} />);
