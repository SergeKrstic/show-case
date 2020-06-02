import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ChangeLabel from './change-label.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/change-label',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ChangeLabel />);
