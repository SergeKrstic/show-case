import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ChangeDescription from './change-description.component';

storiesOf(
  'Services|TrelloClone/components/menus/board-menu/panels/change-description',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ChangeDescription />);
