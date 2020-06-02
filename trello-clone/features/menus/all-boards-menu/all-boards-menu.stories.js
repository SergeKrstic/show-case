import React from 'react';

import Div100vh from 'react-div-100vh';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import AllBoardsMenu from './all-boards-menu.component';
import AllBoardsMenuContainer from './all-boards-menu.container';

const props = {
  boardsMenuActions: {
    saveUserInput: action('saveUserInput'),
    focusOnBoardsMenu: action('focusOnBoardsMenu'),
    blurOnBoardsMenu: action('blurOnBoardsMenu')
  }
};

storiesOf('Services|TrelloClone/components/menus/all-boards-menu', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => (
    <Div100vh>
      <AllBoardsMenu {...props} />
    </Div100vh>
  ))
  .add('container', () => (
    <Div100vh>
      <AllBoardsMenuContainer {...props} />
    </Div100vh>
  ));
