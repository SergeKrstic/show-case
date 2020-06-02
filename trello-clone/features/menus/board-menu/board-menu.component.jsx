import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../common/base-menu/base-menu.component';
import SetBoardColor from '../create-board-menu/set-board-color/set-board-color.component';
import EditLabels from '../card-menu/edit-labels/edit-labels.component';
import ArchivedItems from './archived-items/archived-items.component';
import CopyBoard from './copy-board/copy-board.component';
import CloseBoard from './close-board/close-board.component';
import ExportData from './export-data/export-data.component';
import ChangeSettings from './change-settings/change-settings.component';
import ChangeDescription from './change-description/change-description.component';

export default function CardMenu({ anchorElement, handleClose }) {
  const actions = [
    {
      type: 'menuItem',
      name: 'Change description...',
      onClick: 'description'
    },
    {
      type: 'menuItem',
      name: 'Change background...',
      onClick: 'background'
    },

    {
      type: 'menuItem',
      name: 'Edit labels...',
      onClick: 'labels'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'View archived items...',
      onClick: 'archive'
    },
    {
      type: 'menuItem',
      name: 'Copy board...',
      onClick: 'copy'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Export...',
      onClick: 'export'
    },
    {
      type: 'menuItem',
      name: 'Print',
      onClick: () => {}
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Edit settings...',
      onClick: 'settings'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Close board...',
      onClick: 'close'
    }
  ];

  const panels = {
    main: { title: 'Board Menu', component: null },
    description: {
      title: 'Change Description',
      component: <ChangeDescription />
    },
    background: { title: 'Change Background', component: <SetBoardColor /> },
    labels: { title: 'Labels', component: <EditLabels /> },
    archive: { title: 'Archive', component: <ArchivedItems /> },
    copy: { title: 'Copy Board', component: <CopyBoard /> },
    export: { title: 'Export', component: <ExportData /> },
    settings: { title: 'Settings', component: <ChangeSettings /> },
    close: { title: 'Close Board?', component: <CloseBoard /> }
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

CardMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
