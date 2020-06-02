import { makeStyles } from '@material-ui/styles';

import {
  colors,
  menuBase,
  menuContentBase,
  greyButtonBase,
  labelBase,
  textBoxBase
} from '../../../common.styles';

const useAddAttachmentStyles = makeStyles({
  container: {
    ...menuBase,
    backgroundColor: colors.White
  },

  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase
    },

    '& input': {
      ...textBoxBase
    },

    '& button': {
      ...greyButtonBase,
      margin: 0
    }
  }
});

export default useAddAttachmentStyles;
