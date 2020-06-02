import { makeStyles } from '@material-ui/styles';

import { colors, buttonBase, greyButtonBase } from '../../../common.styles';

export const useClosedBoardStyles = makeStyles({
  content: {
    flexGrow: 1
  },

  boardItem: {
    alignItems: 'center',
    borderBottom: '1px solid rgba(9,30,66,.13)',
    display: 'flex',
    flexDirection: 'row',
    padding: '8px 0'
  },

  boardTitle: {
    margin: '0 8px',
    flex: 1
  },

  boardName: {
    color: colors.FontDark
  },

  domainName: {
    color: colors.FontLight
  },

  reopenButton: {
    ...greyButtonBase,
    margin: 0,
    '& span': {
      color: colors.FontLight,
      fontSize: '12px',
      paddingRight: '8px'
    }
  },

  deleteButton: {
    ...buttonBase,
    padding: '6px 24px',
    margin: '0 0 0 4px',
    backgroundColor: colors.Danger,
    '&:hover': {
      backgroundColor: colors.DangerHighlight
    }
  }
});

export default useClosedBoardStyles;
