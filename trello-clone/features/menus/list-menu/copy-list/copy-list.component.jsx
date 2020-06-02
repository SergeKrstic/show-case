import React from 'react';

import useStyles from './copy-list.styles';

export default function ListMenu() {
  const classes = useStyles();
  const handleFocus = event => event.target.select();

  return (
    <div className={classes.content}>
      <form>
        <label>Name</label>
        <textarea
          name="name"
          value="List Name"
          autoFocus
          spellCheck={false}
          onFocus={handleFocus}
          onChange={() => {}}
        />
        <input type="submit" value="Create List" />
      </form>
    </div>
  );
}
