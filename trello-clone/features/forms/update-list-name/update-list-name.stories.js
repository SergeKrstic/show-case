import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import UpdateListName from './update-list-name.component';
import UpdateListNameContainer from './update-list-name.container';

const props = {
  initialValues: { name: 'Some text' },
  onFocus: action('onfocus'),
  onBlur: action('onBlur'),
  onSubmit: action('onSubmit')
};

storiesOf('Services|TrelloClone/components/forms/update-list-name', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <UpdateListName {...props} />)
  .add('container', () => (
    <UpdateListNameContainer onSubmit={action('onSubmit')} />
  ));
