import { makeStyles } from '@material-ui/styles';

import {
  menuContentBase,
  buttonBase,
  labelBase,
  textBoxBase
} from '../../../common.styles';

const useAddCheckStyles = makeStyles({
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

export default useAddCheckStyles;
