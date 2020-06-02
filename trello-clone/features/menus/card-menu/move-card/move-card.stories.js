import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import MoveCard from './move-card.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/move-card',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <MoveCard />);
