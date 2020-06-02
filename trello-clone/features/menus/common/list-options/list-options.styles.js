import { makeStyles } from '@material-ui/styles';

import { baseFont, colors, menuBase } from '../../../common.styles';

const useListMenuStyles = makeStyles({
  content: {
    ...menuBase
  },

  divider: {
    margin: '8px'
  },

  menuItem: {
    ...baseFont
  },

  muted: {
    backgroundColor: colors.White,
    color: colors.FontMuted,

    '&:hover': {
      backgroundColor: colors.White,
      cursor: 'default'
    }
  }
});

export default useListMenuStyles;
