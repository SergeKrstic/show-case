// Entities
import { metaTypes } from './entities/models.types';
import { createFirestoreReducer } from 'firebase/redux/firestore.reducer';

import * as firestoreActionCreators from 'firebase/redux/firestore.actions';
import * as firestoreDomainsActionCreators from './entities/domains/domains.actions';
import * as firestoreBoardsActionCreators from './entities/boards/boards.actions';
import * as firestoreListsActionCreators from './entities/lists/lists.actions';
import * as firestoreCardsActionCreators from './entities/cards/cards.actions';

import * as modelsActionCreators from './entities/models.actions';

// Session
import sessionReducer, * as sessionActionCreators from './session/session.slice';

// Views
import homeViewReducer, * as homeViewActionCreators from './views/home-view/home-view.slice';
import boardsMenuReducer, * as boardsMenuActionCreators from './views/boards-menu/boards-menu.slice';
import boardViewReducer, * as boardViewActionCreators from './views/board-view/board-view.slice';
import cardViewReducer, * as cardViewActionCreators from './views/card-view/card-view.slice';

import notificationReducer, * as notificationActionCreators from './views/notification/notification.slice';
import modalsReducer, * as modalsActionCreators from './views/modals/modals.slice';
import popOverReducer, * as popOverActionCreators from './views/pop-over/pop-over.slice';

const entitiesReducer = createFirestoreReducer(metaTypes);

export {
  // ===============================
  // Actions - entities
  firestoreActionCreators,
  firestoreDomainsActionCreators,
  firestoreBoardsActionCreators,
  firestoreListsActionCreators,
  firestoreCardsActionCreators,
  modelsActionCreators,
  // Actions - session
  sessionActionCreators,
  // Actions - view
  homeViewActionCreators,
  boardsMenuActionCreators,
  boardViewActionCreators,
  cardViewActionCreators,
  notificationActionCreators,
  modalsActionCreators,
  popOverActionCreators,
  // ===============================
  // Reducers - entities
  entitiesReducer,
  // Reducers - session
  sessionReducer,
  // Reducers - view
  homeViewReducer,
  boardsMenuReducer,
  boardViewReducer,
  cardViewReducer,
  notificationReducer,
  modalsReducer,
  popOverReducer
};
