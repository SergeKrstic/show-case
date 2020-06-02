import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ArchivedItems from './archived-items.component';

storiesOf(
  'Services|TrelloClone/components/menus/board-menu/panels/archived-items',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ArchivedItems />);
