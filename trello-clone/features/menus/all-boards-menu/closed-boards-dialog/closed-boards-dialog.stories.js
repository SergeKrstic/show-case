import React from 'react';

import { storiesOf } from '@storybook/react';
import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ClosedBoardsDialog from './closed-boards-dialog.component';

storiesOf(
  'Services|TrelloClone/components/menus/all-boards-menu/closed-boards-dialog',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ClosedBoardsDialog isOpen={true} />);
