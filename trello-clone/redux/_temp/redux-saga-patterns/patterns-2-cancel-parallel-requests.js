import { race, cancel, take, fork, all, put, select } from 'redux-saga/effects';

export function* fetchDataForPage() {
  const userId = yield select(getUserId);

  try {
    if (!userId) {
      throw new Error('No user - aborting');
    }

    const apiCalls = yield all([
      fork(
        requestAndPut,
        [requestData, 'current', userId, MAX_CURRENT],
        requestOneActionCreator
      ),
      fork(
        requestAndPut,
        [requestData, 'past', userId, MAX_PAST],
        requestTwoActionCreator
      )
    ]);

    const { cancelSagas, success } = yield race({
      cancelSagas: take(ON_PAGE_CHANGED),
      success: waitForTheseRequestsToFinish()
    });

    // If cancelSagas wins the race, cancel all of our sagas
    if (cancelSagas) {
      for (let i = 0; i < apiCalls.length; i++) {
        yield cancel(apiCalls[i]);
      }
    } else {
      return success;
    }
  } catch (e) {
    yield put({ type: ON_PAGE_MOUNT_ERROR, payload: e });
  }
}

// Returns true when all of these action types are fired
function* waitForTixRequestsToFinish() {
  yield all([take(ON_REQUEST_ONE_SUCCESS), take(ON_REQUEST_TWO_SUCCESS)]);

  return true;
}
