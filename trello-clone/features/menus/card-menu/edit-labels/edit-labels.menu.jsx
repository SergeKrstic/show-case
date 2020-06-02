import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import EditLabels from './edit-labels.component';

export default function EditLabelsMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Labels', component: <EditLabels /> }
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

EditLabelsMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
