import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import MoveList from './move-list.component';

storiesOf(
  'Services|TrelloClone/components/menus/list-menu/panels/move-list',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <MoveList />);
