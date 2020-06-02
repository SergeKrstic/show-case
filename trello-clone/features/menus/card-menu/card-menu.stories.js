import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import MenuHelper from '../common/menu-helper.component';
import CardMenu from './card-menu.component';

storiesOf('Services|TrelloClone/components/menus/card-menu', module)
  .addDecorator(withMockStoreProvider)
  .add('menu', () => (
    <MenuHelper buttonName="Open Card Menu" menuComponent={CardMenu} />
  ));
