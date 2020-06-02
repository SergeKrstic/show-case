import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import MenuHelper from '../common/menu-helper.component';
import BoardMenu from './board-menu.component';

storiesOf('Services|TrelloClone/components/menus/board-menu', module)
  .addDecorator(withMockStoreProvider)
  .add('menu', () => (
    <MenuHelper buttonName="Open Board Menu" menuComponent={BoardMenu} />
  ));
