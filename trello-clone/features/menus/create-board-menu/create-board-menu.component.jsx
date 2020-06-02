import React from 'react';
import PropTypes from 'prop-types';

import BaseMenu from '../common/base-menu/base-menu.component';
import CreateBoard from './create-board/create-board.component';

const CreateBoardMenu = ({ anchorElement, handleClose }) => {
  const actions = [];

  const panels = {
    main: { title: 'Create a new board', component: <CreateBoard /> }
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

CreateBoardMenu.propTypes = {
  anchorElement: PropTypes.object,
  handleClose: PropTypes.func.isRequired
};

export default CreateBoardMenu;
