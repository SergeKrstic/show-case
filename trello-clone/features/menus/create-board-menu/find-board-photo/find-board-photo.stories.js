import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import FindBoardPhoto from './find-board-photo.component';

storiesOf(
  'Services|TrelloClone/components/menus/create-board-menu/panels/find-board-photo',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <FindBoardPhoto />);
