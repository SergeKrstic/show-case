export function hasNotMoved(dragResult) {
  const { destination, source } = dragResult;

  if (!destination) return true;

  if (
    destination.droppableId === source.droppableId &&
    destination.index === source.index
  ) {
    return true;
  }

  return false;
}
