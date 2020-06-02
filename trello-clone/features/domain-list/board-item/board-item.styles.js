import { makeStyles } from '@material-ui/styles';

import { colors, baseFont } from '../../common.styles';

const useBoardItemStyles = makeStyles({
  // Domain View
  // ==========================================================================

  gridItem: {
    ...baseFont,
    display: 'block',
    position: 'relative',

    margin: '8px',
    padding: '8px 12px',
    borderRadius: '3px',

    backgroundSize: 'cover',
    backgroundPosition: 'center center'
  },

  domainBoardPlaceHolder: {
    extend: 'gridItem',
    backgroundColor: colors.TransparentGreyDark,
    minHeight: '96px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',

    '&:hover': {
      cursor: 'pointer',
      backgroundColor: colors.TransparentGreyDarker
    }
  },

  domainBoardItem: {
    extend: 'gridItem',
    color: colors.White,
    backgroundColor: colors.BoardBlueDark,

    '&:hover': {
      cursor: 'pointer',
      backgroundColor: colors.BoardBlueHover
    }
  },

  domainBoardItemContent: {
    display: 'flex',
    flexDirection: 'column',
    height: '80px',
    position: 'relative',
    overflow: 'hidden'
  },

  domainBoardItemTitle: {
    fontSize: '16px',
    fontWeight: 700,
    flex: 1,
    overflow: 'hidden'
  },

  domainBoardItemSubTitle: {
    color: colors.BoardSubTitleLight,
    width: 'calc(100% - 18px)',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap'
  },

  domainBoardItemStarIcon: {
    width: '20px',
    height: '20px',
    justifyContent: 'center',
    alignItems: 'center',
    display: 'flex',
    position: 'absolute',
    bottom: '8px',
    right: '8px',
    opacity: 0.15,
    transition: 'all 0.25s',

    '&:hover': {
      fontSize: '18px',
      opacity: 0.8
    }
  },

  domainBoardItemIsStarred: {
    color: colors.Star,
    opacity: 1,

    '&:hover': {
      opacity: 1
    }
  },

  // Menu View
  // ==========================================================================
  menuBoardItem: {
    margin: '0 4px 4px 0',
    borderRadius: '3px',
    position: 'relative',
    minWidth: 0,
    lineHeight: '20px',
    cursor: 'pointer'
  },

  menuBoardItemTile: {
    display: 'flex',
    fontWeight: 700,
    height: '36px',
    overflow: 'hidden',
    position: 'relative',
    color: colors.FontDark,
    backgroundColor: colors.BoardBlueLight,

    '&:hover': {
      backgroundColor: colors.BoardBlueLightHover,

      '& $menuBoardItemThumbnail': {
        opacity: 1
      },

      '& $menuBoardItemStarIcon': {
        width: '24px',
        opacity: props => (props.isStarred ? 1 : 0.65),

        '&:hover': {
          fontSize: '18px',
          opacity: 1
        }
      }
    }
  },

  menuBoardItemThumbnail: {
    display: 'flex',
    flex: '0 0 auto',
    backgroundSize: 'cover',
    borderRadius: '3px 0 0 3px',
    height: '36px',
    width: '36px',
    backgroundColor: colors.BoardBlue,
    position: 'relative',
    opacity: 0.7
  },

  menuBoardItemTileTitle: {
    display: 'flex',
    position: 'relative',
    flex: 1,
    width: '100%',
    padding: '9px 0 9px 10px',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap',
    alignItems: 'center'
  },

  menuBoardItemTileWithDomain: {
    paddingTop: '1px',
    paddingBottom: 0,
    flexDirection: 'column',
    zIndex: 1,
    alignItems: 'flex-start'
  },

  menuBoardItemTileTitleName: {
    display: 'block',
    paddingRight: '12px',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    whiteSpace: 'nowrap'
  },

  menuBoardItemTileTitleSubName: {
    fontSize: '12px',
    fontWeight: 400,
    lineHeight: '12px',
    color: colors.BoardSubTitleDark
  },

  menuBoardItemStarIcon: {
    width: props => (props.isStarred ? '24px' : 0),
    marginRight: '4px',
    transitionDuration: '85ms',
    transitionProperty: 'width, opacity, fontSize',
    overflow: 'hidden',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    opacity: props => (props.isStarred ? 1 : 0)
  },

  menuBoardItemIsStarred: {
    color: colors.Star
  }
});

export default useBoardItemStyles;
