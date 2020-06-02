import { makeStyles } from '@material-ui/styles';

import {
  boardBackgroundContainer,
  boardBackgroundItem
} from '../common.styles';

import {
  colors,
  labelBase,
  textBoxBase,
  menuContentBase,
  buttonBase,
  selectBase
} from '../../../common.styles';

export default makeStyles({
  content: {
    ...menuContentBase,
    paddingTop: '8px',

    '& label': {
      ...labelBase
    },

    '& input': {
      ...textBoxBase
    },

    '& select': {
      ...selectBase
    },

    '& button': {
      ...buttonBase
    }
  },

  imageContainer: {
    ...boardBackgroundContainer,
    paddingTop: '8px'
  },

  boardColor: {
    ...boardBackgroundItem
  },

  boardImage: {
    ...boardBackgroundItem,
    backgroundPosition: '50%',
    backgroundSize: 'cover',
    cursor: 'pointer'
  },

  moreBackgrounds: {
    extend: 'boardColor',
    backgroundColor: colors.TransparentGrey,

    '&:hover': {
      backgroundColor: colors.TransparentGreyDark
    }
  }
});
