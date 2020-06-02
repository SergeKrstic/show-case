import React from 'react';

import { createProvider } from 'redux/createProvider';
import * as modelActions from './redux/entities/models.actions';

import rootReducer from './redux/root.reducer';
import rootSaga from './redux/root.saga';
// import { regeneratingRootSaga as rootSaga } from './redux/root.saga';

import App from './app.container';

const ignoredActionsInDev = [
  modelActions.moveList.type,
  modelActions.moveCard.type
];
const AppProvider = createProvider(rootReducer, rootSaga, ignoredActionsInDev);

export default props => (
  <AppProvider>
    <App {...props} />
  </AppProvider>
);
