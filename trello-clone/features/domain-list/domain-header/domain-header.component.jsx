import React from 'react';
import PropTypes from 'prop-types';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faArrowAltCircleRight,
  // faHockeyPuck,
  // faDatabase,
  // faFolder,
  // faCubes,
  faMinus,
  faCube,
  faStar,
  faCog
} from '@fortawesome/free-solid-svg-icons';

import useDomainHeaderStyles from './domain-header.styles';

const DomainHeader = ({ mode, domainName, iconName }) => {
  const classes = useDomainHeaderStyles();

  const getIcon = iconName => {
    if (iconName === 'focus') return faArrowAltCircleRight;
    if (iconName === 'star') return faStar;
    if (iconName === 'domain') return faCube;
  };

  const renderGridHeader = () => (
    <div className={classes.gridHeaderContainer}>
      <div className={classes.gridHeaderIconContainer}>
        <FontAwesomeIcon
          className={classes.gridHeaderIcon}
          icon={getIcon(iconName)}
        />
      </div>
      <h3>{domainName}</h3>
      <div className={classes.gridHeaderSettings}>
        <FontAwesomeIcon
          className={classes.gridHeaderSettingsIcon}
          icon={faCog}
        />
        Settings
      </div>
    </div>
  );

  const renderListHeader = () => (
    <div className={classes.listHeaderContainer}>
      <FontAwesomeIcon
        className={classes.listHeaderIcon}
        icon={getIcon(iconName)}
      />
      <div className={classes.listHeaderTitle}>{domainName}</div>
      <div className={classes.listHeaderButton}>
        <FontAwesomeIcon icon={faMinus} />
      </div>
    </div>
  );

  return mode === 'grid' ? renderGridHeader() : renderListHeader();
};

DomainHeader.propTypes = {
  mode: PropTypes.oneOf(['grid', 'list']),
  domainName: PropTypes.string.isRequired,
  iconName: PropTypes.oneOf(['focus', 'star', 'domain'])
};

export default DomainHeader;
