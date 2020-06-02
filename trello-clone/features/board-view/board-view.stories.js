import React from 'react';
import { storiesOf } from '@storybook/react';

import { withBaseStyles } from './board-view.styles';
import { withMockStoreProvider } from '../../utils/provider.utils';

import BoardView from './board-view.component';
import BoardViewContainer from './board-view.container';

const props = {
  isFocusOnUpdateBoardNameForm: false,
  isUpdateBoardNameFormOpen: false,

  isFocusOnCreateListForm: false,
  isCreateListFormOpen: false,

  isFocusOnUpdateListNameForm: false,
  isUpdateListNameFormOpen: false,

  isFocusOnCreateCardForm: false,
  isCreateCardFormOpen: false
};

storiesOf('Services|TrelloClone/components/board-view/view', module)
  .addDecorator(withBaseStyles)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <BoardView {...props} />)
  .add('container', () => <BoardViewContainer />);
