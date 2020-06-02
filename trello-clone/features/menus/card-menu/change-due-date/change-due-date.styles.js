import { makeStyles } from '@material-ui/styles';

import {
  colors,
  menuContentBase,
  textBoxBase,
  buttonBase,
  labelBase
} from '../../../common.styles';

export const useChangeDueDateStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase,
      fontWeight: 700,
      margin: '16px 0 8px 0'
    },

    '& input[type=text]': {
      ...textBoxBase
    }
  },

  buttonSave: {
    ...buttonBase
  },

  buttonDelete: {
    ...buttonBase,
    backgroundColor: colors.Danger,
    float: 'right',

    '&:hover': {
      backgroundColor: colors.DangerHighlight
    }
  }
});

export default useChangeDueDateStyles;
