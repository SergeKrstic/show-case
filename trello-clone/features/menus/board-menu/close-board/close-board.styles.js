import { makeStyles } from '@material-ui/styles';

import { colors, menuContentBase, buttonBase } from '../../../common.styles';

const useCloseBoardStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& p': {
      margin: '0 0 8px'
    },

    '& input': {
      ...buttonBase,
      width: '100%',
      backgroundColor: colors.Danger,

      '&:hover': {
        backgroundColor: colors.DangerHighlight
      }
    }
  }
});

export default useCloseBoardStyles;
