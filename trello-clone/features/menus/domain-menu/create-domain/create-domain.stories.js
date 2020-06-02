import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import CreateDomain from './create-domain.component';

storiesOf(
  'Services|TrelloClone/components/menus/domain-menu/panels/create-domain',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CreateDomain />);
