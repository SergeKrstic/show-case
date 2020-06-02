import { makeStyles } from '@material-ui/styles';

import { baseFont, colors, menuBase } from '../../../common.styles';

const useMenuStyles = makeStyles({
  container: {
    ...menuBase
  },

  header: {
    ...baseFont,
    display: 'flex',
    color: colors.FontLight,
    position: 'relative',
    height: '24px',
    alignItems: 'center'
  },

  title: {
    margin: '0 auto'
  },

  buttonBase: {
    width: '24px',
    height: '24px',
    position: 'absolute',
    top: 0,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-around',
    cursor: 'pointer',

    '&:hover': {
      color: colors.FontDark
    }
  },

  backButton: {
    extend: 'buttonBase',
    margin: '0 0 0 8px',
    left: 0
  },

  closeButton: {
    extend: 'buttonBase',
    margin: '0 8px 0 0',
    right: 0
  },

  divider: {
    margin: '8px'
  },

  menuItem: {
    ...baseFont
  }
});

export default useMenuStyles;
