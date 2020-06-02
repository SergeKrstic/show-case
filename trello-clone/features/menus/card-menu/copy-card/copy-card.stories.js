import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import CopyCard from './copy-card.component';

storiesOf(
  'Services|TrelloClone/components/menus/card-menu/panels/copy-card',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CopyCard />);
