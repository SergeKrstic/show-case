import React from 'react';

import PropTypes from 'prop-types';

import useStyles from './notification.styles';

export default function Notification({ errorMessages }) {
  const classes = useStyles();

  const renderErrorMessages = () => {
    if (!errorMessages.length) return null;

    return errorMessages.map((message, index) => (
      <p className={classes.notificationItem} key={index}>
        {message}
      </p>
    ));
  };

  return <div className={classes.notification}>{renderErrorMessages()}</div>;
}

Notification.propTypes = {
  errorMessages: PropTypes.array.isRequired
};
