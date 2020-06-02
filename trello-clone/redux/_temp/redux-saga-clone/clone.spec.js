import { runSaga } from './mySagaImpl';

import reduxStore from './samples/redux-01';

import { store } from './samples/store';
import { mySaga01 } from './samples/saga-01';
import { mySaga02 } from './samples/saga-02';
import { mySaga03 } from './samples/saga-03';

describe('redux-1', () => {
  xit('should create a store', () => {
    console.log('state:', reduxStore.state);
    reduxStore.stateEmitter.on('new_state', () =>
      console.log('New state:', reduxStore.state)
    );
    reduxStore.dispatch({ type: 'setName', payload: 'Serge Krstic' });
  });
});

describe('saga-01', () => {
  xit('should run the saga', async () => {
    await runSaga(store, mySaga01);
  });
});

describe('saga-02', () => {
  xit('should run the saga', async () => {
    await runSaga(store, mySaga02);
  });
});

describe('saga-03', () => {
  xit('should run the saga', async () => {
    await runSaga(store, mySaga03);
  });
});
