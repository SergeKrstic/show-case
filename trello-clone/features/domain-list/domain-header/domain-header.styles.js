import { makeStyles } from '@material-ui/styles';

import { colors, baseFont } from '../../common.styles';

const useDomainHeaderStyles = makeStyles({
  // Grid header
  // ==========================================================================
  gridHeaderContainer: {
    ...baseFont,
    display: 'flex',
    alignItems: 'center',

    '& h3': {
      display: 'inline-block',
      lineHeight: '24px',
      margin: 0,
      fontSize: '16px',
      fontWeight: 700,
      flex: 1,
      overflow: 'hidden',
      textOverflow: 'ellipsis',
      whiteSpace: 'nowrap'
    }
  },

  gridHeaderIconContainer: {
    padding: '0 8px'
  },

  gridHeaderIcon: {
    color: colors.Icon,
    width: '32px',
    height: '32px',
    lineHeight: '32px',
    fontSize: '24px'
  },

  gridHeaderSettings: {
    display: 'inline-block',
    backgroundColor: colors.TransparentGreyDark,
    margin: '0 8px 8px 8px',
    padding: '6px 12px 6px 6px',
    borderRadius: '3px',

    '&:hover': {
      cursor: 'pointer',
      backgroundColor: colors.TransparentGreyDarker
    }
  },

  gridHeaderSettingsIcon: {
    marginRight: '6px',
    marginLeft: '3px',
    color: colors.Icon,
    fontSize: '16px',
    lineHeight: '20px',
    width: '20px'
  },

  // List header
  // ==========================================================================
  listHeaderContainer: {
    display: 'flex',
    minHeight: '20px',
    position: 'relative',
    color: colors.FontLight,
    fontSize: '12px',
    fontWeight: 500,
    letterSpacing: '0.04em',
    textTransform: 'uppercase',
    lineHeight: '19px',
    margin: '0 4px 0 8px',
    alignItems: 'center'
  },

  listHeaderIcon: {
    height: '20px',
    width: '20px',
    marginRight: '8px',
    fontSize: '16px',
    lineHeight: '20px'
  },

  listHeaderTitle: {
    marginRight: 'auto'
  },

  listHeaderButton: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: '3px',
    height: '32px',
    width: '32px',
    fontSize: '16px',
    fontWeight: 400,

    '&:hover': {
      backgroundColor: colors.TransparentGreyDark,
      cursor: 'pointer'
    }
  }
});

export default useDomainHeaderStyles;
