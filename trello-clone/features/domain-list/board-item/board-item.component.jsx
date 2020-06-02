import React from 'react';
import PropTypes from 'prop-types';
import cx from 'classnames';

import Grid from '@material-ui/core/Grid';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faStar } from '@fortawesome/free-solid-svg-icons';

import useBoardItemStyles from './board-item.styles';

const BoardItem = ({
  mode,
  boardName,
  domainName,
  isStarred,
  isStarIconVisible,
  isDomainNameVisible,
  isPlaceHolder,
  placeHolderText,
  openBoard,
  toggleBoardStar
}) => {
  const classes = useBoardItemStyles({ isStarred });

  const handleToggleBoardStar = event => {
    event.stopPropagation();
    toggleBoardStar();
  };

  const renderGridItem = () => {
    if (isPlaceHolder) {
      return (
        <Grid item xs={6} sm={4} lg={3}>
          <div className={classes.domainBoardPlaceHolder} onClick={openBoard}>
            {placeHolderText}
          </div>
        </Grid>
      );
    }

    return (
      <Grid item xs={6} sm={4} lg={3}>
        <div className={classes.domainBoardItem} onClick={openBoard}>
          <div className={classes.domainBoardItemContent}>
            <div className={classes.domainBoardItemTitle}>
              <div>{boardName}</div>
            </div>
            {isDomainNameVisible && (
              <div className={classes.domainBoardItemSubTitle}>
                {domainName}
              </div>
            )}
          </div>
          {isStarIconVisible && (
            <FontAwesomeIcon
              icon={faStar}
              name="star-o"
              className={cx(classes.domainBoardItemStarIcon, {
                [classes.domainBoardItemIsStarred]: isStarred
              })}
              onClick={handleToggleBoardStar}
            />
          )}
        </div>
      </Grid>
    );
  };

  const renderListItem = () => (
    <div className={classes.menuBoardItem}>
      <div className={classes.menuBoardItemTile} onClick={openBoard}>
        <span className={classes.menuBoardItemThumbnail} />
        <div
          className={cx(classes.menuBoardItemTileTitle, {
            [classes.menuBoardItemTileWithDomain]: isDomainNameVisible
          })}
        >
          <div className={classes.menuBoardItemTileTitleName}>{boardName}</div>
          {isDomainNameVisible && (
            <div className={classes.menuBoardItemTileTitleSubName}>
              {domainName}
            </div>
          )}
        </div>
        <div
          className={cx(classes.menuBoardItemStarIcon, {
            [classes.menuBoardItemIsStarred]: isStarred
          })}
        >
          <FontAwesomeIcon
            icon={faStar}
            name="star-o"
            onClick={handleToggleBoardStar}
          />
        </div>
      </div>
    </div>
  );

  return mode === 'grid' ? renderGridItem() : renderListItem();
};

BoardItem.propTypes = {
  mode: PropTypes.oneOf(['grid', 'list']),
  boardName: PropTypes.string.isRequired,
  domainName: PropTypes.string.isRequired,
  isStarred: PropTypes.bool.isRequired,
  openBoard: PropTypes.func.isRequired,
  toggleBoardStar: PropTypes.func.isRequired
};

export default BoardItem;
