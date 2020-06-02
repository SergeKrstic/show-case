import { makeStyles } from '@material-ui/styles';

import { colors } from '../common.styles';

const useDomainListStyles = makeStyles({
  domainButton: {
    color: colors.FontDark,
    backgroundColor: colors.TransparentGreyDark,
    margin: '8px 8px 16px 8px',
    padding: '6px 12px 6px 6px',
    borderRadius: '3px',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    fontWeight: 400,

    '&:hover': {
      cursor: 'pointer',
      backgroundColor: colors.TransparentGreyDarker
    }
  }
});

export default useDomainListStyles;
