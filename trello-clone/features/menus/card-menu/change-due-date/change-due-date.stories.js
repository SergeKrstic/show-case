import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ChangeDueDate from './change-due-date.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/change-due-date',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ChangeDueDate />);
