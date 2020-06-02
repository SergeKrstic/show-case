import React from 'react';

import Dropdown from '../../common/dropdown/dropdown.component';

import useStyles from './move-list.styles';

const domains = [
  {
    name: 'Domain 1',
    id: 'domain-1',
    items: [
      { name: 'Project 1', id: 'board-1', isCurrent: false },
      { name: 'Project 2', id: 'board-2', isCurrent: false },
      { name: 'Project 3', id: 'board-3', isCurrent: false }
    ]
  },
  {
    name: 'Domain 2',
    id: 'domain-2',
    items: [
      { name: 'Project 4', id: 'board-4', isCurrent: true },
      { name: 'Project 5', id: 'board-5', isCurrent: false }
    ]
  },
  {
    name: 'Domain 3',
    id: 'domain-3',
    items: [{ name: 'Project 6', id: 'board-6', isCurrent: false }]
  }
];

const lists = [
  { id: 'list-1', name: 'Inbox', isCurrent: false },
  { id: 'list-2', name: 'Labels', isCurrent: false },
  { id: 'list-3', name: 'Outcomes', isCurrent: false },
  { id: 'list-4', name: 'Could', isCurrent: false },
  { id: 'list-5', name: 'Should', isCurrent: false },
  { id: 'list-6', name: 'Must', isCurrent: true },
  { id: 'list-7', name: 'Next', isCurrent: false },
  { id: 'list-8', name: 'Doing', isCurrent: false },
  { id: 'list-9', name: 'Today', isCurrent: false },
  { id: 'list-10', name: 'Done', isCurrent: false },
  { id: 'list-11', name: '+ Retrospective', isCurrent: false },
  { id: 'list-12', name: 'Discarded', isCurrent: false }
];

export default function ListMenu() {
  const classes = useStyles();
  return (
    <div className={classes.content}>
      <form>
        <Dropdown options={domains} labelName="Board" isGrouped />
        <Dropdown options={lists} labelName="Position" />
        <input type="submit" value="Move" />
      </form>
    </div>
  );
}
