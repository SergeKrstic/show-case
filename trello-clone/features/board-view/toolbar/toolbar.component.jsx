import React, { useState } from 'react';

import CreateBoardMenu from '../../menus/create-board-menu/create-board-menu.component';
import ToolbarButton from './toolbar-button/toolbar-button.component';
import useToolbarStyles from './toolbar.styles';

import InsertChart from '@material-ui/icons/InsertChart';
import {
  faHome,
  faBullseye,
  faFlag,
  faStar,
  faPlus
} from '@fortawesome/free-solid-svg-icons';

// today: fire, filter, fist-raised, dot-circle, bullseye
// next: flag, forward, arrow-circle-right

export default function BoardsToolbar({
  boards,
  activeBoardId,
  boardViewActions,
  boardsMenuActions,
  homeViewActions
}) {
  const classes = useToolbarStyles();
  const [anchorElement, setAnchorElement] = useState(null);

  const handleOpenMenu = event => {
    setAnchorElement(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setAnchorElement(null);
  };

  const handleGoHome = () => {
    homeViewActions.openHomeView();
  };

  const renderSpecialBoardButton = (name, icon) => {
    const board = boards.find(board => board.name === name);
    if (board) return renderBoardButton(board, icon);
  };

  const renderRemainingBoardButtons = () => {
    return boards.map(board => {
      if (['Today', 'Next'].includes(board.name)) return null;
      if (!board.isStarred) return null;
      return renderBoardButton(board, faStar);
    });
  };

  const renderBoardButton = (board, icon) => {
    return (
      <ToolbarButton
        key={board.id}
        text={board.name}
        icon={icon}
        onClick={() => boardViewActions.setBoardId({ id: board.id })}
        isSelected={activeBoardId === board.id}
        isDark={activeBoardId === board.id}
      />
    );
  };

  return (
    <div className={classes.header}>
      <ToolbarButton icon={faHome} onClick={handleGoHome} />
      <ToolbarButton
        text="Boards"
        icon={InsertChart}
        iconType="mui"
        isFlippedY
        isBold
        onClick={() => boardsMenuActions.openBoardsMenu()}
      />
      <ToolbarButton icon={faPlus} onClick={handleOpenMenu} />
      <CreateBoardMenu
        anchorElement={anchorElement}
        handleClose={handleCloseMenu}
      />
      <div className={classes.divider} />
      {renderSpecialBoardButton('Today', faBullseye)}
      {renderSpecialBoardButton('Next', faFlag)}
      <div className={classes.divider} />
      {renderRemainingBoardButtons()}
      <div className={classes.spacer} />
    </div>
  );
}
