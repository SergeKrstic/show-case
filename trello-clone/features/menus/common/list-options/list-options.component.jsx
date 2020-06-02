import React from 'react';
import PropTypes from 'prop-types';
import cx from 'classnames';

import Divider from '@material-ui/core/Divider';
import MenuItem from '@material-ui/core/MenuItem';

import useStyles from './list-options.styles';

export default function ListOptions({ options }) {
  const classes = useStyles();

  return (
    <div className={classes.content}>
      {options.map((option, index) => {
        if (option.type === 'divider') {
          return <Divider key={index} className={classes.divider} />;
        }

        return (
          <MenuItem
            key={index}
            className={cx(classes.menuItem, {
              [classes.muted]: option.isCurrent
            })}
            onClick={option.onClick}
          >
            {`${option.name} ${option.isCurrent ? '(current)' : ''}`}
          </MenuItem>
        );
      })}
    </div>
  );
}

ListOptions.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.shape({
      type: PropTypes.oneOf(['menuItem', 'divider']).isRequired,
      name: PropTypes.string,
      isCurrent: PropTypes.bool,
      onClick: PropTypes.func
    })
  )
};
