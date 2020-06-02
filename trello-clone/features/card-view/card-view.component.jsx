import React, { useState } from 'react';
import MarkDownEditor from './markdown-editor.component';

import NotesIcon from '@material-ui/icons/Subject';
import CardIcon from '@material-ui/icons/VideoLabel';

import BaseDialog from '../../components/base-dialog/base-dialog.component';
import AddLabelsMenu from '../menus/card-menu/edit-labels/edit-labels.menu';
import AddChecklistMenu from '../menus/card-menu/add-checklist/add-checklist.menu';
import AddDueDateMenu from '../menus/card-menu/change-due-date/change-due-date.menu';
import AddAttachmentMenu from '../menus/card-menu/add-attachment/add-attachment.menu';
import AddCoverMenu from '../menus/card-menu/add-cover/add-cover.menu';
import MoveCardMenu from '../menus/card-menu/move-card/move-card.menu';
import CopyCardMenu from '../menus/card-menu/copy-card/copy-card.menu';

import useStyles from './card-view.styles';

export default function CardView({
  card,
  isOpen,
  cardViewActions,
  modelsActions
}) {
  const classes = useStyles();

  const [text, setText] = useState(card.description);
  const [selectedTab, setSelectedTab] = useState('preview');
  const [anchorElement, setAnchorElement] = useState(null);
  const [anchorName, setAnchorName] = useState(null);

  const handleOpenMenu = name => event => {
    setAnchorElement(event.currentTarget);
    setAnchorName(name);
  };

  const handleCloseMenu = () => {
    setAnchorElement(null);
    setAnchorName(null);
  };

  const handleCloseDialog = () => {
    modelsActions.updateCard({
      id: card.id,
      data: { description: text }
    });
    cardViewActions.hideCardView();
  };

  const renderMenu = () => {
    if (!anchorName) return null;

    const menus = {
      'add-labels': AddLabelsMenu,
      'add-checklist': AddChecklistMenu,
      'add-due-date': AddDueDateMenu,
      'add-attachment': AddAttachmentMenu,
      'add-cover': AddCoverMenu,
      'move-card': MoveCardMenu,
      'copy-card': CopyCardMenu
    };

    const MenuComponent = menus[anchorName];

    return (
      <MenuComponent
        anchorElement={anchorElement}
        handleClose={handleCloseMenu}
      />
    );
  };

  return (
    <BaseDialog
      handleClose={handleCloseDialog}
      isOpen={isOpen}
      title={card.name}
      subtitle={`in list ${card.listName}`}
      icon={<CardIcon />}
      fullScreen
    >
      <div className={classes.cardPanels}>
        <div className={classes.cardContentPanel}>
          <div className={classes.moduleTitle}>
            <h3>Description</h3>
            <span>
              <NotesIcon />
            </span>
          </div>
          <div className={classes.editor}>
            <MarkDownEditor
              text={text}
              onChange={setText}
              selectedTab={selectedTab}
              onTabChange={setSelectedTab}
              minEditorHeight={2000}
            />
          </div>
        </div>
        <div className={classes.cardSidebarPanel}>
          <h5>ADD TO CARD</h5>
          <button onClick={handleOpenMenu('add-labels')}>Labels</button>
          <button onClick={handleOpenMenu('add-checklist')}>Checklist</button>
          <button onClick={handleOpenMenu('add-due-date')}>Due Date</button>
          <button onClick={handleOpenMenu('add-attachment')}>Attachment</button>
          <button onClick={handleOpenMenu('add-cover')}>Cover</button>
          <h5>ACTIONS</h5>
          <button onClick={handleOpenMenu('move-card')}>Move</button>
          <button onClick={handleOpenMenu('copy-card')}>Copy</button>
          <button>Archive</button>
          {renderMenu()}
        </div>
      </div>
    </BaseDialog>
  );
}
