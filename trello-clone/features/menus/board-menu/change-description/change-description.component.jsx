import React from 'react';

import useStyles from './change-description.styles';

export default function ListMenu() {
  const classes = useStyles();
  const handleFocus = event => event.target.select();

  return (
    <div className={classes.content}>
      <label>Name</label>
      <textarea
        name="name"
        value="Some description about the purpose of the board"
        autoFocus
        spellCheck={false}
        onFocus={handleFocus}
        onChange={() => {}}
      />
      <button>Save</button>
    </div>
  );
}
