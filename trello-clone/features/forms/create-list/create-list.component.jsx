import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

import useCreateListStyles from './create-list.styles';

const propTypes = {
  onFocus: PropTypes.func.isRequired,
  onBlur: PropTypes.func.isRequired,
  onClose: PropTypes.func.isRequired,
  onSubmit: PropTypes.func.isRequired
};

function CreateList(props) {
  const classes = useCreateListStyles();

  const hasText = props.name !== undefined;

  const handleSpecialKeyPresses = event => {
    if (event.keyCode === 13) handleSubmit(event);
    if (event.keyCode === 27) props.onClose();
  };

  const handleSubmit = event => {
    event.preventDefault();
    props.handleSubmit();
  };
  return (
    <div
      className={classes.container}
      tabIndex="0"
      onFocus={() => {
        props.onFocus();
      }}
      onBlur={() => {
        props.onBlur();
      }}
    >
      <form onSubmit={handleSubmit}>
        <Field
          className={classes.cardTitle}
          autoFocus={true}
          type="text"
          name="name"
          value=""
          placeholder="Enter list title..."
          component="input"
          dir="auto"
          onKeyDown={handleSpecialKeyPresses}
        />
        <div className={classes.controls}>
          <button
            type="submit"
            className={classes.submitButton}
            disabled={!hasText}
          >
            Save
          </button>
          <FontAwesomeIcon
            icon={faTimes}
            size="2x"
            className={classes.closeButton}
            onClick={() => {
              props.onClose();
            }}
          />
        </div>
      </form>
    </div>
  );
}

CreateList.propTypes = propTypes;

export default reduxForm({ form: 'createListForm' })(CreateList);
