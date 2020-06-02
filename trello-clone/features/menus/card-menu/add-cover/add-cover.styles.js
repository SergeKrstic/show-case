import { makeStyles } from '@material-ui/styles';

import {
  menuContentBase,
  greyButtonBase,
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

    '& div': {
      marginBottom: '16px',

      '& button': {
        ...greyButtonBase
      }
    }
  },

  uploadButton: {
    ...greyButtonBase,
    margin: 0,
    width: '100%'
  }
});

export default useAddCheckStyles;
