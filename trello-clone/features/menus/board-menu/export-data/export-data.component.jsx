import React from 'react';

import ListOptions from '../../common/list-options/list-options.component';

const lists = [
  { type: 'menuItem', name: 'Export as CSV', isCurrent: false },
  { type: 'menuItem', name: 'Export as JSON', isCurrent: false }
];

export default function ExportData() {
  return <ListOptions options={lists} />;
}
