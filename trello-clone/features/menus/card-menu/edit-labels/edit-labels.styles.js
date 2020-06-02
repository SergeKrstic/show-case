import { makeStyles } from '@material-ui/styles';

import {
  colors,
  menuContentBase,
  textBoxBase,
  buttonBase,
  labelBase,
  iconButton
} from '../../../common.styles';

export const useLabelStyles = makeStyles({
  label: {
    paddingRight: '36px',
    position: 'relative',

    '& span': {
      borderRadius: '3px',
      cursor: 'pointer',
      fontWeight: 700,
      margin: '0 0 4px',
      minHeight: '32px',
      padding: '6px 12px',
      position: 'relative',
      transition: 'padding 85ms, margin 85ms, box-shadow 85ms',

      backgroundColor: props => props.color,

      color: colors.White,
      display: 'block',
      maxWidth: '100%',
      overflow: 'hidden',
      textOverflow: 'ellipsis',

      '&:hover': {
        marginLeft: '4px',
        paddingRight: '32px',
        boxShadow: props => `-8px 0 ${props.shadow}`
      }
    }
  },

  iconButton: {
    ...iconButton,
    position: 'absolute',
    top: 0,
    right: 0
  },

  iconButtonCheck: {
    extend: 'iconButton',
    color: colors.White
  }
});

export const useEditLabelsStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase,
      textTransform: 'uppercase',
      fontWeight: 500,
      margin: '16px 0 8px 0'
    },

    '& input[type=text]': {
      ...textBoxBase
    },

    '& button': {
      ...buttonBase,
      width: '100%',
      color: colors.FontDark,
      backgroundColor: colors.TransparentGrey,
      textAlign: 'center',

      '&:hover': {
        backgroundColor: colors.TransparentGreyDark
      }
    },

    '& ul': {
      listStyle: 'none',
      marginBottom: '8px',
      margin: 0,
      padding: 0
    }
  }
});

export default useEditLabelsStyles;
