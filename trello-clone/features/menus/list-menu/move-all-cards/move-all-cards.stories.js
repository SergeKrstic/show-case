import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import MoveAllCards from './move-all-cards.component';

storiesOf(
  'Services|TrelloClone/components/menus/list-menu/panels/move-all-cards',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <MoveAllCards />);
