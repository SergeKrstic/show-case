import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../common/base-menu/base-menu.component';
import ChangeDomain from './change-domain/change-domain.component';

const DomainMenu = ({ anchorElement, handleClose }) => {
  const actions = [];

  const panels = {
    main: { title: 'Change Domain', component: <ChangeDomain /> }
  };

  return (
    <BaseMenu
      anchorElement={anchorElement}
      handleClose={handleClose}
      actions={actions}
      panels={panels}
    />
  );
};

DomainMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};

export default DomainMenu;
