//////////////////////////////////////////////////////
// Take and Fork
//////////////////////////////////////////////////////

/* this is the saga you are going to register */
export function* aListenerOnlySaga() {
  const somePossibleData = yield take('SOME_ACTION');
  yield fork(someOtherSagaProcess);
}

function* someOtherSagaProcess() {
  /* Any process calculation you need to do */
}

//////////////////////////////////////////////////////
// Use case
//////////////////////////////////////////////////////

/* Some ugly react component*/
class CompanyDropDown extends React.Component {
  state = { company: null, branches: [] };

  componentDidUpdate({ company, branches }) {
    this.setState(({ company }) => ({ company, branches }));
  }

  onChangeCompany(company) {
    this.props.dispatch('company_change', company);
  }

  render() {
    /* omitted for convenience */
  }
}

const mapStateToProps = ({ company, branches }) => ({ company, branches });

export const CompanyDropDownContainer = connect(mapStateToProps)(
  CompanyDropDown
);

/* somewhere in your code... */
export function* listenForChangeCompany() {
  /* this variable holds the argument passed */
  const company = yield take('company_change');
  yield fork(changeCompanySaga, company);
}

function* changeCompanySaga(company) {
  const branchesPerCompany = yield call(getBranchesByCompany, company);
  yield put({ type: 'company_change_success', payload: branchesPerCompany });
}

//////////////////////////////////////////////////////
// Watch and Fork
//////////////////////////////////////////////////////

export function* listenForChangeCompany() {
  while (true) {
    const company = yield take('company_change');
    yield fork(changeCompanySaga, company);
  }
} /* eh viola! */

/* Where you register the sagas */
function* rootSagas() {
  yield [takeEvery('company_change', changeCompanySaga)];
}

//////////////////////////////////////////////////////
// Put and Take
//////////////////////////////////////////////////////

export function* fetchDataOverFiveDifferentLocations() {
  while (true) {
    yield put({ type: 'fetchSomeData_events_start' });

    /*         computing stuff...       */

    yield put({ type: 'fetchSomeData_events_success' });
  }
}

function* rootSagas() {
  yield [
    takeEvery('fetchSomeData_events', fetchDataOverFiveDifferentLocations)
  ];
}

/* We create a manager saga */
function* fetchDataManager() {
  /* we need to start the service/saga */

  yield put({ type: 'fetchSomeData_events' });

  /* we need to wait/listen when it ends...*/

  yield take('fetchSomeData_events_success');
  /*
    fork another process,
    query info from the state,
    do imperative stuff,
    whatever you need to do when the previous saga finishes,
    the sky is the limit...
  */
}

/* We create an orchestrator saga */
function* orchestratorSaga() {
  while (true) {
    yield fork(fetchDataManager);
  }
}

/* your root saga then looks like this */
function* rootSagas() {
  yield [takeEvery('other_action_trigger', orchestratorSaga)];
}

//////////////////////////////////////////////////////
// For/of Collection
//////////////////////////////////////////////////////

// function* someSagaName() {
//   /* code omitted for convenience */

//   const events = yield call(fetchEvents);
//   events.map((event) => {
//     /* this is syntactically invalid */
//     yield put({type: 'some_action', payload: event})
//   })
// }

function* someSagaName() {
  /* code omitted for convenience */

  const events = yield call(fetchEvents);
  for (event of events) {
    yield put({ type: 'some_action', payload: event });

    /* ?? */

    /* or maybe something like: */

    yield fork(someOtherSagaOrService, event);

    /* ?? */
  }
}

//////////////////////////////////////////////////////
// Error Handling
//////////////////////////////////////////////////////

/* Case 1, service that manage the error */
export function* fetchDataOverFiveDifferentLocations() {
  try {
    while (true) {
      yield put({ type: 'fetchSomeData_events_start' });

      /*           computing stuff...         */

      yield put({
        type: 'fetchSomeData_events_success'
      });
    }
  } catch (error) {
    yield put({ type: 'fetchSomeData_events_error', error });
  }
}

function* rootSagas() {
  yield [
    takeEvery('fetchSomeData_events_error', yourErrorHandlerService),
    /* ... */
    ,
  ];
}

/* Case 2, manager takes care of the error */
function* fetchDataOverFiveDifferentLocations() {
  while (true) {
    yield put({ type: 'fetchSomeData_events_start' });

    /*           computing stuff...         */

    yield put({ type: 'fetchSomeData_events_success' });
  }
}

function* fetchDataManager() {
  try {
    yield put('fetchSomeData_events');

    /*...*/

    yield take('fetchSomeData_success');
  } catch (error) {
    yield put('some_custom_error_action', error);
  }
}
