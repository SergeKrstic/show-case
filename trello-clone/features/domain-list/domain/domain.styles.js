import { makeStyles } from '@material-ui/styles';

const useDomainStyles = makeStyles({
  // Grid
  // ==========================================================================
  gridContainer: {
    padding: '0 0 40px'
  },

  gridContent: {
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'wrap'
  },

  // List
  // ==========================================================================
  listContainer: {
    margin: '16px 0 8px'
  },

  listContent: {
    margin: '8px 0 4px',
    overflow: 'hidden'
  }
});

export default useDomainStyles;
