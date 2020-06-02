import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import AddAttachment from './add-attachment.component';

export default function AddAttachmentMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Attach From...', component: <AddAttachment /> }
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

AddAttachmentMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
