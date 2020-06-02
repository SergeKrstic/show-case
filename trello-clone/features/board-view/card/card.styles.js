import { makeStyles } from '@material-ui/styles';

import { colors, baseFont, cardShadow } from '../../common.styles';

const useCardStyles = makeStyles({
  card: {
    ...baseFont,

    backgroundColor: colors.White,
    borderRadius: '3px',
    marginBottom: '8px',
    maxWidth: '300px',
    minHeight: '20px',
    boxShadow: cardShadow,
    alignItems: 'center',
    overflow: 'hidden',
    cursor: 'pointer',

    '&:hover': {
      '& span': {
        visibility: 'visible',

        '&:hover': {
          backgroundColor: colors.TextAreaDark,
          color: colors.FontDark,
          opacity: 1
        }
      }
    }
  },

  cardContent: {
    position: 'relative',
    padding: '6px 8px',

    '& p': {
      overflowWrap: 'break-word',
      wordWrap: 'break-word',
      margin: 0
    }
  },

  cardHeader: {
    fontSize: '12px',
    fontWeight: '600',
    backgroundColor: colors.Header,
    padding: '0px 8px'
  },

  labels: {
    display: 'block',
    overflow: 'auto',
    position: 'relative'
  },

  editButton: {
    backgroundColor: colors.BackgroundGrey,
    backgroundClip: 'padding-box',
    backgroundOrigin: 'padding-box',
    borderRadius: '3px',
    opacity: '0.8',
    padding: '4px',
    position: 'absolute',
    right: '2px',
    top: '2px',
    visibility: 'hidden',
    zIndex: 40,
    cursor: 'pointer',

    color: colors.Icon,

    height: '28px',
    fontSize: '16px',
    lineHeight: '28px',
    width: '28px',

    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',

    fontFamily: 'trellicons',
    fontStyle: 'normal',
    fontWeight: 400,
    textAlign: 'center',

    '& svg': {
      height: '20px',
      width: '20px'
    }
  },

  cardLabel: {
    height: '16px',
    lineHeight: '16px',
    padding: '0 8px',
    maxWidth: '198px',

    borderRadius: '4px',
    color: colors.White,
    display: 'block',
    overflow: 'hidden',
    position: 'relative',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap',
    '-webkit-font-smoothing': 'antialiased',

    float: 'left',
    fontSize: '12px',
    fontWeight: 700,
    margin: '0 4px 4px 0',
    minWidth: '40px',
    textShadow: 'none',
    width: 'auto',

    '& span': {
      display: 'initial',

      '&:hover': {
        color: colors.White
      }
    }
  },

  cardBadges: {
    height: '20px',
    fontSize: '16px',
    lineHeight: '20px',
    color: colors.Badge,

    '& i': {
      display: 'inline-block',

      '& svg': {
        height: '20px',
        width: '20px'
      }
    }
  }
});

export default useCardStyles;
