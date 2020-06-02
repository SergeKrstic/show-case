import React from 'react';
import { Draggable } from 'react-beautiful-dnd';

import List from './list.component';

const ListDraggable = ({ index, list, ...rest }) => {
  if (!list) return null;
  return (
    <Draggable draggableId={list.id} index={index}>
      {provided => (
        <div ref={provided.innerRef} {...provided.draggableProps}>
          <List
            {...rest}
            list={list}
            index={index}
            dragHandleProps={provided.dragHandleProps}
          />
        </div>
      )}
    </Draggable>
  );
};

ListDraggable.propTypes = List.propTypes;

export default ListDraggable;
