import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ArchiveAllCards from './archive-all-cards.component';

storiesOf(
  'Services|TrelloClone/components/menus/list-menu/panels/archive-all-cards',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ArchiveAllCards />);
