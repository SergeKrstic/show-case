import localForage from 'localforage';
import { reducer as formReducer } from 'redux-form';
import { combineReducers } from 'redux';
import { persistReducer } from 'redux-persist';
import errorReducer from 'redux/error/error.slice';
// import { routerReducer } from 'react-router-redux';

import {
  // entities reducers
  entitiesReducer,
  // session reducers
  sessionReducer,
  // views reducer
  homeViewReducer,
  boardsMenuReducer,
  boardViewReducer,
  cardViewReducer,
  notificationReducer,
  modalsReducer,
  popOverReducer
} from './index.js';

export const viewsReducer = combineReducers({
  homeView: homeViewReducer,
  boardsMenu: boardsMenuReducer,
  boardView: boardViewReducer,
  cardView: cardViewReducer,
  notification: notificationReducer,
  modals: modalsReducer,
  popOver: popOverReducer

  // routing: routerReducer
});

const rootReducer = combineReducers({
  entities: entitiesReducer,
  error: errorReducer,
  session: sessionReducer,
  form: formReducer,
  views: viewsReducer
});

const persistConfig = {
  key: 'trello-clone',
  storage: localForage
};

export default persistReducer(persistConfig, rootReducer);
