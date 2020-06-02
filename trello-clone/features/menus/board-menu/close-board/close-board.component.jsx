import React from 'react';

import useStyles from './close-board.styles';

export default function CloseBoard() {
  const classes = useStyles();
  return (
    <div className={classes.content}>
      <p>
        You can re-open the board by clicking the "Boards" menu from the header,
        selecting "View Closed Boards", finding the board and clicking
        "Re-open".
      </p>
      <input type="submit" value="Close" />
    </div>
  );
}
