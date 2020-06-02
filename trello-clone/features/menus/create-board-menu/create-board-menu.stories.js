import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import MenuHelper from '../common/menu-helper.component';
import CreateBoardMenu from './create-board-menu.component';

storiesOf('Services|TrelloClone/components/menus/create-board-menu', module)
  .addDecorator(withMockStoreProvider)
  .add('menu', () => (
    <MenuHelper
      buttonName="Open Create Board Menu"
      menuComponent={CreateBoardMenu}
    />
  ));
