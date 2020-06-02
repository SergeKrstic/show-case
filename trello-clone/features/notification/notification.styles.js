import { makeStyles } from '@material-ui/styles';

const useNotificationStyles = makeStyles({
  notification: {
    position: 'fixed',
    right: '4px',
    top: '40px',
    zIndex: '21',
    maxWidth: '270px',
    overflow: 'hidden'
  },
  notificationItem: {
    padding: '4px 8px',
    margin: '4px',
    borderRadius: '3px',
    fontWeight: 700,
    color: '#fff',
    backgroundColor: '#eb5a46',
    borderColor: '#f5d3ce'
  }
});

export default useNotificationStyles;
