import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import SetBoardColor from './set-board-color.component';

storiesOf(
  'Services|TrelloClone/components/menus/create-board-menu/panels/set-board-color',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <SetBoardColor />);
