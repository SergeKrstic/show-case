import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import DomainHeader from './domain-header.component';

const props = {
  domainName: 'Domain 1',
  iconName: 'domain'
};

storiesOf('Services|TrelloClone/components/domain-list/domain-header', module)
  .addDecorator(withMockStoreProvider)
  .add('grid', () => <DomainHeader mode="grid" {...props} />)
  .add('list', () => <DomainHeader mode="list" {...props} />);
