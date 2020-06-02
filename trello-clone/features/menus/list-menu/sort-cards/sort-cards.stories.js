import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import SortCards from './sort-cards.component';

storiesOf(
  'Services|TrelloClone/components/menus/list-menu/panels/sort-cards',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <SortCards />);
