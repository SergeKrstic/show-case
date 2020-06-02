import React from 'react';

import useStyles from './add-cover.styles';

export default function AddCover() {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      <input
        type="text"
        value=""
        placeholder="Search Unsplash for covers"
        autoFocus
      />
      <label>Suggested searches</label>
      <div>
        <button>Productivity</button>
        <button>Perspective</button>
        <button>Organization</button>
        <button>Colourful</button>
        <button>Nature</button>
        <button>Business</button>
        <button>Minimal</button>
        <button>Space</button>
        <button>Animals</button>
      </div>
      <label>Upload</label>
      <button className={classes.uploadButton}>Upload a Cover Image</button>
    </div>
  );
}
