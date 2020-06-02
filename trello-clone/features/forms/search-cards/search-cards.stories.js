import React from 'react';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';

import { withMockStoreProvider } from '../../../utils/provider.utils';

import SearchCards from './search-cards.component';
import SearchCardsContainer from './search-cards.container';

const props = {
  onSearchTermChange: action('onSearchTermChange')
};

storiesOf('Services|TrelloClone/components/forms/search-cards', module)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <SearchCards {...props} />)
  .add('container', () => (
    <SearchCardsContainer onSubmit={action('onSubmit')} />
  ));
