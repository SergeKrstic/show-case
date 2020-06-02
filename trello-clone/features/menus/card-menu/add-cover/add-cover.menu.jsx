import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import AddCover from './add-cover.component';

export default function AddCoverMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Add Cover', component: <AddCover /> }
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

AddCoverMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
