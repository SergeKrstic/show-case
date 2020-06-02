import React from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEllipsisH } from '@fortawesome/free-solid-svg-icons';

import { boardColors, boardImageUrls } from '../common.styles';
import useStyles from './create-board.styles';

export default function CreateBoard() {
  const classes = useStyles();

  // const handleAddBoard = () => {
  //   const boardName = prompt('Add a new board:');
  //   if (boardName) modelsActions.addBoard({ name: boardName.trim() });
  // };

  const renderBoardImages = () => {
    const selectedImageUrls = boardImageUrls.slice(0, 4);
    return selectedImageUrls.map((imageUrl, index) => (
      <div
        key={index}
        className={classes.boardImage}
        style={{
          backgroundImage: imageUrl
        }}
      />
    ));
  };

  const renderBoardColors = () => {
    const selectedBoardColors = boardColors.slice(0, 4);
    return selectedBoardColors.map(color => (
      <div
        key={color.name}
        className={classes.boardColor}
        style={{
          backgroundColor: color.value
        }}
      />
    ));
  };

  return (
    <div className={classes.content}>
      <label>Name</label>
      <input type="text" value="" autoFocus />
      <label>Domain</label>
      <select>
        <option>Domain 1</option>
        <option>Domain 2</option>
        <option>Domain 3</option>
      </select>
      <label>Select a background...</label>
      <div className={classes.imageContainer}>
        {renderBoardImages()}
        {renderBoardColors()}
        <div className={classes.moreBackgrounds}>
          <FontAwesomeIcon icon={faEllipsisH} />
        </div>
      </div>
      <button>Create</button>
    </div>
  );
}
