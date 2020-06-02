import { makeStyles } from '@material-ui/styles';

import {
  menuContentBase,
  buttonBase,
  labelBase,
  textAreaBase
} from '../../../common.styles';

const useListMenuStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase
    },

    '& textarea': {
      ...textAreaBase
    },

    '& input': {
      ...buttonBase
    }
  }
});

export default useListMenuStyles;
