import { makeStyles } from '@material-ui/styles';

import { colors, menuContentBase, textBoxBase } from '../../../common.styles';

import {
  boardBackgroundContainer,
  boardBackgroundItem
} from '../common.styles';

export default makeStyles({
  content: {
    ...menuContentBase
  },

  search: {
    position: 'sticky',
    top: 0,
    zIndex: 3,
    paddingBottom: '8px',
    backgroundColor: colors.White,
    display: 'flex',

    '& input': {
      ...textBoxBase,
      margin: 0,
      paddingLeft: '32px',
      flex: 'auto'
    },

    '& div': {
      position: 'absolute',
      left: '12px',
      top: '8px',
      fontSize: '12px',
      color: colors.FontLight
    }
  },

  imageContainer: {
    ...boardBackgroundContainer,
    paddingTop: '8px'
  },

  image: {
    ...boardBackgroundItem,
    backgroundPosition: '50%',
    backgroundSize: 'cover',
    cursor: 'pointer'
  }
});
