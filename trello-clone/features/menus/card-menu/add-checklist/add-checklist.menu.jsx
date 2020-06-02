import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import AddChecklist from './add-checklist.component';

export default function AddChecklistMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Add Checklist', component: <AddChecklist /> }
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

AddChecklistMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
