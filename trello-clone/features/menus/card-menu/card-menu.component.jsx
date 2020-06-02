import React from 'react';
import PropTypes from 'prop-types';

import EditLabels from './edit-labels/edit-labels.component';
import CopyCard from './copy-card/copy-card.component';
import MoveCard from './move-card/move-card.component';
import ChangeDueDate from './change-due-date/change-due-date.component';

import BaseMenu from '../common/base-menu/base-menu.component';

export default function CardMenu({
  card,
  anchorElement,
  handleClose,
  modelsActions
}) {
  const handleRename = () => {
    const newName = prompt('Rename card:', card.name);
    if (newName)
      modelsActions.updateCard({
        id: card.id,
        data: { name: newName }
      });
    handleClose();
  };

  const actions = [
    {
      type: 'menuItem',
      name: 'Rename...',
      onClick: handleRename
    },
    {
      type: 'menuItem',
      name: 'Edit Labels...',
      onClick: 'labels'
    },
    {
      type: 'menuItem',
      name: 'Change Due Date...',
      onClick: 'changeDueDate'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Move...',
      onClick: 'move'
    },
    {
      type: 'menuItem',
      name: 'Copy...',
      onClick: 'copy'
    },
    { type: 'divider' },
    {
      type: 'menuItem',
      name: 'Archive',
      onClick: handleClose
    }
  ];

  const panels = {
    main: { title: 'Card Actions', component: null },
    labels: { title: 'Labels', component: <EditLabels /> },
    move: { title: 'Move Card', component: <MoveCard /> },
    copy: { title: 'Copy Card', component: <CopyCard /> },
    changeDueDate: {
      title: 'Change Due Date',
      component: <ChangeDueDate />
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

CardMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
