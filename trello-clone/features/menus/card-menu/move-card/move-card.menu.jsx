import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../../common/base-menu/base-menu.component';
import MoveCard from './move-card.component';

export default function MoveCardMenu({ anchorElement, handleClose }) {
  const actions = [];

  const panels = {
    main: { title: 'Move Card', component: <MoveCard /> }
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

MoveCardMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};
