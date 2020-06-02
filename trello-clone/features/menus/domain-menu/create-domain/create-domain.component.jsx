import React from 'react';

import useStyles from './create-domain.styles';

const CreateDomain = () => {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      <label>Name</label>
      <input type="text" value="" maxLength={100}></input>
      <button>Create</button>
    </div>
  );
};

export default CreateDomain;
