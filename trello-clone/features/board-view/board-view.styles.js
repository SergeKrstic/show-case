import React from 'react';

import { makeStyles } from '@material-ui/styles';

import { colors, baseFont } from '../common.styles';

export const boardWrapper = {
  ...baseFont
};

export const boardCanvas = {
  backgroundColor: colors.BoardBlue,

  display: 'flex',
  width: '100%',
  flexDirection: 'column',
  position: 'relative',
  flexGrow: 1
};

export const withBaseStyles = story => (
  <div style={{ ...boardWrapper }}>
    <div style={boardCanvas}>{story()}</div>
  </div>
);

const useBoardStyles = makeStyles({ boardWrapper, boardCanvas });

export default useBoardStyles;
