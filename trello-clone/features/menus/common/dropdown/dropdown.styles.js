import { makeStyles } from '@material-ui/styles';

import { colors, baseFont } from '../../../common.styles';

const useDropDownStyles = makeStyles({
  dropdown: {
    display: 'flex',
    flexWrap: 'wrap',

    '& div': {
      width: '100%',
      height: '48px',
      margin: '0 0 8px',
      backgroundColor: colors.TransparentGrey,
      borderRadius: '3px',
      position: 'relative',
      cursor: 'pointer',
      padding: '6px 12px',
      textOverflow: 'ellipsis',

      transitionProperty: 'background-color,border-color,box-shadow',
      transitionDuration: '85ms',
      transitionTimingFunction: 'ease',

      '&:hover': {
        backgroundColor: colors.TransparentGreyDark
      }
    },

    '& select': {
      ...baseFont,
      border: 'none',
      cursor: 'pointer',
      height: '50px',
      position: 'absolute',
      top: 0,
      left: 0,
      margin: 0,
      opacity: 0,
      zIndex: 2,
      width: '100%',
      maxHeight: '300px',
      color: colors.FontDark,
      borderRadius: '3px',
      display: 'inline-block'
    }
  },

  label: {
    display: 'block',
    fontSize: '12px',
    lineHeight: '16px',
    color: colors.FontLight
  },

  value: {
    display: 'block',
    fontSize: '14px',
    lineHeight: '20px',
    overflow: 'hidden',
    textOverflow: 'ellipsis'
  }
});

export default useDropDownStyles;
