import React from 'react';

import useStyles from './archive-all-cards.styles';

export default function ArchiveAllCards() {
  const classes = useStyles();
  return (
    <div className={classes.content}>
      <p>
        This will remove all the cards in the list from the board. To view
        archived cards and bring them back to the board, click "Menu" >
        "Archived Items"
      </p>
      <input type="submit" value="Archive All" />
    </div>
  );
}
