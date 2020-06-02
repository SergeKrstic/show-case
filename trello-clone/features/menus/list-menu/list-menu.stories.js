import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import MenuHelper from '../common/menu-helper.component';
import ListMenu from './list-menu.component';

storiesOf('Services|TrelloClone/components/menus/list-menu', module)
  .addDecorator(withMockStoreProvider)
  .add('menu', () => (
    <MenuHelper buttonName="Open List Menu" menuComponent={ListMenu} />
  ));
