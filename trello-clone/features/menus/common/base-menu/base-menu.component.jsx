import React, { useState } from 'react';
import PropTypes from 'prop-types';

import Divider from '@material-ui/core/Divider';
import Menu from '@material-ui/core/Menu';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes, faChevronLeft } from '@fortawesome/free-solid-svg-icons';

import ListOptions from '../list-options/list-options.component';
import useBaseMenuStyles from './base-menu.styles';

export default function BaseMenu({
  anchorElement,
  handleClose,
  actions,
  panels,
  initialPanel = 'main'
}) {
  const classes = useBaseMenuStyles();

  const [activePanel, setActivePanel] = useState(initialPanel);

  const renderButton = (className, icon, onClick) => {
    return (
      <div className={className} onClick={onClick}>
        <FontAwesomeIcon icon={icon} />
      </div>
    );
  };

  const renderBackButton = () => {
    if (activePanel === 'main') return null;
    return renderButton(classes.backButton, faChevronLeft, () =>
      setActivePanel('main')
    );
  };

  const renderCloseButton = () => {
    return renderButton(classes.closeButton, faTimes, handleClose);
  };

  const renderTitle = () => {
    return <div className={classes.title}>{panels[activePanel].title}</div>;
  };

  const renderActivePanel = () => {
    const processedActions = actions.map(action => {
      if (typeof action.onClick === 'function') return action;
      return {
        ...action,
        onClick: () => setActivePanel(action.onClick)
      };
    });
    if (panels[activePanel].component) {
      return panels[activePanel].component;
    }
    if (activePanel === 'main') {
      return <ListOptions options={processedActions} />;
    }
    return null;
  };

  return (
    <Menu
      id="list-menu"
      getContentAnchorEl={null}
      anchorEl={anchorElement}
      keepMounted
      open={Boolean(anchorElement)}
      onClose={handleClose}
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'left'
      }}
      transformOrigin={{
        vertical: 'top',
        horizontal: 'left'
      }}
    >
      <div className={classes.container}>
        <div className={classes.header}>
          {renderBackButton()}
          {renderTitle()}
          {renderCloseButton()}
        </div>
        <Divider className={classes.divider} />
        {anchorElement && renderActivePanel()}
      </div>
    </Menu>
  );
}

BaseMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
