import React from 'react';
import PropTypes from 'prop-types';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

import useStyles from './toolbar-button.styles';

const ToolbarButton = ({ text, icon, iconType, onClick, ...rest }) => {
  const classes = useStyles({ text, iconType, ...rest });

  const renderIcon = () => {
    const Icon = icon;
    if (!icon) return null;
    if (iconType === 'mui')
      return <Icon className={classes.headerButtonIcon} />;
    if (iconType === 'fa')
      return (
        <FontAwesomeIcon className={classes.headerButtonIcon} icon={icon} />
      );
  };

  return (
    <div className={classes.headerButton} tabIndex="0" onClick={onClick}>
      <span>{renderIcon()}</span>
      <span>{text}</span>
    </div>
  );
};

export const ToolbarButtonWrapper = props => {
  const classes = useStyles(props);
  return (
    <div className={classes.headerButtonContainer}>
      <ToolbarButton {...props} />
    </div>
  );
};

ToolbarButton.propTypes = {
  text: PropTypes.string,
  onClick: PropTypes.func.isRequired,
  icon: PropTypes.object,
  iconType: PropTypes.oneOf(['fa', 'mui']),
  isSelected: PropTypes.bool,
  isDark: PropTypes.bool,
  isBold: PropTypes.bool,
  isFlippedY: PropTypes.bool
};

ToolbarButton.defaultProps = {
  icon: null,
  iconType: 'fa',
  isSelected: false,
  isDark: false,
  isBold: false,
  isFlippedY: false
};

export default ToolbarButton;
