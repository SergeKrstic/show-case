import { makeStyles } from '@material-ui/styles';

import { colors, baseFont } from '../../common.styles';

const useBoardStyles = makeStyles({
  board: {
    ...baseFont,
    display: 'flex',

    userSelect: 'none',
    overflowX: 'auto',
    // overflowX: 'visible',
    // overflowX: 'hidden',
    overflowY: 'hidden',
    padding: '0 4px 8px',
    marginBottom: '8px',
    flex: '1',

    '&::-webkit-scrollbar': {
      height: '12px',
      width: '12px',
      backgroundColor: colors.ScrollBarTrack,
      borderRadius: '4px'
    },

    '&::-webkit-scrollbar-thumb': {
      borderRadius: '4px',
      backgroundColor: colors.ScrollBarThumb
    }
  },

  addList: {
    background: colors.TransparentBlack,
    cursor: 'pointer',
    borderRadius: '3px',
    height: 'auto',
    minHeight: '32px',
    padding: '4px',

    width: '272px',
    margin: '0 8px 0 4px',
    display: 'inline-block',
    whiteSpace: 'nowrap',
    verticalAlign: 'top',

    '&:hover': {
      background: colors.TransparentBlackDark
    },

    '& span': {
      display: 'block',
      padding: '6px 8px',
      color: colors.White
    }
  },

  addIcon: {
    marginRight: '6px'
  }
});

export default useBoardStyles;
