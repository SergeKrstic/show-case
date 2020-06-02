import React from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faRedoAlt } from '@fortawesome/free-solid-svg-icons';

import ArchiveIcon1 from '@material-ui/icons/DeleteOutline';
// import ArchiveIcon2 from '@material-ui/icons/RestoreFromTrash';
// import ArchiveIcon3 from '@material-ui/icons/RestoreFromTrashOutlined';
// import ArchiveIcon4 from '@material-ui/icons/Restore';

import BaseDialog from '../../../../components/base-dialog/base-dialog.component';

import useStyles from './closed-boards-dialog.styles';

const archivedBoards = [
  { id: 'board-01', name: 'Project Board 1', domainName: 'Domain 1' },
  { id: 'board-02', name: 'Project Board 2', domainName: 'Domain 1' },
  { id: 'board-03', name: 'Project Board 3', domainName: 'Domain 1' },
  { id: 'board-04', name: 'Project Board 4', domainName: 'Domain 2' },
  { id: 'board-05', name: 'Project Board 5', domainName: 'Domain 2' },
  { id: 'board-06', name: 'Project Board 6', domainName: 'Domain 2' }
];

const ArchivedBoard = ({ name, domainName }) => {
  const classes = useStyles();
  return (
    <div className={classes.boardItem}>
      <div className={classes.boardTitle}>
        <div className={classes.boardName}>{name}</div>
        <div className={classes.domainName}>{domainName}</div>
      </div>
      <button className={classes.reopenButton}>
        <span>
          <FontAwesomeIcon flip="horizontal" icon={faRedoAlt} />
        </span>
        Re-open
      </button>
      <button className={classes.deleteButton}>Delete</button>
    </div>
  );
};

export default function ClosedBoardsDialog({ isOpen }) {
  const classes = useStyles();

  const handleClose = () => {};

  const renderArchivedBoards = () => {
    return archivedBoards.map(board => (
      <ArchivedBoard
        key={board.id}
        name={board.name}
        domainName={board.domainName}
      />
    ));
  };

  return (
    <BaseDialog
      onClose={handleClose}
      isOpen={isOpen}
      title="Dialog Title"
      icon={<ArchiveIcon1 />}
      size="sm"
    >
      <div className={classes.content}>{renderArchivedBoards()}</div>
    </BaseDialog>
  );
}
