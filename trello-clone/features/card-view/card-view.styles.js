import { makeStyles } from '@material-ui/styles';

import { colors, greyButtonBase } from '../common.styles';

const useCardViewStyles = makeStyles({
  cardPanels: {
    display: 'flex',
    flexGrow: 1,

    '& p': {
      margin: '0 0 8px'
    },

    '& h2, h3, h4, h5, h6': {
      fontFamily: 'inherit',
      fontWeight: '600',
      margin: '0 0 8px'
    },

    '& h3, h4, h5, h6': {
      fontSize: '16px',
      lineHeight: '20px'
    }
  },

  cardContentPanel: {
    flexGrow: 1,
    padding: '0 8px 0px 0px'
  },

  moduleTitle: {
    padding: '8px 0',
    position: 'relative',
    margin: '0 0 4px 40px',
    display: 'flex',
    alignItems: 'center',
    minHeight: '32px',

    '& span': {
      display: 'inline-block',
      position: 'absolute',
      top: '6px',
      left: '-36px',
      width: '32px',
      height: '32px'
    }
  },

  editor: {
    marginLeft: '40px',

    '& textarea': {
      fontFamily: 'inherit',
      fontSize: 'inherit',
      height: '1000px',
      color: colors.FontDark
    }
  },

  cardSidebarPanel: {
    display: 'flex',
    flexDirection: 'column',
    minWidth: '168px',
    padding: '0 0px 0px 8px',
    color: colors.FontLight,

    '& h5': {
      fontSize: '12px',
      fontWeight: '500',
      letterSpacing: '0.48px',
      textTransform: 'uppercase',
      lineHeight: '20px',
      marginTop: '16px',
      marginBottom: '-4px'
    },

    '& button': {
      ...greyButtonBase,
      display: 'block',
      height: '32px',
      margin: '8px 0 0 0',
      maxWidth: '300px',
      overflow: 'hidden',
      position: 'relative',
      textDecoration: 'none',
      textOverflow: 'ellipsis',
      whiteSpace: 'nowrap'
    }
  }
});

export default useCardViewStyles;
