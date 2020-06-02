import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import AddChecklist from './add-checklist.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/add-checklist',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <AddChecklist />);
