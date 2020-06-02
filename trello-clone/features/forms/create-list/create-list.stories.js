import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import CreateList from './create-list.component';
import CreateListContainer from './create-list.container';

const props = {
  onFocus: action('onfocus'),
  onBlur: action('onBlur'),
  onClose: action('onClose'),
  onSubmit: action('onSubmit')
};

storiesOf('Services|TrelloClone/components/forms/create-list', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <CreateList {...props} />)
  .add('container', () => (
    <CreateListContainer onSubmit={action('onSubmit')} />
  ));
