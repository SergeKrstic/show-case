import React from 'react';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from './utils/provider.utils';

import App from './app.component';
import AppContainer from './app.container';

import { TEST_USER_ID } from './utils/constants';

const props = {
  isHomeViewOpen: false,
  isCardViewOpen: false,
  isFocusOnBoardsMenu: false,
  isBoardsMenuOpen: true,
  isFocusOnPopOver: false,
  isPopOverOpen: false,
  isFocusOnModal: false,
  isModalOpen: false,
  errorMessages: [],
  boardsMenuActions: {
    hideBoardsMenu: action('hideBoardsMenu')
  },
  popOverActions: {
    hidePopOver: action('hidePopOver')
  },
  modalActions: {
    closeAllModals: action('closeAllModals')
  },
  appActions: {
    getUser: action('getUser')
  }
};

const user = {
  id: TEST_USER_ID,
  displayName: 'John Smith'
};

storiesOf('Services|TrelloClone/app', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <App {...props} />)
  .add('live container', () => <AppContainer user={user} />);
