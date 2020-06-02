import React from 'react';

import { withMockStoreProvider } from '../../utils/provider.utils';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import BaseDialog from './base-dialog.component';
import NotesIcon from '@material-ui/icons/Subject';

const props = {
  isOpen: true,
  title: 'Dialog Title',
  subtitle: 'subtitle goes here',
  icon: <NotesIcon />,
  children: <div>some dialog content</div>,
  handleClose: action('handleClose')
};

storiesOf('Services|TrelloClone/components/dialogs/base-dialog', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <BaseDialog {...props} />);
