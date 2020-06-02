import React from 'react';
import { storiesOf } from '@storybook/react';
import { withMockStoreProvider } from '../../utils/provider.utils';

import Showdown from 'showdown';
import CardView from './card-view.component';
import { action } from '@storybook/addon-actions';

var defaultOptions = JSON.stringify(Showdown.getDefaultOptions(), undefined, 2);

const code = '```';

const initialText = `
### Icons

 - Glyhicon: @glyphicon-envelope (doesn't work)
 - FontAwesome: @fa-home

### XSS Filter

<script>alert('xss!')</script>

${code}
def maliciousFunction:
    <script>alert('xss!')</script>
${code}

### Emoji

:+1: :art: :balloon: :blush: :broken_heart: :clap: :cookie: :cry:
:fist_oncoming: :grinning: :headphones: :heart: :innocent: :joy:
:kissing_heart: :laughing: :monkey: :monkey_face: :ok_hand: :pencil2:
:shamrock: :sleeping: :sleeping_bed: :slightly_smiling_face: :smile:
:thinking: :turtle: :upside_down_face: :wink:

### Math

${code}asciimath
  g(x) = 3x^4 + 2x^2
${code}

### Code Highlighting

Doesn't work:
- showdown-pretty
- showdown-highlight

${code}
function sayHello (msg, who) {
    return \`\${who} says: msg\`;
}
sayHello("Hello World", "Johnny");
${code}

### Videos

- Default
  - ![youtube video](http://www.youtube.com/watch?v=dQw4w9WgXcQ)
- simple, assumes units are in px (=100x80)
  - ![foo](youtu.be/dQw4w9WgXcQ =100x80)
- sets the height to "auto" (=100x*)
  - ![bar](youtu.be/dQw4w9WgXcQ =100x*)
- width of 80% and height of 15em (=80%x15em)
  - ![baz](youtu.be/dQw4w9WgXcQ =80%x15em)

extends options:
- youtubeHeight
- youtubeWidth
- smoothLivePreview
- youtubeUseSimpleImg

### Showdown Default Options

${code}
  ${defaultOptions}
${code}
`;

export const CardData = {
  name: 'Card Name',
  description: initialText,
  listName: 'Inbox'
};

const props = {
  card: CardData,
  isOpen: true,
  cardViewActions: {
    hideCardView: action('hideCardView')
  }
};

storiesOf('Services|TrelloClone/components/card-view', module)
  .addDecorator(withMockStoreProvider)
  .add('with mock data', () => <CardView {...props} />);
