import { makeStyles } from '@material-ui/styles';

import { menuContentBase } from '../../../common.styles';

const useChangeSettingsStyles = makeStyles({
  content: {
    ...menuContentBase,

    '& p': {
      margin: '0 0 8px'
    }
  }
});

export default useChangeSettingsStyles;
