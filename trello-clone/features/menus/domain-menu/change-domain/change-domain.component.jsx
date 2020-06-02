import React from 'react';

import useStyles from './change-domain.styles';

const ChangeDomain = () => {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      <label>This board is part of...</label>
      <select>
        <option>Domain 1</option>
        <option>Domain 2</option>
        <option>Domain 3</option>
      </select>
      <div>
        <button className={classes.changeButton}>Change</button>
        <button className={classes.createDomainButton}>Create Domain</button>
      </div>
    </div>
  );
};

export default ChangeDomain;
