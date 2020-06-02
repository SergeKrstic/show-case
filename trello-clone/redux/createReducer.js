import produce from 'immer';

export default function createReducer(initialState, handlers) {
  return function reducer(state = initialState, action) {
    return produce(state, draft => {
      if (handlers.hasOwnProperty(action.type)) {
        handlers[action.type](draft, action);
      }
    });
  };
}
