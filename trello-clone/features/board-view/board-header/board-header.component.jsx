import React, { useState } from 'react';
import PropTypes from 'prop-types';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faStar, faEllipsisH } from '@fortawesome/free-solid-svg-icons';

import BoardMenu from '../../menus/board-menu/board-menu.component';
import DomainMenu from '../../menus/domain-menu/domain-menu.component';
import SearchCards from '../../forms/search-cards/search-cards.container';

import useBoardHeaderStyles from './board-header.styles';

const BoardHeader = ({ board, modelsActions }) => {
  const classes = useBoardHeaderStyles();

  const [anchorElement, setAnchorElement] = useState(null);
  const [anchorName, setAnchorName] = useState(null);

  const handleOpenMenu = name => event => {
    setAnchorElement(event.currentTarget);
    setAnchorName(name);
  };

  const handleCloseMenu = () => {
    setAnchorElement(null);
  };

  const renderBoardTitle = () => {
    if (['Today', 'Next'].includes(board.name)) {
      return <div className={classes.boardHeaderName}>{board.name}</div>;
    } else {
      return (
        <div
          className={classes.boardHeaderName}
          onClick={() => alert('Todo: allow user to update the board name')}
        >
          {board.name}
        </div>
      );
    }
  };

  const renderBoardStar = () => {
    if (['Today', 'Next'].includes(board.name)) return null;

    return (
      <div
        className={
          board.isStarred
            ? classes.boardHeaderButtonSelected
            : classes.boardHeaderButton
        }
        onClick={() => {
          modelsActions.updateBoard({
            id: board.id,
            data: {
              isStarred: !board.isStarred
            }
          });
        }}
      >
        <FontAwesomeIcon
          className={
            board.isStarred ? classes.boardStarred : classes.boardNotStarred
          }
          icon={faStar}
        />
      </div>
    );
  };

  const renderBoardDomainName = () => {
    if (!board.domainName || ['Today', 'Next'].includes(board.name))
      return null;

    return (
      <div
        className={classes.boardHeaderButton}
        onClick={handleOpenMenu('domain-menu')}
      >
        {board.domainName}
      </div>
    );
  };

  const renderCardSearchBox = () => {
    return <SearchCards />;
  };

  const renderBoardMenuButton = () => {
    return (
      <div
        className={classes.boardHeaderMenuButton}
        onClick={handleOpenMenu('board-menu')}
      >
        <FontAwesomeIcon
          className={classes.boardHeaderMenuIcon}
          icon={faEllipsisH}
        />
        Show Menu
      </div>
    );
  };

  const renderMenu = () => {
    if (!anchorName) return null;
    const menus = {
      'board-menu': BoardMenu,
      'domain-menu': DomainMenu
    };
    const MenuComponent = menus[anchorName];
    return (
      <MenuComponent
        anchorElement={anchorElement}
        handleClose={handleCloseMenu}
      />
    );
  };

  if (!board) return null;

  return (
    <div className={classes.boardHeaderContainer}>
      {renderMenu()}
      {renderBoardTitle()}
      {renderBoardStar()}
      {renderBoardDomainName()}
      {renderCardSearchBox()}
      {renderBoardMenuButton()}
      <div className={classes.spacer} />
    </div>
  );
};

BoardHeader.propTypes = {
  board: PropTypes.object
};

export default BoardHeader;
