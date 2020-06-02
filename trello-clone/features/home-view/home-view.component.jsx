import React from 'react';
import PropTypes from 'prop-types';

import DomainList from '../domain-list/domain-list.container';
import Notification from '../notification/notification.component';

import useHomeViewStyles from './home-view.styles';

const HomeView = props => {
  const classes = useHomeViewStyles();

  const renderNotificationErrorMessage = () => {
    const { errorMessages } = props;

    if (errorMessages && errorMessages.length > 0) {
      return <Notification errorMessages={errorMessages} />;
    } else {
      return null;
    }
  };

  return (
    <div className={classes.homeView}>
      <DomainList mode="grid" {...props} />
      {renderNotificationErrorMessage()}
    </div>
  );
};

HomeView.propTypes = {
  domains: PropTypes.array.isRequired,
  boards: PropTypes.array.isRequired,
  errorMessages: PropTypes.array
};

export default HomeView;
