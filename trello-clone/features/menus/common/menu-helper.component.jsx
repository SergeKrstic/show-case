import React, { useState } from 'react';
import PropTypes from 'prop-types';
import Button from '@material-ui/core/Button';

const MenuHelper = ({ buttonName, menuComponent }) => {
  const [anchorElement, setAnchorElement] = useState(null);
  const MenuComponent = menuComponent;

  const handleClick = event => {
    setAnchorElement(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorElement(null);
  };

  return (
    <div style={{ padding: '50px 0 0 50px' }}>
      <Button onClick={handleClick}>{buttonName}</Button>
      <MenuComponent anchorElement={anchorElement} handleClose={handleClose} />
    </div>
  );
};

MenuHelper.propTypes = {
  buttonName: PropTypes.string,
  menuComponent: PropTypes.any.isRequired
};

MenuHelper.defaultProps = {
  buttonName: 'Open Menu'
};

export default MenuHelper;
