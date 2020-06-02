import React from 'react';
import PropTypes from 'prop-types';

import CopyList from './copy-list/copy-list.component';
import MoveList from './move-list/move-list.component';
import SortCards from './sort-cards/sort-cards.component';
import MoveAllCards from './move-all-cards/move-all-cards.component';
import ArchiveAllCards from './archive-all-cards/archive-all-cards.component';

import BaseMenu from '../common/base-menu/base-menu.component';

export default function ListMenu({ anchorElement, handleClose }) {
  const actions = [
    {
      type: 'menuItem',
      name: 'Add Card...',
      onClick: handleClose
    },
    {
      type: 'menuItem',
      name: 'Copy List...',
      onClick: 'copyList'
    },
    {
      type: 'menuItem',
      name: 'Move List...',
      onClick: 'moveList'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Sort By...',
      onClick: 'sortBy'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Move All Cards in This List...',
      onClick: 'moveAll'
    },
    {
      type: 'menuItem',
      name: 'Archive All Cards in This List...',
      onClick: 'archiveAll'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Archive This List...',
      onClick: handleClose
    }
  ];

  const panels = {
    main: { title: 'List Actions', component: null },
    copyList: { title: 'Copy List', component: <CopyList /> },
    moveList: { title: 'Move List', component: <MoveList /> },
    sortBy: { title: 'Sort List', component: <SortCards /> },
    moveAll: { title: 'Move All Cards in List', component: <MoveAllCards /> },
    archiveAll: {
      title: 'Archive All Cards in List?',
      component: <ArchiveAllCards />
    }
  };

  return (
    <BaseMenu
      anchorElement={anchorElement}
      handleClose={handleClose}
      actions={actions}
      panels={panels}
    />
  );
}

ListMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
