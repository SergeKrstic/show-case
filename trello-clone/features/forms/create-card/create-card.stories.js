import React from 'react';
import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import CreateCard from './create-card.component';
import CreateCardContainer from './create-card.container';

const props = {
  onFocus: action('onfocus'),
  onBlur: action('onBlur'),
  onClose: action('onClose'),
  onSubmit: action('onSubmit')
};

const styles = {
  border: '1px solid #888',
  width: '300px'
};

storiesOf('Services|TrelloClone/components/forms/create-card', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => (
    <div style={styles}>
      <CreateCard {...props} />
    </div>
  ))
  .add('container', () => (
    <div style={styles}>
      <CreateCardContainer onSubmit={action('onSubmit')} />
    </div>
  ));
