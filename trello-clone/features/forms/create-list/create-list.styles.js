import { makeStyles } from '@material-ui/styles';

import {
  baseFont,
  colors,
  buttonBase,
  textBoxBase,
  formCloseButton
} from '../../common.styles';

const useCreateCardStyles = makeStyles({
  container: {
    ...baseFont,

    width: '272px',
    margin: '0 4px',
    height: '100%',
    boxSizing: 'border-box',
    display: 'inline-block',
    verticalAlign: 'top',
    whiteSpace: 'nowrap',

    backgroundColor: colors.BackgroundGrey2,
    borderRadius: '3px',
    minHeight: '32px',
    padding: '4px',
    transition:
      'background 85ms ease-in,opacity 40ms ease-in,border-color 85ms ease-in'
  },

  cardTitle: {
    ...baseFont,
    ...textBoxBase,
    margin: 0
  },

  controls: {
    display: 'flex',
    alignItems: 'center',
    marginTop: '8px'
  },

  submitButton: {
    ...buttonBase,
    margin: 0
  },

  closeButton: {
    ...formCloseButton
  }
});

export default useCreateCardStyles;
