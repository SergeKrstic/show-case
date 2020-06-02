import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import EditLabels from './edit-labels.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/edit-labels',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <EditLabels />);
