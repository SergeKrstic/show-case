import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';
// import TextareaAutosize from 'react-textarea-autosize';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

import useCreateCardStyles from './create-card.styles';

function CreateCard(props) {
  const hasText = props.name !== undefined;
  const classes = useCreateCardStyles({ hasText });

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
          component="textarea"
          dir="auto"
          onKeyDown={handleSpecialKeyPresses}
        />
        {/* <TextareaAutosize
          autoFocus
          value={props.cardName}
          className={classes.createCardFormCardTitle}
          onChange={event => {
            props.onChange(props.listId, event.target.value);
          }}
          onKeyDown={handleSpecialKeyPresses}
        /> */}
        <div className={classes.controls}>
          <button
            type="submit"
            className={classes.submitButton}
            disabled={!hasText}
          >
            Add Card
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

CreateCard.propTypes = {
  listId: PropTypes.string.isRequired,
  onFocus: PropTypes.func.isRequired,
  onBlur: PropTypes.func.isRequired,
  onClose: PropTypes.func.isRequired,
  onSubmit: PropTypes.func.isRequired
};

export default reduxForm({ form: 'createCardForm' })(CreateCard);
