import React from 'react';
import Grid from '@material-ui/core/Grid';
import Dropdown from '../../common/dropdown/dropdown.component';

import useStyles from './move-card.styles';

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

const cards = [
  { id: 'card-1', name: '1', isCurrent: false },
  { id: 'card-2', name: '2', isCurrent: false },
  { id: 'card-3', name: '3', isCurrent: false },
  { id: 'card-4', name: '4', isCurrent: false },
  { id: 'card-5', name: '5', isCurrent: false },
  { id: 'card-6', name: '6', isCurrent: true },
  { id: 'card-7', name: '7', isCurrent: false },
  { id: 'card-8', name: '8', isCurrent: false }
];

export default function MoveCard() {
  const classes = useStyles();
  return (
    <div className={classes.content}>
      <form>
        <label>Select Destination</label>
        <Dropdown options={domains} labelName="Board" isGrouped />
        <Grid container spacing={1}>
          <Grid item xs={9}>
            <Dropdown options={lists} labelName="List" />
          </Grid>
          <Grid item xs={3}>
            <Dropdown options={cards} labelName="Position" />
          </Grid>
        </Grid>
        <input type="submit" value="Move" />
      </form>
    </div>
  );
}
