// source: https://www.freecodecamp.org/news/async-operations-using-redux-saga-2ba02ae077b3/

//////////////////////////////////////////////////////
// The Flight Dashboard Case
//////////////////////////////////////////////////////

class TravelServiceApi {
  static getUser() {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve({
          email: 'somemockemail@email.com',
          repository: 'http://github.com/username'
        });
      }, 3000);
    });
  }

  static getDeparture(user) {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve({
          userID: user.email,
          flightID: 'AR1973',
          date: '10/27/2016 16:00PM'
        });
      }, 2500);
    });
  }

  static getForecast(date) {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve({
          date: date,
          forecast: 'rain'
        });
      }, 2000);
    });
  }
}

const dashboard = (state = {}, action) => {
  switch (action.type) {
    case 'FETCH_DASHBOARD_SUCCESS':
      return Object.assign({}, state, action.payload);
    default:
      return state;
  }
};

const mapStateToProps = state => ({
  user: state.user,
  dashboard: state.dashboard
});

//////////////////////////////////////////////////////
// Show me the Sagas
//////////////////////////////////////////////////////

// 1. Register the Sagas

function* rootSaga() {
  yield [fork(loadUser), takeLatest('LOAD_DASHBOARD', loadDashboardSequenced)];
}

// 2. Inject the Saga Middleware into the Redux store.

const sagaMiddleware = createSagaMiddleware();
const store = createStore(
  rootReducer,
  [],
  compose(applyMiddleware(sagaMiddleware))
);
sagaMiddleware.run(rootSaga); /* inject our sagas into the middleware*/

// 3. Create the Sagas.

function* loadUser() {
  try {
    //1st step
    const user = yield call(getUser);
    //2nd step
    yield put({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (error) {
    yield put({ type: 'FETCH_FAILED', error });
  }
}

// Sequenced saga

function* loadDashboardSequenced() {
  try {
    yield take('FETCH_USER_SUCCESS');
    const user = yield select(state => state.user);
    const departure = yield call(loadDeparture, user);
    const flight = yield call(loadFlight, departure.flightID);
    const forecast = yield call(loadForecast, departure.date);
    yield put({
      type: 'FETCH_DASHBOARD_SUCCESS',
      payload: { forecast, flight, departure }
    });
  } catch (error) {
    yield put({ type: 'FETCH_FAILED', error: error.message });
  }
}

// Non-blocking Saga

function* loadDashboardNonSequenced() {
  try {
    //Wait for the user to be loaded
    yield take('FETCH_USER_SUCCESS');
    //Take the user info from the store
    const user = yield select(getUserFromState);
    //Get Departure information
    const departure = yield call(loadDeparture, user);
    //Here is when the magic happens
    const [flight, forecast] = yield [
      call(loadFlight, departure.flightID),
      call(loadForecast, departure.date)
    ];
    //Tell the store we are ready to be displayed
    yield put({
      type: 'FETCH_DASHBOARD2_SUCCESS',
      payload: { departure, flight, forecast }
    });
  } catch (error) {
    yield put({ type: 'FETCH_FAILED', error: error.message });
  }
}

function* rootSaga() {
  yield [
    fork(loadUser),
    takeLatest('LOAD_DASHBOARD', loadDashboardSequenced),
    takeLatest('LOAD_DASHBOARD2', loadDashboardNonSequenced)
  ];
}

// Non Sequenced and Non Blocking Sagas

/* **************Flight Saga************** */

function* isolatedFlight() {
  try {
    /* departure will take the value of the object passed by the put*/
    const departure = yield take('FETCH_DEPARTURE3_SUCCESS');
    const flight = yield call(loadFlight, departure.flightID);
    yield put({ type: 'FETCH_DASHBOARD3_SUCCESS', payload: { flight } });
  } catch (error) {
    yield put({ type: 'FETCH_FAILED', error: error.message });
  }
}

/* **************Forecast Saga************** */
function* isolatedForecast() {
  try {
    /* departure will take the value of the object passed by the put*/
    const departure = yield take('FETCH_DEPARTURE3_SUCCESS');
    const forecast = yield call(loadForecast, departure.date);
    yield put({ type: 'FETCH_DASHBOARD3_SUCCESS', payload: { forecast } });
  } catch (error) {
    yield put({ type: 'FETCH_FAILED', error: error.message });
  }
}

function* loadDashboardNonSequencedNonBlocking() {
  try {
    // Wait for the action to start
    yield take('FETCH_USER_SUCCESS');
    // Take the user info from the store
    const user = yield select(getUserFromState);
    // Get Departure information
    const departure = yield call(loadDeparture, user);
    // Update the store so the UI get updated
    yield put({ type: 'FETCH_DASHBOARD3_SUCCESS', payload: { departure } });
    // trigger actions for Forecast and Flight to start...
    // We can pass and object into the put statement
    yield put({ type: 'FETCH_DEPARTURE3_SUCCESS', departure });
  } catch (error) {
    yield put({ type: 'FETCH_FAILED', error: error.message });
  }
}

// What about testing?

describe('Sequenced Saga', () => {
  const saga = loadDashboardSequenced();
  let output = null;

  it('should take fetch users success', () => {
    output = saga.next().value;
    let expected = take('FETCH_USER_SUCCESS');
    expect(output).toEqual(expected);
  });

  it('should select the state from store', () => {
    output = saga.next().value;
    let expected = select(getUserFromState);
    expect(output).toEqual(expected);
  });

  it('should call LoadDeparture with the user obj', done => {
    output = saga.next(user).value;
    let expected = call(loadDeparture, user);
    done();
    expect(output).toEqual(expected);
  });

  it('should Load the flight with the flightId', done => {
    let output = saga.next(departure).value;
    let expected = call(loadFlight, departure.flightID);
    done();
    expect(output).toEqual(expected);
  });

  it('should load the forecast with the departure date', done => {
    output = saga.next(flight).value;
    let expected = call(loadForecast, departure.date);
    done();
    expect(output).toEqual(expected);
  });

  it('should put Fetch dashboard success', done => {
    output = saga.next(forecast, departure, flight).value;
    let expected = put({
      type: 'FETCH_DASHBOARD_SUCCESS',
      payload: { forecast, flight, departure }
    });
    const finished = saga.next().done;
    done();
    expect(finished).toEqual(true);
    expect(output).toEqual(expected);
  });
});
