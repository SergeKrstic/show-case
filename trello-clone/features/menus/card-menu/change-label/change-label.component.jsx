import React from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheck } from '@fortawesome/free-solid-svg-icons';

import { useChangeLabelStyles, useLabelStyles } from './change-label.styles';

const labels = [
  { color: '#61bd4f', isChecked: true },
  { color: '#f2d600', isChecked: false },
  { color: '#ff9f1a', isChecked: false },
  { color: '#eb5a46', isChecked: false },
  { color: '#c377e0', isChecked: false },
  { color: '#0079bf', isChecked: false },
  { color: '#00c2e0', isChecked: false },
  { color: '#51e898', isChecked: false },
  { color: '#ff78cb', isChecked: false },
  { color: '#344563', isChecked: false }
];

const noColorLabel = {
  color: '#b3bac5',
  isChecked: true
};

const LabelItem = ({ color, isChecked }) => {
  const classes = useLabelStyles({ color });
  return (
    <span className={classes.label}>
      {isChecked && (
        <div className={classes.iconButtonCheck}>
          <FontAwesomeIcon icon={faCheck} />
        </div>
      )}
    </span>
  );
};

const ChangeLabel = () => {
  const classes = useChangeLabelStyles();

  const renderLabelItems = () => labels.map(label => <LabelItem {...label} />);

  return (
    <div className={classes.content}>
      <label>Name</label>
      <input type="text" value="" />
      <label>Select a color</label>
      <div className={classes.clearFix}>{renderLabelItems()}</div>
      <div className={classes.noColorSection}>
        <div>
          <LabelItem {...noColorLabel} />
        </div>
        <div>
          <p>No color</p>
          <p>This won't show up on the front of cards.</p>
        </div>
      </div>
      <button className={classes.buttonSave}>Save</button>
      <button className={classes.buttonDelete}>Delete</button>
    </div>
  );
};

export default ChangeLabel;
