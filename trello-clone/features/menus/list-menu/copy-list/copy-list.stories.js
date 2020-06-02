import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import CopyList from './copy-list.component';

storiesOf(
  'Services|TrelloClone/components/menus/list-menu/panels/copy-list',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CopyList />);
