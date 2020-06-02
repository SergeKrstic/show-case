// Watcher
export function* onPageInit() {
  yield takeLatest(ON_PAGE_MOUNT, fetchDataForPage);
}

// Saga
export function* fetchDataForPage() {
  // Get any dependencies (from your store, or locally, etc)
  const userId = yield select(getUserId);
  const dependency = 42;

  try {
    // error checking
    if (!userId) {
      throw new Error('No user - aborting');
    }

    // run all fetch requests in parallel
    yield all([
      fork(requestAndPut, [firstRequest, userId], firstRequestActionCreator),
      fork(
        requestAndPut,
        [secondRequest, userId, dependency],
        secondRequestActionCreator
      ),
      fork(requestAndPut, [thirdRequest, userId], thirdRequestActionCreator)
    ]);
  } catch (e) {
    // error handling
    yield put({ type: ON_PAGE_MOUNT_ERROR, payload: e });
  }
}

// Helpers
function* requestAndPut(requestParameters, actionCreator) {
  const result = yield call(...requestParameters);
  yield put(actionCreator(result));
}

const firstRequest = userId => {
  return request(`${Config.api.base}/foo/bar`, { userId }).then(resp =>
    resp.json()
  );
};

const firstRequestActionCreator = data => ({
  type: FETCH_FIRST_REQUEST_SUCCESS,
  payload: data
});

// .. and secondRequestActionCreator & thirdRequestActionCreator ...
