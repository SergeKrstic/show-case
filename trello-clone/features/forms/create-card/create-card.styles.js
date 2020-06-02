import { makeStyles } from '@material-ui/styles';

import {
  baseFont,
  colors,
  buttonBase,
  cardShadow,
  formCloseButton
} from '../../common.styles';

const useCreateCardStyles = makeStyles({
  container: {
    width: '100%',
    margin: 0,
    paddingBottom: '4px',

    '&:focus': {
      outline: 'none'
    }
  },

  cardTitle: {
    ...baseFont,
    width: '100%',
    backgroundColor: colors.White,
    border: 0,
    boxShadow: cardShadow,
    borderRadius: '3px',
    marginBottom: '6px',
    maxWidth: '300px',
    minHeight: '66px',
    alignItems: 'center',
    resize: 'none',
    padding: '8px',
    wordWrap: 'break-word',
    display: 'block',

    '&:focus': {
      outline: 'none'
    }
  },

  controls: {
    display: 'flex',
    alignItems: 'center',
    marginTop: '8px'
  },

  submitButton: {
    ...buttonBase,
    margin: 0,
    fontWeight: 700,
    cursor: props => (props.hasText ? 'pointer' : 'not-allowed'),
    background: props => (props.hasText ? colors.Success : colors.Disabled),
    '&:hover': {
      background: props =>
        props.hasText ? colors.SuccessHighlight : colors.Disabled
    }
  },

  closeButton: {
    ...formCloseButton
  }
});

export default useCreateCardStyles;
