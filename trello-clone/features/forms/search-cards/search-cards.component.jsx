import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch, faTimes } from '@fortawesome/free-solid-svg-icons';

import useSearchCardsStyles from './search-cards.styles';

function SearchCards({ searchTerm, onSearchTermChange, reset }) {
  const classes = useSearchCardsStyles();

  const handleSpecialKeyPresses = event => {
    if (event.keyCode === 27) {
      event.target.blur();
      handleReset();
    }
  };

  const handleReset = () => {
    onSearchTermChange({ searchTerm: '' });
    reset();
  };

  const handleOnChange = event => {
    onSearchTermChange({ searchTerm: event.target.value });
  };

  return (
    <div className={classes.searchBox} tabIndex="0">
      <Field
        className={classes.searchBoxText}
        name="searchTerm"
        type="text"
        autoComplete="off"
        autoCorrect="off"
        spellCheck="false"
        value=""
        component="input"
        dir="auto"
        onKeyDown={handleSpecialKeyPresses}
        onChange={handleOnChange}
      />
      <div className={classes.searchBoxIcon} onClick={handleReset}>
        {searchTerm ? (
          <FontAwesomeIcon icon={faTimes} />
        ) : (
          <FontAwesomeIcon icon={faSearch} />
        )}
      </div>
    </div>
  );
}

SearchCards.propTypes = {
  onSearchTermChange: PropTypes.func.isRequired
};

export default reduxForm({ form: 'searchCardsForm' })(SearchCards);
