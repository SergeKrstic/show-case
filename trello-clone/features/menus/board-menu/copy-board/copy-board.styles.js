import { makeStyles } from '@material-ui/styles';

import {
  colors,
  baseFont,
  menuContentBase,
  buttonBase,
  labelBase,
  textBoxBase,
  selectBase,
  boxShadowBorder
} from '../../../common.styles';

const useCopyBoardStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase
    },

    '& input[type="text"]': {
      ...textBoxBase
    },

    '& select': {
      ...selectBase
    },

    '& button': {
      ...buttonBase
    }
  },

  // Todo: complete styling this checkbox
  checkbox: {
    ...baseFont,
    marginTop: '10px',
    position: 'relative',
    margin: '8px 6px',
    paddingLeft: '34px',
    minHeight: '18px',

    '& input[type="checkbox"]': {
      height: '18px',
      width: '18px',
      position: 'absolute',
      opacity: 1,
      // opacity: 0,
      top: 0,
      left: 0,
      display: 'inline',
      '-webkit-appearance': 'checkbox',
      marginRight: '4px'
    },

    '& label': {
      ...baseFont,
      lineHeight: '18px',

      '&::before': {
        content: '',
        borderRadius: '2px',
        boxSizing: 'border-box',
        lineHeight: '18px',
        overflow: 'hidden',
        textIndent: 0,
        height: '18px',
        width: '18px',
        whiteSpace: 'nowrap',
        backgroundColor: colors.BoardBlue,
        boxShadow: boxShadowBorder,
        position: 'absolute',
        left: 0,
        textAlign: 'center',
        top: '2px',
        margin: 0
      },

      '&::after': {
        height: '18px',
        lineHeight: '18px',
        width: '18px',
        opacity: 1,
        color: colors.White
      }
    }
  }
});

export default useCopyBoardStyles;
