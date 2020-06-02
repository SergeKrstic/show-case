import { makeStyles } from '@material-ui/styles';

import { colors, baseFont } from '../../features/common.styles';

export const useBaseDialogStyles = makeStyles({
  root: {
    margin: 0,
    padding: 0,
    backgroundColor: colors.BackgroundGrey,
    borderRadius: '2px'
  },

  container: {
    ...baseFont,
    display: 'flex',
    flexDirection: 'column',
    color: colors.FontMedium
  },

  header: {
    margin: '0px 40px 8px 56px',
    minHeight: '32px',
    '& span': {
      display: 'inline-block',
      position: 'absolute',
      top: '20px',
      left: '20px',
      width: '32px',
      height: '32px'
    }
  },

  title: {
    margin: 0,

    '& h2': {
      fontFamily: 'inherit',
      fontWeight: '600',
      margin: '0 0 8px',
      fontSize: '20px',
      lineHeight: '24px'
    }
  },

  closeButton: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    color: colors.FontMedium,
    borderRadius: '50%',
    position: 'absolute',
    top: 0,
    right: 0,
    height: '40px',
    overflow: 'hidden',
    padding: '4px',
    margin: '4px',
    transition: 'background-color 85ms,color 85ms',
    fontSize: '20px',
    lineHeight: '32px',
    width: '40px',

    '&:hover': {
      backgroundColor: colors.TransparentGreyDark,
      cursor: 'pointer'
    }
  },

  content: {
    display: 'flex',
    padding: '0 16px 16px 16px'
  }
});

export default useBaseDialogStyles;
