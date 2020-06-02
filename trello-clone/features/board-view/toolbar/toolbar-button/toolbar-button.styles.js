import { makeStyles } from '@material-ui/styles';

import { colors } from '../../../common.styles';

export const headerButtonContainer = {
  height: '48px',
  overflow: 'auto',
  overflowX: 'scroll',
  overflowY: 'hidden',
  whiteSpace: 'nowrap',
  userSelect: 'none',
  padding: '8px',
  display: 'flex',
  color: 'white',
  textDecoration: 'none',
  backgroundColor: colors.BoardBlue
};

const useHeaderButtonStyles = makeStyles({
  headerButtonContainer: headerButtonContainer,

  headerButton: {
    borderRadius: '3px',
    height: '32px',
    lineHeight: '32px',
    padding: '0 12px',
    margin: '0 8px 0 0',
    color: 'white',
    userSelect: 'none',
    transition: '.1s ease',
    fontWeight: props => (props.isBold ? 700 : 400),
    backgroundColor: props => {
      if (props.isDark)
        return props.isSelected
          ? colors.TransparentBlackDark
          : colors.TransparentBlack;
      else
        return props.isSelected
          ? colors.TransparentWhiteDarker
          : colors.TransparentWhiteDark;
    },

    '&:hover': {
      backgroundColor: props =>
        props.isDark
          ? colors.TransparentBlackDark
          : colors.TransparentWhiteDarker,
      cursor: 'pointer'
    }
  },

  headerButtonIcon: {
    fontSize: props => (props.iconType === 'fa' ? '15px' : '20px'),
    marginRight: props => (props.text ? '12px' : ''),
    position: props => (props.iconType === 'mui' ? 'relative' : ''),
    top: props => (props.iconType === 'mui' ? '5px' : ''),

    '-o-transform': props => (props.isFlippedY ? 'scaleY(-1)' : ''),
    '-moz-transform': props => (props.isFlippedY ? 'scaleY(-1)' : ''),
    '-webkit-transform': props => (props.isFlippedY ? 'scaleY(-1)' : ''),
    '-ms-transform': props => (props.isFlippedY ? 'scaleY(-1)' : ''),
    transform: props => (props.isFlippedY ? 'scaleY(-1)' : '')
  }
});

export default useHeaderButtonStyles;
