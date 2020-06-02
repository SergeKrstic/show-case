import { makeStyles } from '@material-ui/styles';

const useHomeViewStyles = makeStyles({
  homeView: {
    maxWidth: '900px',
    margin: 'auto',
    display: 'flex',
    flexDirection: 'column',
    flexGrow: 1
  },
  container: {
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'wrap'
  }
});

export default useHomeViewStyles;
