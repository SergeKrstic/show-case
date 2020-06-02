import React from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

import useStyles from './find-board-photo.styles';

import { boardImageUrls } from '../common.styles';

export default function CopyCard() {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      <div className={classes.search}>
        <div>
          <FontAwesomeIcon icon={faSearch} />
        </div>
        <input placeholder="Photos" value="" />
      </div>
      <div className={classes.imageContainer}>
        {boardImageUrls.map((imageUrl, index) => (
          <div
            key={index}
            className={classes.image}
            style={{ backgroundImage: imageUrl }}
          />
        ))}
      </div>
    </div>
  );
}
