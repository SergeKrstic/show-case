import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../utils/provider.utils';

import DomainList from './domain-list.component';
import DomainListContainer from './domain-list.container';

const props = {
  domains: [
    {
      id: 'domain-00',
      name: 'Focus'
    },
    {
      id: 'domain-01',
      name: 'Domain 1'
    },
    {
      id: 'domain-02',
      name: 'Domain 2'
    }
  ],
  boards: [
    {
      id: 'board-today',
      name: 'Today',
      domainId: 'domain-00',
      domainName: 'Focus',
      isStarred: false
    },
    {
      id: 'board-next',
      name: 'Next',
      domainId: 'domain-00',
      domainName: 'Focus',
      isStarred: false
    },
    {
      id: 'board-1',
      name: 'Board 1',
      domainId: 'domain-01',
      domainName: 'Domain 1',
      isStarred: true
    },
    {
      id: 'board-2',
      name: 'Board 2',
      domainId: 'domain-01',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-3',
      name: 'Board 3',
      domainId: 'domain-01',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-4',
      name: 'Board 4',
      domainId: 'domain-01',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-5',
      name: 'Board 5',
      domainId: 'domain-01',
      domainName: 'Domain 1',
      isStarred: false
    },
    {
      id: 'board-6',
      name: 'Board 6',
      domainId: 'domain-01',
      domainName: 'Domain 1',
      isStarred: true
    },
    {
      id: 'board-7',
      name: 'Board 7',
      domainId: 'domain-02',
      domainName: 'Domain 2',
      isStarred: true
    },
    {
      id: 'board-8',
      name: 'Board 8',
      domainId: 'domain-02',
      domainName: 'Domain 2',
      isStarred: false
    },
    {
      id: 'board-9',
      name: 'Board 9',
      domainId: 'domain-02',
      domainName: 'Domain 2',
      isStarred: false
    }
  ]
};

storiesOf('Services|TrelloClone/components/domain-list/view', module)
  .addDecorator(withMockStoreProvider)
  .add('grid', () => <DomainList mode="grid" {...props} />)
  .add('list', () => <DomainList mode="list" {...props} />)
  .add('container: grid', () => <DomainListContainer mode="grid" />)
  .add('container: list', () => <DomainListContainer mode="list" />);
