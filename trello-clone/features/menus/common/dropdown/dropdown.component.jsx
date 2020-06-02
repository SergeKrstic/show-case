import React from 'react';

import useStyles from './dropdown.styles';

const Dropdown = ({ options, labelName, isGrouped }) => {
  const classes = useStyles();

  const getSelected = options => {
    if (isGrouped) {
      for (let group of options) {
        for (let item of group.items) {
          if (item.isCurrent) return item;
        }
      }
    } else {
      for (let item of options) {
        if (item.isCurrent) return item;
      }
    }
    return null;
  };

  const renderGroups = groups => {
    return options.map(group => (
      <optgroup key={group.id} label={group.name}>
        {renderItems(group.items)}
      </optgroup>
    ));
  };

  const renderItems = items => {
    return items.map(item => (
      <option key={item.id} value={item.name} selected={item.isCurrent}>
        {`${item.name} ${item.isCurrent ? '(current)' : ''}`}
      </option>
    ));
  };

  return (
    <div className={classes.dropdown}>
      <div>
        <span className={classes.label}>{labelName}</span>
        <span className={classes.value}>{getSelected(options).name}</span>
        <select id={labelName}>
          {isGrouped ? renderGroups(options) : renderItems(options)}
        </select>
      </div>
    </div>
  );
};

export default Dropdown;
