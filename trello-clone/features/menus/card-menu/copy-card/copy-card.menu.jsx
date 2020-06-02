import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import CopyCard from './copy-card.component';

export default function CopyCardMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Copy Card', component: <CopyCard /> }
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

CopyCardMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
