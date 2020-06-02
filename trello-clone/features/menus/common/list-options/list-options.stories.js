import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ListOptions from './list-options.component';

const props = {
  options: [
    { name: 'Option 1', isCurrent: false },
    { name: 'Option 2', isCurrent: false },
    { name: 'Option 3', isCurrent: true },
    { name: 'Option 4', isCurrent: false }
  ]
};

storiesOf(
  'Services|TrelloClone/components/menus/list-menu/panels/list-options',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ListOptions {...props} />);
