import React from 'react';
import PropTypes from 'prop-types';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

import './pop-over.styles.css';

const propTypes = {
  fullName: PropTypes.string.isRequired
};

export default function PopOver(props) {
  const hidePopOver = () => {
    props.popOverActions.hidePopOver();
  };

  const logout = () => {
    hidePopOver();
    props.loginActions.logoutUser();
  };

  const focusOnPopHover = isFocusOnPopHover => {
    if (isFocusOnPopHover) {
      props.popOverActions.focusOnPopHover();
    } else {
      props.popOverActions.blurOnPopHover();
    }
  };

  return (
    <div
      className="PopOver"
      tabIndex="0"
      onFocus={() => {
        focusOnPopHover(true);
      }}
      onBlur={() => {
        focusOnPopHover(false);
      }}
    >
      <div className="PopOver-Header">
        <span className="PopOver-Header-Title">
          {props.fullName}
          <FontAwesomeIcon
            icon={faTimes}
            className="PopOver-Header-Close-Button"
            onClick={() => {
              hidePopOver();
            }}
          />
        </span>
      </div>
      <div className="PopOver-Content">
        <div className="PopOver-Content-List">
          <p onClick={() => logout()}>Logout</p>
        </div>
      </div>
    </div>
  );
}

PopOver.propTypes = propTypes;
