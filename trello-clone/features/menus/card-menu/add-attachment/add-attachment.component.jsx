import React from 'react';

import ListOptions from '../../common/list-options/list-options.component';
import useStyles from './add-attachment.styles';

const options = [
  { type: 'menuItem', name: 'Computer' },
  { type: 'menuItem', name: 'Trello' },
  { type: 'menuItem', name: 'Google Drive' },
  { type: 'menuItem', name: 'Dropbox' },
  { type: 'menuItem', name: 'Box' },
  { type: 'menuItem', name: 'OneDrive' },
  { type: 'divider' }
];

export default function AddAttachment() {
  const classes = useStyles();

  return (
    <div className={classes.container}>
      <ListOptions options={options} />
      <div className={classes.content}>
        <label>Attach a link</label>
        <input type="text" value="" placeholder="Paste any link here..." />
        <button>Attach</button>
      </div>
    </div>
  );
}
