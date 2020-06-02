import React from 'react';

import DomainList from '../../domain-list/domain-list.container';

import useAllBoardsMenuStyles from './all-boards-menu.styles';

export default function AllBoardsMenu(props) {
  const classes = useAllBoardsMenuStyles();

  const handleOnChange = event => {
    props.boardsMenuActions.saveUserInput(event.target.value);
  };

  const focusOnBoardsMenu = isFocused => {
    if (isFocused) {
      props.boardsMenuActions.focusOnBoardsMenu();
    } else {
      props.boardsMenuActions.blurOnBoardsMenu();
    }
  };

  return (
    <div
      className={classes.container}
      tabIndex="0"
      onFocus={() => {
        focusOnBoardsMenu(true);
      }}
      onBlur={() => {
        focusOnBoardsMenu(false);
      }}
    >
      <div className={classes.boardsMenu}>
        <div className={classes.boardsMenuContent}>
          <div className={classes.boardsMenuContentSearch}>
            <input
              onChange={handleOnChange}
              placeholder="Find boards by name…"
              type="text"
              autoFocus
            />
          </div>
          <DomainList mode="list" />
        </div>
      </div>
    </div>
  );
}
