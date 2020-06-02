import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import CopyBoard from './copy-board.component';

storiesOf(
  'Services|TrelloClone/components/menus/board-menu/panels/copy-board',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CopyBoard />);
