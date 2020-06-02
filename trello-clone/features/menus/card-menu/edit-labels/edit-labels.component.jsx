import React from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faCheck } from '@fortawesome/free-solid-svg-icons';

import { colors } from '../../../common.styles';
import { useEditLabelsStyles, useLabelStyles } from './edit-labels.styles';

const labels = [
  {
    color: colors.LabelGreen,
    shadow: colors.LabelGreenShadow,
    isChecked: true,
    name: 'green'
  },
  {
    color: colors.LabelYellow,
    shadow: colors.LabelYellowShadow,
    isChecked: false,
    name: 'yellow'
  },
  {
    color: colors.LabelOrange,
    shadow: colors.LabelOrangeShadow,
    isChecked: false,
    name: 'orange'
  },
  {
    color: colors.LabelRed,
    shadow: colors.LabelRedShadow,
    isChecked: false,
    name: 'red'
  },
  {
    color: colors.LabelPurple,
    shadow: colors.LabelPurpleShadow,
    isChecked: false,
    name: 'purple'
  },
  {
    color: colors.LabelBlue,
    shadow: colors.LabelBlueShadow,
    isChecked: false,
    name: 'blue'
  },
  {
    color: colors.LabelSky,
    shadow: colors.LabelSkyShadow,
    isChecked: false,
    name: 'sky'
  },
  {
    color: colors.LabelLime,
    shadow: colors.LabelLimeShadow,
    isChecked: false,
    name: 'lime'
  },
  {
    color: colors.LabelPink,
    shadow: colors.LabelPinkShadow,
    isChecked: false,
    name: 'pink'
  },
  {
    color: colors.LabelBlack,
    shadow: colors.LabelBlackShadow,
    isChecked: false,
    name: 'black'
  }
];

const LabelItem = ({ name, color, shadow, isChecked }) => {
  const classes = useLabelStyles({ color, shadow });
  return (
    <li className={classes.label}>
      <span>
        {name}
        {isChecked && (
          <div className={classes.iconButtonCheck}>
            <FontAwesomeIcon icon={faCheck} />
          </div>
        )}
      </span>
      <div className={classes.iconButton}>
        <FontAwesomeIcon icon={faPen} />
      </div>
    </li>
  );
};

const EditLabels = () => {
  const classes = useEditLabelsStyles();

  const renderLabelItems = () => {
    return labels.map(label => <LabelItem key={label.name} {...label} />);
  };

  return (
    <div className={classes.content}>
      <input
        className={''}
        type="text"
        placeholder="Search labels..."
        value=""
        autoComplete="off"
      />
      <label>Labels</label>
      <ul>{renderLabelItems()}</ul>
      <button>Create a new label...</button>
    </div>
  );
};

export default EditLabels;
