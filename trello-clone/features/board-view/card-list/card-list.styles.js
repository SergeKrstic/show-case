import { makeStyles } from '@material-ui/styles';

import { colors } from '../../common.styles';

const useCardListStyles = makeStyles({
  cardList: {
    flexGrow: 1,
    margin: '0 4px',
    padding: '0 4px',
    minHeight: '20px',

    // Todo: setting overflow breaks card dragging on the iPhone ?!?
    overflowY: 'auto',
    overflowX: 'hidden',

    '&::-webkit-scrollbar': {
      height: '8px',
      width: '8px',
      backgroundColor: colors.TransparentGreyDark,
      borderRadius: '4px'
    },

    '&::-webkit-scrollbar-thumb': {
      borderRadius: '4px',
      backgroundColor: colors.TransparentGreyDarkest
    }
  }
});

export default useCardListStyles;
