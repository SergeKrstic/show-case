import { makeStyles } from '@material-ui/styles';

import { colors, baseFont, boxShadowBorderFocus } from '../../common.styles';

const useUpdateListNameStyles = makeStyles({
  updateListNameForm: {
    width: '222px',
    padding: '5px 0px 6px 8px',
    margin: 0,

    '&:focus': {
      outline: 'none'
    }
  },

  updateListNameFormText: {
    ...baseFont,
    fontWeight: 600,

    transition: 'background 85ms ease-in, border-color 85ms ease-in',
    background: '0 0',
    resize: 'none',
    border: 'none',
    borderRadius: '3px',
    boxShadow: 'none',
    overflow: 'hidden',
    wordWrap: 'break-word',
    height: '100%',
    width: '100%',
    padding: '6px 6px',

    '&:focus': {
      outline: 'none',
      background: colors.White,
      boxShadow: boxShadowBorderFocus
    }
  }
});

export default useUpdateListNameStyles;
