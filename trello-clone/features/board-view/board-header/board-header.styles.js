import { makeStyles } from '@material-ui/styles';

import { colors, headerButtonBase } from '../../common.styles';

const useBoardHeaderStyles = makeStyles({
  boardHeaderContainer: {
    overflowX: 'scroll',
    overflowY: 'hidden',
    '-ms-overflow-style': 'none',
    '&::-webkit-scrollbar': { display: 'none' },

    whiteSpace: 'nowrap',
    padding: '8px 4px 4px 8px',
    display: 'flex',
    color: 'white',
    textDecoration: 'none'
  },

  boardHeaderName: {
    ...headerButtonBase,
    fontSize: '18px',
    fontWeight: '700'
  },

  boardHeaderButton: {
    ...headerButtonBase,
    backgroundColor: colors.TransparentBlack
  },

  boardHeaderButtonSelected: {
    ...headerButtonBase,
    backgroundColor: colors.TransparentBlackDark
  },

  boardHeaderSearchBox: {
    ...headerButtonBase,
    backgroundColor: colors.TransparentBlack,
    margin: '0 4px 4px 0',
    marginLeft: 'auto'
  },

  boardHeaderMenuButton: {
    ...headerButtonBase,
    backgroundColor: colors.TransparentBlack,
    margin: '0 4px 4px 4px'
  },

  boardHeaderMenuIcon: {
    fontSize: '12px',
    marginRight: '12px'
  },

  boardStarred: {
    color: 'yellow'
  },

  boardNotStarred: {
    color: colors.TransparentWhite
  },

  spacer: {
    paddingLeft: '1px'
  }
});

export default useBoardHeaderStyles;
