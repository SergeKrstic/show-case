import React from 'react';

import useStyles from './add-checklist.styles';

export default function AddChecklist() {
  const classes = useStyles();
  const handleFocus = event => event.target.select();

  return (
    <div className={classes.content}>
      <label>Title</label>
      <input
        type="text"
        value="Checklist"
        autoFocus
        spellCheck={false}
        onFocus={handleFocus}
        onChange={() => {}}
      />
      <button>Add</button>
    </div>
  );
}
