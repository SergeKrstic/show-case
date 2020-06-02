import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import ChangeDueDate from './change-due-date.component';

export default function ChangeDueDateMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Change Due Date', component: <ChangeDueDate /> }
  };

  return (
    <BaseMenu
      anchorElement={anchorElement}
      handleClose={handleClose}
      actions={actions}
      panels={panels}
    />
  );
}

ChangeDueDateMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
