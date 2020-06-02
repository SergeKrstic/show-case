import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import CloseBoard from './close-board.component';

storiesOf(
  'Services|TrelloClone/components/menus/board-menu/panels/close-board',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CloseBoard />);
