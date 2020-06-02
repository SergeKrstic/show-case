import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import CreateBoard from './create-board.component';

storiesOf(
  'Services|TrelloClone/components/menus/create-board-menu/panels/create-board',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CreateBoard />);
