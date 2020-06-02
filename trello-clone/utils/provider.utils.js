import React from 'react';
import { Provider } from 'react-redux';
import createSagaMiddleware from 'redux-saga';
import thunkMiddleware from 'redux-thunk';
import { createLogger } from 'redux-logger';
import { createStore, applyMiddleware } from 'redux';

import { DndProvider } from 'react-dnd';
import HTML5Backend from 'react-dnd-html5-backend';

import rootSaga from '../redux/root.saga';
import rootReducer from '../redux/root.reducer';
import mockStoreInitialState from './mock-redux-store';
import { composeWithDevTools } from 'redux-devtools-extension';

import jss from 'jss';
import preset from 'jss-preset-default';
import { StylesProvider } from '@material-ui/styles';

jss.setup(preset());

const configureStore = (reducers, initialState) => {
  const sagaMiddleware = createSagaMiddleware();
  const store = createStore(
    reducers,
    initialState,
    composeWithDevTools(
      applyMiddleware(thunkMiddleware, sagaMiddleware, createLogger())
    )
  );
  sagaMiddleware.run(rootSaga);
  return store;
};

const ProviderWrapper = ({ children, store }) => (
  <Provider store={store}>
    <DndProvider backend={HTML5Backend}>{children}</DndProvider>
  </Provider>
);

const withProvider = store => story => (
  <ProviderWrapper store={store}>{story()}</ProviderWrapper>
);

const withMockStoreProvider = story => {
  const mockStore = configureStore(rootReducer, mockStoreInitialState);
  return (
    <StylesProvider jss={jss}>
      <ProviderWrapper store={mockStore}>{story()}</ProviderWrapper>
    </StylesProvider>
  );
};

export { configureStore, withProvider, withMockStoreProvider };
