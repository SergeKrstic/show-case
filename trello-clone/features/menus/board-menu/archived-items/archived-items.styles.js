import { makeStyles } from '@material-ui/styles';

import {
  colors,
  baseFont,
  menuBase,
  menuContentBase,
  greyButtonBase,
  textBoxBase
} from '../../../common.styles';

const useArchivedItemsStyles = makeStyles({
  container: {
    ...menuBase,
    backgroundColor: colors.BackgroundGrey
  },

  content: {
    ...menuContentBase,
    backgroundColor: colors.BackgroundGrey
  },

  controls: {
    display: 'flex',
    alignItems: 'center',
    margin: '4px 0 12px',

    '& div': {
      width: '0px', // not sure why this works
      flex: '1 1 auto',
      margin: '0 6px 0 0',

      '& input': {
        ...textBoxBase,
        margin: 0
      }
    },

    '& button': {
      ...greyButtonBase,
      margin: 0
    }
  },

  noItems: {
    display: 'block',
    borderRadius: '6px',
    padding: '24px 12px',
    textAlign: 'center',
    backgroundColor: colors.TransparentGrey
  },

  archivedItemContainer: {
    marginBottom: '8px'
  },

  archivedListContent: {
    display: 'flex',
    paddingBottom: '8px',
    alignItems: 'center',

    '& button': {
      ...greyButtonBase,
      margin: 0
    },

    '& span': {
      color: colors.FontLight,
      fontSize: '12px',
      paddingRight: '8px'
    }
  },

  archivedListTitle: {
    padding: '8px',
    margin: '0 auto 0 0'
  },

  archivedCardOptions: {
    marginBottom: '12px',
    color: colors.FontLight,
    '& button': {
      ...baseFont,
      border: 'none',
      color: colors.FontLight,
      textDecoration: 'underline',
      backgroundColor: 'transparent'
    }
  }
});

export default useArchivedItemsStyles;
