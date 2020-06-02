export const colors = {
  White: '#fff',

  Success: '#5aac44',
  SuccessHighlight: '#61bd4f',

  Danger: '#cf513d',
  DangerHighlight: '#eb5a46',

  TextAreaLight: '#fafbfc',
  TextAreaDark: '#ebecf0',

  FontLight: '#5e6c84',
  FontMedium: '#3c4858',
  FontDark: '#172b4d',
  FontMuted: '#a5adba',

  ShadowBorder: '#dfe1e6',
  ShadowBorderFocus: '#0079bf',

  BackgroundGrey: '#f4f5f7', // for board menu
  BackgroundGrey2: '#ebecf0', // for list surface
  TransparentGrey: 'rgba(9, 30, 66, 0.04)',
  TransparentGreyDark: 'rgba(9, 30, 66, 0.08)',
  TransparentGreyDarker: 'rgba(9, 30, 66, 0.12)',
  TransparentGreyDarkest: 'rgba(9, 30, 66, 0.16)',
  TransparentGreyBlack: 'rgba(9, 30, 66, 0.25)',
  TransparentBlack: 'rgba(0, 0, 0, 0.08)',
  TransparentBlackDark: 'rgba(0, 0, 0, 0.16)',
  TransparentWhite: 'rgba(255, 255, 255, 0.5)',
  TransparentWhiteDark: 'rgba(255, 255, 255, 0.3)',
  TransparentWhiteDarker: 'rgba(255, 255, 255, 0.2)',

  SelectBackground: 'rgb(248, 248, 248)',
  SelectBorder: 'rgb(166, 166, 166)',

  Header: '#ddd',
  Disabled: '#888',

  Star: '#e6c60d',
  Badge: '#6b778c',
  Icon: '#42526e',
  IconDark: '#091e42',

  ScrollBarTrack: 'rgba(0, 0, 0, 0.16)',
  ScrollBarThumb: 'rgba(255, 255, 255, 0.4)',

  // Boards
  BoardBlue: '#0079bf',
  BoardBlueDark: '#0067a3',
  BoardBlueHover: '#005c91',
  BoardBlueLight: 'rgba(0, 121, 191, 0.1)',
  BoardBlueLightHover: 'rgba(0, 121, 191, 0.2)',

  BoardOrange: '#d29034',
  BoardGreen: '#519839',
  BoardRed: '#b04732',
  BoardPurple: '#89609e',
  BoardPink: '#cd5a92',
  BoardLime: '#4bbf6c',
  BoardSky: '#00adcc',
  BoardGrey: '#838c91',

  BoardSubTitleLight: 'rgba(255, 255, 255, 0.65)',
  BoardSubTitleDark: 'rgba(0, 0, 0, 0.4)',

  // Labels
  LabelGreen: '#61bd4f',
  LabelGreenShadow: '#519839',

  LabelYellow: '#f2d600',
  LabelYellowShadow: '#d9b51c',

  LabelOrange: '#ff9f1a',
  LabelOrangeShadow: '#cd8313',

  LabelRed: '#eb5a46',
  LabelRedShadow: '#b04632',

  LabelPurple: '#c377e0',
  LabelPurpleShadow: '#89609e',

  LabelBlue: '#0079bf',
  LabelBlueShadow: '#055a8c',

  LabelSky: '#00c2e0',
  LabelSkyShadow: '#0098b7',

  LabelLime: '#51e898',
  LabelLimeShadow: '#4bbf6b',

  LabelPink: '#ff78cb',
  LabelPinkShadow: '#c9558f',

  LabelBlack: '#344563',
  LabelBlackShadow: '#091e42'
};

export const dividerBorder = `1px solid ${colors.TransparentWhiteDark}`;
export const boxShadowBorder = `inset 0 0 0 2px ${colors.ShadowBorder}`;
export const boxShadowBorderFocus = `inset 0 0 0 2px ${colors.ShadowBorderFocus}`;
export const cardShadow = `0 1px 0 ${colors.TransparentGreyBlack}`;
export const menuShadow =
  `0 12px 24px -6px ${colors.TransparentGreyBlack}, ` +
  `0 0 0 1px ${colors.TransparentGreyDark}`;

export const baseFont = {
  fontFamily:
    '-apple-system,' +
    'BlinkMacSystemFont,' +
    'Segoe UI,' +
    'Roboto,' +
    'Noto Sans,' +
    'Ubuntu,' +
    'Droid Sans,' +
    'Helvetica Neue,' +
    'sans-serif',
  fontSize: '14px',
  fontWeight: 400,
  lineHeight: '20px',
  textAlign: 'left',
  color: colors.FontDark
};

export const menuBase = {
  ...baseFont,
  width: '304px',
  backgroundColor: colors.White
};

export const menuContentBase = {
  ...menuBase,
  maxHeight: '814px',
  overflowX: 'hidden',
  overflowY: 'auto',
  padding: '0 12px 12px'
};

export const labelBase = {
  margin: '4px 0',
  color: colors.FontLight,
  fontSize: '12px',
  lineHeight: '16px',
  display: 'block',
  fontWeight: 700
};

export const buttonBase = {
  ...baseFont,
  backgroundColor: colors.Success,
  boxShadow: 'none',
  border: 'none',
  color: colors.White,
  padding: '6px 24px',
  cursor: 'pointer',
  display: 'inline-block',
  margin: '8px 4px 0 0',
  textAlign: 'center',
  borderRadius: '3px',
  transitionProperty: 'background-color,border-color,box-shadow',
  transitionDuration: '85ms',
  transitionTimingFunction: 'ease',
  '&:hover': {
    backgroundColor: colors.SuccessHighlight
  }
};

export const greyButtonBase = {
  ...buttonBase,
  margin: '0 4px 4px 0',
  padding: '6px 12px',
  color: colors.FontDark,
  backgroundColor: colors.TransparentGrey,
  '&:hover': {
    backgroundColor: colors.TransparentGreyDark
  }
};

export const headerButtonBase = {
  ...buttonBase,
  backgroundColor: 'transparent',
  height: '32px',
  lineHeight: '32px',
  padding: '0 12px',
  margin: '0 8px 4px 0',
  userSelect: 'none',

  '&:hover': {
    backgroundColor: colors.TransparentBlackDark
  }
};

export const textBoxBase = {
  ...baseFont,
  display: 'block',
  margin: '4px 0 12px',
  padding: '8px 12px',
  width: '100%',
  backgroundColor: colors.TextAreaLight,
  border: 'none',
  borderRadius: '3px',
  boxShadow: boxShadowBorder,
  transitionProperty: 'background-color,border-color,box-shadow',
  transitionDuration: '85ms',
  transitionTimingFunction: 'ease',
  '&:hover': {
    backgroundColor: colors.TextAreaDark,
    border: 'none',
    boxShadow: boxShadowBorder
  },
  '&:focus': {
    background: colors.White,
    boxShadow: boxShadowBorderFocus
  }
};

export const textAreaBase = {
  ...textBoxBase,
  height: '72px',
  padding: '8px',
  resize: 'vertical',
  overflow: 'auto'
};

export const iconButton = {
  borderRadius: '3px',
  height: '32px',
  width: '32px',
  lineHeight: '32px',
  fontSize: '12px',
  cursor: 'pointer',
  color: colors.Icon,

  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',

  '&:hover': {
    color: colors.IconDark,
    backgroundColor: colors.TransparentGreyDark
  }
};

export const selectBase = {
  ...baseFont,
  width: '100%',
  marginBottom: '14px',

  '-webkit-writing-mode': 'horizontal-tb !important',
  textRendering: 'auto',
  letterSpacing: 'normal',
  wordSpacing: 'normal',
  textIndent: '0px',
  textShadow: 'none',
  display: 'inline-block',
  textAlign: 'start',
  '-webkit-appearance': 'menulist',
  boxSizing: 'border-box',
  alignItems: 'center',
  whiteSpace: 'pre',
  '-webkit-rtl-ordering': 'logical',
  backgroundColor: colors.SelectBackground,
  cursor: 'default',
  borderRadius: '5px',
  borderWidth: '1px',
  borderStyle: 'solid',
  borderColor: colors.SelectBorder,
  borderImage: 'initial'
};

export const formCloseButton = {
  height: '31px',
  width: '31px',
  fontSize: '28px',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  margin: '0 8px 0 auto',
  cursor: 'pointer',
  color: colors.FontLight,

  '&:hover': {
    color: colors.FontDark
  }
};
