import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import AddAttachment from './add-attachment.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/add-attachment',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <AddAttachment />);
