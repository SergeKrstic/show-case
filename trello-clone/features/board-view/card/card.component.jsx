import React, { useState } from 'react';
import PropTypes from 'prop-types';

import CreateIcon from '@material-ui/icons/Create';
import NotesIcon from '@material-ui/icons/Notes';

import CardMenu from '../../menus/card-menu/card-menu.container';

import { colors } from '../../common.styles';
import useCardStyles from './card.styles';

const LabelColors = {
  green: colors.LabelGreen,
  yellow: colors.LabelYellow,
  orange: colors.LabelOrange,
  red: colors.LabelRed,
  purple: colors.LabelPurple,
  blue: colors.LabelBlue,
  sky: colors.LabelSky,
  lime: colors.LabelLime,
  pink: colors.LabelPink,
  black: colors.LabelBlack
};

const Card = ({
  card,
  currentBoardId,
  boardViewActions,
  cardViewActions,
  innerRef,
  ...rest
}) => {
  const classes = useCardStyles();
  const [anchorElement, setAnchorElement] = useState(null);

  const handleOpenMenu = event => {
    event.stopPropagation();
    setAnchorElement(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setAnchorElement(null);
  };

  const handleMouseEnter = () => {
    boardViewActions.setActiveCard({ id: card.id });
  };

  const handleMouseLeave = () => {
    boardViewActions.setActiveCard({ id: null });
  };

  const handleOpenCardView = () => {
    if (anchorElement) return null;
    cardViewActions.openCardView({ id: card.id });
  };

  const renderCardHeader = () => {
    if (card.boardId !== currentBoardId) {
      return <div className={classes.cardHeader}>{card.boardName}</div>;
    }
  };

  const renderEditButton = () => {
    return (
      <span className={classes.editButton} onClick={handleOpenMenu}>
        <CreateIcon />
      </span>
    );
  };

  const renderCardMenu = () => {
    return (
      <CardMenu
        card={card}
        anchorElement={anchorElement}
        handleClose={handleCloseMenu}
      />
    );
  };

  const renderCardLabels = () => {
    if (!card.labels) return null;
    return (
      <div className={classes.labels}>
        {card.labels.map((label, index) => (
          <div
            key={index}
            className={classes.cardLabel}
            style={{ backgroundColor: LabelColors[label.color] }}
          >
            {label.name}
          </div>
        ))}
      </div>
    );
  };

  const renderCardBadges = () => {
    if (card.description) {
      return (
        <div className={classes.cardBadges}>
          <i>
            <NotesIcon />
          </i>
        </div>
      );
    }
  };

  return (
    <div className={classes.card} ref={innerRef} {...rest}>
      <div
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        onClick={handleOpenCardView}
      >
        {renderCardMenu()}
        {renderCardHeader()}
        <div className={classes.cardContent}>
          {renderEditButton()}
          {renderCardLabels()}
          <p fs-exclude>{card.name}</p>
          {renderCardBadges()}
        </div>
      </div>
    </div>
  );
};

Card.propTypes = {
  // card: PropTypes.object.isRequired,
  currentBoardId: PropTypes.string.isRequired
};

export default Card;
