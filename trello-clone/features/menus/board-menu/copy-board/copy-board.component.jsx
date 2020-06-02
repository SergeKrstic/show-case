import React from 'react';

import useStyles from './copy-board.styles';

const CopyBoard = () => {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      <label>Title</label>
      <input type="text" value="" />
      <label>Domain</label>
      <select>
        <option>Domain 1</option>
        <option>Domain 2</option>
        <option>Domain 3</option>
        <option>Domain 4</option>
      </select>
      <div className={classes.checkbox}>
        <input type="checkbox" name="cards" checked={true} />
        <label>Keep Cards</label>
      </div>
      <button>Create</button>
    </div>
  );
};

export default CopyBoard;
