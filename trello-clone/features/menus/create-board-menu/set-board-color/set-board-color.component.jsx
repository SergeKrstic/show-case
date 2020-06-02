import React from 'react';

import useStyles from './set-board-color.styles';

import { boardColors } from '../common.styles';

export default function CopyCard() {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      <div className={classes.imageContainer}>
        {boardColors.map((color, index) => (
          <div
            key={index}
            className={classes.image}
            style={{ backgroundColor: color.value }}
          />
        ))}
      </div>
    </div>
  );
}
