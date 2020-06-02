import React from 'react';

import ListOptions from '../../common/list-options/list-options.component';

const lists = [
  { type: 'menuItem', name: 'Date Created (Newest First)' },
  { type: 'menuItem', name: 'Date Created (Oldest First)' },
  { type: 'menuItem', name: 'Card Name (Alphabetically)' }
];

export default function SortCards() {
  return <ListOptions options={lists} />;
}
