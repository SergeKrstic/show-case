import { makeStyles } from '@material-ui/styles';

import { colors, dividerBorder } from '../../common.styles';

const useHeaderStyles = makeStyles({
  header: {
    height: '40px',
    overflowX: 'scroll',
    overflowY: 'hidden',
    '-ms-overflow-style': 'none',
    '&::-webkit-scrollbar': { display: 'none' },

    whiteSpace: 'nowrap',
    userSelect: 'none',
    padding: '4px 8px',
    display: 'flex',
    color: 'white',
    textDecoration: 'none',
    // backgroundColor: colors.TransparentGreyDarkest
    backgroundColor: colors.TransparentGreyBlack
  },

  divider: {
    padding: '4px 12px 4px 0',
    margin: '4px 0 4px 4px',
    borderLeft: dividerBorder
  },

  spacer: {
    paddingLeft: '1px'
  }
});

export default useHeaderStyles;
