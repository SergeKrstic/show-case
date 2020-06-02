import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';

import useUpdateListNameStyles from './update-list-name.styles';

function UpdateListName({
  onFocus,
  onBlur,
  pristine,
  submitting,
  handleSubmit
}) {
  const classes = useUpdateListNameStyles();

  const handleSpecialKeyPresses = event => {
    if (event.keyCode === 13) {
      processText(event);
      handleBlur(event);
    }
    if (event.keyCode === 27) {
      handleBlur(event);
    }
  };

  const processText = event => {
    if (!pristine && !submitting) {
      handleSubmit(event);
    }
    handleBlur(event);
  };

  const handleBlur = event => {
    event.target.blur();
    onBlur();
  };

  return (
    <div
      className={classes.updateListNameForm}
      tabIndex="0"
      onFocus={() => {
        onFocus();
      }}
      onBlur={event => {
        processText(event);
      }}
    >
      <form onSubmit={handleSubmit}>
        <Field
          className={classes.updateListNameFormText}
          autoFocus={true}
          type="text"
          name="name"
          value=""
          component="input"
          dir="auto"
          onKeyDown={handleSpecialKeyPresses}
        />
      </form>
    </div>
  );
}

UpdateListName.propTypes = {
  onFocus: PropTypes.func.isRequired,
  onBlur: PropTypes.func.isRequired
};

export default reduxForm({ form: 'updateListNameForm' })(UpdateListName);
