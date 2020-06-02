import { makeStyles } from '@material-ui/styles';

import { colors, menuShadow, textBoxBase } from '../../common.styles';

const useBoardsMenuStyles = makeStyles({
  container: {
    background: 'transparent',
    position: 'absolute',
    top: '44px',
    bottom: 'auto',
    maxHeight: 'calc(100% - 48px)',

    width: '280px',
    zIndex: 20,
    display: 'flex',
    flexDirection: 'column',

    '&:focus': {
      outline: 'none'
    }
  },

  boardsMenu: {
    background: '#fff',
    boxShadow: menuShadow,
    borderRadius: '3px',
    display: 'flex',
    overflow: 'hidden',
    flex: 1
  },

  boardsMenuContent: {
    margin: '8px 4px 8px 8px',
    overflowX: 'hidden',
    overflowY: 'auto',
    flex: 1,
    display: 'block',

    width: '100%',

    '&::-webkit-scrollbar': {
      display: 'block',
      height: '8',
      width: '8px',
      backgroundColor: colors.TransparentGreyDark,
      borderRadius: '4px'
    },

    '&::-webkit-scrollbar-thumb': {
      borderRadius: '4px',
      backgroundColor: colors.TransparentGreyDarkest
    }
  },

  boardsMenuContentSearch: {
    display: 'block',
    paddingRight: '4px',

    '& input': {
      ...textBoxBase
    }
  }
});

export default useBoardsMenuStyles;
