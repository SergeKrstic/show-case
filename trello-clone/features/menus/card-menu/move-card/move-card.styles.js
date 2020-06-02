import { makeStyles } from '@material-ui/styles';

import { menuContentBase, buttonBase, labelBase } from '../../../common.styles';

const useMoveCardStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase,
      textTransform: 'uppercase',
      fontWeight: 500,
      margin: '16px 0 8px 0'
    },

    '& input': {
      ...buttonBase
    }
  }
});

export default useMoveCardStyles;
