import React from 'react';

import ListOptions from '../../common/list-options/list-options.component';

const lists = [
  { type: 'menuItem', name: 'Inbox', isCurrent: false },
  { type: 'menuItem', name: 'Labels', isCurrent: false },
  { type: 'menuItem', name: 'Outcomes', isCurrent: false },
  { type: 'menuItem', name: 'Could', isCurrent: false },
  { type: 'menuItem', name: 'Should', isCurrent: false },
  { type: 'menuItem', name: 'Must', isCurrent: true },
  { type: 'menuItem', name: 'Next', isCurrent: false },
  { type: 'menuItem', name: 'Doing', isCurrent: false },
  { type: 'menuItem', name: 'Today', isCurrent: false },
  { type: 'menuItem', name: 'Done', isCurrent: false },
  { type: 'menuItem', name: '+ Retrospective', isCurrent: false },
  { type: 'menuItem', name: 'Discarded', isCurrent: false }
];

export default function SortCards() {
  return <ListOptions options={lists} />;
}
