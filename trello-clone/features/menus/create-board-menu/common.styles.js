import { colors } from '../../common.styles';

export const boardColors = [
  { name: 'blue', value: colors.BoardBlue },
  { name: 'orange', value: colors.BoardOrange },
  { name: 'green', value: colors.BoardGreen },
  { name: 'red', value: colors.BoardRed },
  { name: 'purple', value: colors.BoardPurple },
  { name: 'pink', value: colors.BoardPink },
  { name: 'lime', value: colors.BoardLime },
  { name: 'sky', value: colors.BoardSky },
  { name: 'grey', value: colors.BoardGrey }
];

export const boardImageUrls = [
  'url("https://images.unsplash.com/photo-1586696037912-43cfc1f854af?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586705576465-1a08ba1cbf03?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586596436497-8d6f8d1d921f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586399254662-c8948cd73421?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586521995568-39abaa0c2311?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586462175816-c0e709898f01?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586455122360-bf852d3d2df7?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586343785556-4c8ddf80622f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")',
  'url("https://images.unsplash.com/photo-1586294839852-650d52bb6923?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjcwNjZ9")'
];

export const boardBackgroundContainer = {
  display: 'flex',
  flexWrap: 'wrap',
  justifyContent: 'space-between',
  listStyle: 'none',
  margin: 0,
  paddingTop: '8px'
};

export const boardBackgroundItem = {
  height: '56px',
  width: 'calc(33.3% - 8px)',
  marginBottom: '12px',
  borderRadius: '3px',
  cursor: 'pointer',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center'
};
