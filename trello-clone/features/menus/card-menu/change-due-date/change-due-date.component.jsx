import React from 'react';
import Grid from '@material-ui/core/Grid';

import useStyles from './change-due-date.styles';

const ChangeDueDate = () => {
  const classes = useStyles();
  return (
    <div className={classes.content}>
      <Grid container spacing={1}>
        <Grid item xs={6}>
          <label>Date</label>
          <input type="text" value="" />
        </Grid>
        <Grid item xs={6}>
          <label>Time</label>
          <input type="text" value="" />
        </Grid>
      </Grid>
      Add calendar element here...
      <label>Set Reminder</label>
      <select id="reminder">
        <option value="None" selected={false}>
          None
        </option>
        <option value="At Time of Due Date" selected={false}>
          At Time of Due Date
        </option>
        <option value="5 Minutes Before" selected={false}>
          5 Minutes Before
        </option>
        <option value="10 Minutes Before" selected={false}>
          10 Minutes Before
        </option>
        <option value="15 Minutes Before" selected={false}>
          15 Minutes Before
        </option>
        <option value="1 Hour Before" selected={false}>
          1 Hour Before
        </option>
        <option value="2 Hours Before" selected={false}>
          2 Hours Before
        </option>
        <option value="1 Day Before" selected={true}>
          1 Day Before
        </option>
        <option value="2 Days Before" selected={false}>
          2 Days Before
        </option>
      </select>
      <div>
        <button className={classes.buttonSave}>Save</button>
        <button className={classes.buttonDelete}>Delete</button>
      </div>
    </div>
  );
};

export default ChangeDueDate;
