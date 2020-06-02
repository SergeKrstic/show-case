import { makeStyles } from '@material-ui/styles';

import {
  baseFont,
  menuContentBase,
  buttonBase,
  labelBase,
  selectBase
} from '../../../common.styles';

const useCopyCardStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& label': {
      ...labelBase
    },

    '& select': {
      ...selectBase
    }
  },
  changeButton: {
    ...buttonBase
  },
  createDomainButton: {
    ...baseFont,
    border: 'none',
    padding: 0,
    margin: 0,
    float: 'right',
    marginTop: '17px',
    cursor: 'pointer',
    textDecoration: 'underline'
  }
});

export default useCopyCardStyles;
