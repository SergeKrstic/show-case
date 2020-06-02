import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import Domain from './domain.component';

const props = {
  iconName: 'domain',
  domainName: 'Domain 1',
  boards: [
    {
      id: 'board-1',
      name: 'Board 1',
      domainName: '',
      isStarred: true
    },
    {
      id: 'board-2',
      name: 'Board 2',
      domainName: 'Domain 1',
      isStarred: true
    },
    {
      id: 'board-3',
      name: 'Board 3',
      domainName: '',
      isStarred: false
    },
    {
      id: 'board-4',
      name: 'Board 4',
      domainName: '',
      isStarred: true
    },
    {
      id: 'board-5',
      name: 'Board 5',
      domainName: 'Domain 2',
      isStarred: false
    },
    {
      id: 'board-6',
      name: 'Board 6',
      domainName: 'Domain 2',
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
      domainName: 'Domain 2',
      isStarred: false
    }
  ]
};

storiesOf('Services|TrelloClone/components/domain-list/domain', module)
  .addDecorator(withMockStoreProvider)
  .add('grid', () => <Domain mode="grid" {...props} />)
  .add('list', () => <Domain mode="list" {...props} />);
