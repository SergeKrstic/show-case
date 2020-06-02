import { makeStyles } from '@material-ui/styles';

import { colors } from '../../common.styles';

const useListStyles = makeStyles({
  list: {
    width: '272px',
    height: '100%',
    display: 'inline-block',
    verticalAlign: 'top'
  },

  listContent: {
    backgroundColor: colors.BackgroundGrey2,
    borderRadius: '3px',
    display: 'flex',
    flexDirection: 'column',
    maxHeight: '100%',
    margin: '0 4px'
  },

  listContentHeader: {
    display: 'flex',
    color: colors.FontDark,
    cursor: 'pointer',
    '& h2': {
      width: '220px',
      padding: '10px 14px',
      fontSize: '14px',
      fontWeight: 600,
      margin: '0 0'
    }
  },

  listContentHeaderMenu: {
    height: '30px',
    width: '30px',
    margin: '6px 6px 6px auto',
    borderRadius: '3px',
    fontSize: '12px',
    color: colors.FontLight,

    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-around',

    '&:hover': {
      backgroundColor: colors.TransparentGreyDark,
      color: colors.FontMedium
    }
  },

  listContentFooter: {
    display: 'block',
    marginBottom: '4px'
  },

  addCard: {
    display: 'flex'
  },

  addCardContent: {
    borderRadius: '3px',
    flex: '1 0 auto',
    display: 'block',
    color: colors.FontLight,
    margin: '2px 8px 4px',
    padding: '6px 8px',
    cursor: 'pointer',
    '&:hover': {
      background: colors.TransparentGreyDark,
      color: colors.FontDark
    }
  },

  addIcon: {
    marginRight: '6px'
  }
});

export default useListStyles;
