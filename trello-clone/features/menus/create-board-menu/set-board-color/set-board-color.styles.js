import { makeStyles } from '@material-ui/styles';

import {
  boardBackgroundContainer,
  boardBackgroundItem
} from '../common.styles';
import { menuContentBase } from '../../../common.styles';

export default makeStyles({
  content: {
    ...menuContentBase,
    paddingTop: '8px'
  },

  imageContainer: {
    ...boardBackgroundContainer
  },

  image: {
    ...boardBackgroundItem
  }
});
