// source: https://medium.com/@bryanfillmer/keep-trying-redux-saga-style-b273882b9ec
// soucre: https://codeburst.io/try-again-more-redux-saga-patterns-bfbc3ffcdc

//////////////////////////////////////////////////////
// Keep Trying
//////////////////////////////////////////////////////

function* fetchProducts() {
  try {
    const products = yield call(Api.fetch, '/products');
    yield put({ type: 'PRODUCTS_RECEIVED', products });
  } catch (error) {
    yield put({ type: 'PRODUCTS_REQUEST_FAILED', error });
  }
}

// Pass in our generator we want to restart, and some function
// to handle potential errors thrown within said generator.
const autoRestart = (generator, handleError) => {
  return function* autoRestarting(...args) {
    while (true) {
      try {
        yield call(generator, ...args);
        break;
      } catch (e) {
        yield handleError(e);
      }
    }
  };
};

const fetchProducts = autoRestart(
  function* fetchProducts() {
    try {
      const products = yield call(Api.fetch, '/products');
      yield put({ type: 'PRODUCTS_RECEIVED', products });
    } catch (error) {
      throw new Error(error);
    }
  },
  function* handleError(e) {
    yield put({ type: 'PRODUCTS_REQUEST_FAILED', e });
  }
);

//////////////////////////////////////////////////////
// Try Again: Max Tries
//////////////////////////////////////////////////////

const log = function() {
  /* ... */
};
const multipleAttempts = (generator, handleError, maxTries) => {
  return function* multipleAttempts(...args) {
    let n = 0;
    while (n <= maxTries) {
      try {
        yield call(generator, ...args);
        break;
      } catch (e) {
        // Log errors here until maxTries has been hit, to prevent
        // spamming the user with messages.
        if (n < maxTries) {
          yield log(e);
        } else {
          yield handleError(e);
        }
      }
    }
  };
};

//////////////////////////////////////////////////////
// Try Again: Time Based Attempts
//////////////////////////////////////////////////////

import {
  hydrateUserData,
  hydrateListData,
  setApplicationToOffline
} from 'actions';

// 30 seconds max load
const maxLoadTime = 1800;

// Fetch the data our application needs and store it in local state.
function* fetchData() {
  const { userData, listData } = yield all({
    userData: call(getUserData),
    listData: call(getListData)
  });
  // Store or retrieved data in our Redux state.
  yield [put(hydrateUserData(userData)), put(hydrateListData(listData))];
  return true;
}

// If our application is offline set some state that will disable
// UI features and notify the user.
function* setOfflineState() {
  yield put(setApplicationToOffline());
}

// Attempt to load our application data in a fixed amount of
// time, otherwise default to offline mode.
function* loadApplication(loadTime, fetchData, setOfflineState) {
  const { offline, online } = yield race({
    offline: delay(loadTime, true),
    online: call(fetchData)
  });
  // Time won our race, thus fetchData never resolved in our
  // required time and we should treat the application as offline.
  if (offline) {
    yield call(setOfflineState);
  }
}
