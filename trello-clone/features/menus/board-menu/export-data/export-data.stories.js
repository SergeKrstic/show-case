import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ExportData from './export-data.component';

storiesOf(
  'Services|TrelloClone/components/menus/board-menu/panels/export-data',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ExportData />);
