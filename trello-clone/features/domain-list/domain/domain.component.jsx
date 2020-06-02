import React from 'react';
import PropTypes from 'prop-types';

// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faStar, faCog } from '@fortawesome/free-solid-svg-icons';

import DomainHeader from '../domain-header/domain-header.component';
import BoardItem from '../board-item/board-item.component';

import useDomainStyles from './domain.styles';

const Domain = ({
  mode,
  domainId,
  domainName,
  iconName,
  boards,
  isStarIconVisible,
  isDomainNameVisible,
  isCreateBoardVisible,
  boardViewActions,
  modelsActions,
  boardsMenuActions,
  homeViewActions
}) => {
  const classes = useDomainStyles();

  const handleOpenBoard = board => {
    boardViewActions.setBoardId({ id: board.id });
    boardsMenuActions.hideBoardsMenu();
    homeViewActions.closeHomeView();
  };

  const handleToggleBoardStar = board => {
    modelsActions.updateBoard({
      id: board.id,
      data: { isStarred: !board.isStarred }
    });
  };

  const handleCreateBoard = () => {
    const boardName = prompt('Add a new board:');
    if (boardName)
      modelsActions.addBoard({
        name: boardName.trim(),
        domainName,
        domainId
      });
  };

  const getClassNameForContainer = () => {
    return mode === 'grid' ? classes.gridContainer : classes.listContainer;
  };

  const getClassNameForContent = () => {
    return mode === 'grid' ? classes.gridContent : classes.listContent;
  };

  const renderCreateBoard = () => {
    if (mode === 'list' || !isCreateBoardVisible) return null;
    return (
      <BoardItem
        mode={mode}
        boardName=""
        domainName=""
        isStarred={false}
        isStarIconVisible={false}
        isDomainNameVisible={false}
        placeHolderText="Create new board"
        isPlaceHolder={isCreateBoardVisible}
        openBoard={handleCreateBoard}
        toggleBoardStar={() => {}}
      />
    );
  };

  return (
    <div className={getClassNameForContainer()}>
      {domainName && (
        <DomainHeader mode={mode} domainName={domainName} iconName={iconName} />
      )}
      <div className={getClassNameForContent()}>
        {boards.map(board => (
          <BoardItem
            key={board.id}
            mode={mode}
            boardName={board.name}
            domainName={board.domainName}
            isStarred={board.isStarred}
            isStarIconVisible={isStarIconVisible}
            isDomainNameVisible={isDomainNameVisible}
            openBoard={() => handleOpenBoard(board)}
            toggleBoardStar={() => handleToggleBoardStar(board)}
          />
        ))}
        {renderCreateBoard()}
      </div>
    </div>
  );
};

Domain.propTypes = {
  mode: PropTypes.oneOf(['grid', 'list']),
  domainName: PropTypes.string.isRequired,
  boards: PropTypes.array.isRequired
};

export default Domain;
