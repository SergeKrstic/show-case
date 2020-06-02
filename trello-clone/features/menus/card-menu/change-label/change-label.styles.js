import { makeStyles } from '@material-ui/styles';

import {
  colors,
  menuContentBase,
  textBoxBase,
  buttonBase,
  labelBase
} from '../../../common.styles';

export const useLabelStyles = makeStyles({
  label: {
    cursor: 'pointer',
    float: 'left',
    height: '32px',
    margin: '0 8px 8px 0',
    padding: 0,
    width: '48px',
    borderRadius: '4px',

    color: colors.White,
    backgroundColor: props => props.color,

    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
  }
});

export const useChangeLabelStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase,
      fontWeight: 700,
      margin: '16px 0 8px 0'
    },

    '& input[type=text]': {
      ...textBoxBase
    }
  },

  clearFix: {
    clear: 'both',
    content: '',
    display: 'table'
  },

  noColorSection: {
    extend: 'clearFix',
    display: 'flex',

    '& div:nth-child(1)': {
      flex: '0 0',
      display: 'block'
    },

    '& div:nth-child(2)': {
      flex: '1 0',
      display: 'block',

      '& p:nth-child(1)': {
        margin: 0,
        padding: 0
      },

      '& p:nth-child(2)': {
        color: colors.FontLight,
        margin: 0,
        padding: 0
      }
    }
  },

  buttonSave: {
    ...buttonBase
  },

  buttonDelete: {
    ...buttonBase,
    backgroundColor: colors.Danger,
    float: 'right',

    '&:hover': {
      backgroundColor: colors.DangerHighlight
    }
  }
});

export default useChangeLabelStyles;
