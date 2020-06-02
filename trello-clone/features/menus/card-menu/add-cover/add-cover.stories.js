import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import AddCover from './add-cover.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/add-cover',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <AddCover />);
