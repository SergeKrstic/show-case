import React, { useState } from 'react';

import { Divider } from '@material-ui/core';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faRedoAlt } from '@fortawesome/free-solid-svg-icons';

import Card from '../../../board-view/card/card.component';

import useStyles from './archived-items.styles';

const cardData = {
  id: 'card-01',
  name: 'Card name',
  boardName: 'Board 1',
  labels: [
    { name: 'label 1', color: 'green' },
    { name: 'label 2', color: 'orange' }
  ]
};

const archivedLists = [
  { name: 'Archived List 1' },
  { name: 'Archived List 2' },
  { name: 'Archived List 3' }
];

const archivedCards = [
  { ...cardData, name: 'Archived Card 1' },
  { ...cardData, name: 'Archived Card 2' },
  { ...cardData, name: 'Archived Card 3' }
];

const ArchivedList = ({ listName }) => {
  const classes = useStyles();
  return (
    <div className={classes.archivedItemContainer}>
      <div className={classes.archivedListContent}>
        <div className={classes.archivedListTitle}>{listName}</div>
        <button>
          <span>
            <FontAwesomeIcon flip="horizontal" icon={faRedoAlt} />
          </span>
          Send to Board
        </button>
      </div>
      <Divider />
    </div>
  );
};

const ArchivedCard = ({ card }) => {
  const classes = useStyles();
  return (
    <div className={classes.archivedItemContainer}>
      <Card card={card} />
      <div className={classes.archivedCardOptions}>
        <button>Send to Board</button>
        {` - `}
        <button>Delete</button>
      </div>
    </div>
  );
};

export default function ArchivedItems() {
  const classes = useStyles();
  const [activeArchive, setActiveArchive] = useState('cards');

  const handleSwitch = () => {
    setActiveArchive(activeArchive === 'cards' ? 'lists' : 'cards');
  };

  const renderArchivedLists = () => {
    return archivedLists.map((list, index) => (
      <ArchivedList listName={list.name} />
    ));
  };

  const renderArchivedCards = () => {
    return archivedCards.map((card, index) => <ArchivedCard card={card} />);
  };

  const renderNoItemsPanelIfEmpty = () => {
    // Todo...
    if (true) return null;

    return (
      <p className={classes.noItems}>{`No archived to ${activeArchive}`}</p>
    );
  };

  return (
    <div className={classes.container}>
      <div className={classes.content}>
        <div className={classes.controls}>
          <div>
            <input type="text" value="" placeholder="Search archive..." />
          </div>
          <button onClick={handleSwitch}>{`Switch to ${
            activeArchive === 'cards' ? 'lists' : 'cards'
          }`}</button>
        </div>
        <div className={classes.archivedItems}>
          {activeArchive === 'cards'
            ? renderArchivedCards()
            : renderArchivedLists()}
          {renderNoItemsPanelIfEmpty()}
        </div>
      </div>
    </div>
  );
}
