import { makeStyles } from '@material-ui/styles';

import { colors, headerButtonBase } from '../../common.styles';

const useSearchCardsStyles = makeStyles({
  searchBox: {
    ...headerButtonBase,
    backgroundColor: colors.TransparentBlack,
    margin: '0 4px 4px auto',
    position: 'relative'
  },

  searchBoxText: {
    margin: 0,
    zIndex: 1,
    height: '100%',
    border: 'none',
    fontSize: '13px',
    borderRadius: '3px',
    cursor: 'text',
    color: 'white',
    backgroundColor: 'transparent',
    marginRight: '20px'
  },

  searchBoxIcon: {
    position: 'absolute',
    top: 0,
    right: 0,
    width: '32px',
    fontSize: '14px'
  }
});

export default useSearchCardsStyles;
