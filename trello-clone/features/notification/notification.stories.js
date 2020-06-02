import React from 'react';

import { storiesOf } from '@storybook/react';

import Notification from './notification.component';

storiesOf('Services|TrelloClone/components/notification', module)
  .add('single message', () => (
    <Notification errorMessages={['Board 1 not found']} />
  ))
  .add('multiples messages', () => (
    <Notification
      errorMessages={[
        'Board 1 not found',
        'Board 2 not found',
        'Board 3 not found'
      ]}
    />
  ))
  .add('long messages', () => (
    <Notification
      errorMessages={[
        'This is a very long message that shows how the notification item is displayed',
        'A short message'
      ]}
    />
  ));
