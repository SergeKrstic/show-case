import React from 'react';

import { storiesOf } from '@storybook/react';

import { withMockStoreProvider } from '../../../../utils/provider.utils';

import ChangeDomain from './change-domain.component';

storiesOf(
  'Services|TrelloClone/components/menus/domain-menu/panels/change-domain',
  module
)
  .addDecorator(withMockStoreProvider)
  .add('default', () => <ChangeDomain />);
