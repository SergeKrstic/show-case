import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ChangeSettings from './change-settings.component';

storiesOf(
  'Services|TrelloClone/components/menus/board-menu/panels/change-settings',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ChangeSettings />);
