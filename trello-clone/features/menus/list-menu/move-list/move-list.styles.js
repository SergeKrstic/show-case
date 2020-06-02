import { makeStyles } from '@material-ui/styles';

import { menuContentBase, buttonBase } from '../../../common.styles';

const useListMenuStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& input': {
      ...buttonBase
    }
  }
});

export default useListMenuStyles;
