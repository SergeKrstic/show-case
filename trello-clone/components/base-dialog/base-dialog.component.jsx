import React from 'react';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';

import CloseIcon from '@material-ui/icons/Close';

import useStyles from './base-dialog.styles';

export default function BaseDialog({
  isOpen,
  title,
  subtitle,
  icon,
  children,
  handleClose,
  size = 'md',
  fullScreen
}) {
  const classes = useStyles();

  return (
    <Dialog
      onClose={handleClose}
      open={isOpen}
      scroll="body"
      fullScreen={fullScreen}
      fullWidth={true}
      maxWidth={size}
    >
      <DialogContent className={classes.root}>
        <div className={classes.container}>
          <div className={classes.closeButton} onClick={handleClose}>
            <CloseIcon />
          </div>
          <div className={classes.header}>
            <div className={classes.title}>
              <h2>{title}</h2>
            </div>
            <div className={classes.subtitle}>
              <p>{subtitle}</p>
            </div>
            <span>{icon}</span>
          </div>
          <div className={classes.content}>{children}</div>
        </div>
      </DialogContent>
    </Dialog>
  );
}
