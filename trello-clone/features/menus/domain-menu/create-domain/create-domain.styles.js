import { makeStyles } from '@material-ui/styles';

import {
  menuContentBase,
  buttonBase,
  labelBase,
  textBoxBase
} from '../../../common.styles';

export default makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase
    },

    '& input': {
      ...textBoxBase
    },

    '& button': {
      ...buttonBase
    }
  }
});
