// source: https://hackernoon.com/modelling-common-patterns-with-redux-saga-464a380a37ce

//////////////////////////////////////////////////////
// first-amongst-these
//////////////////////////////////////////////////////

function* emailSaga() {
  // ...

  const action = yield take([
    // (A)
    `DISCARD_DRAFT`,
    `SEND_EMAIL`
  ]);
  if (action.type === `DISCARD_DRAFT`) {
    // (B)
    //discard the draft
  } else {
    //send the email
  }
}

function* emailSaga() {
  const { discard, send } = yield race({
    // (A)
    discard: take(`DISCARD_DRAFT`),
    send: take(`SEND_EMAIL`)
  });
  if (discard) {
    //discard the draft
  } else {
    //send the email
  }
}

//////////////////////////////////////////////////////
// keep-doing-until
//////////////////////////////////////////////////////

function* addToPlaylist() {
  while (true) {
    //(A)
    const action = yield take([`ADD_SONG`, `SAVE_PLAYLIST`]);
    if (action.type === `ADD_SONG`) {
      //add the song to the playlist
    } else {
      break; //(B)
    }
  }
}

function* addToPlaylist() {
  const addTask = yield takeEvery(`ADD_SONG`, function*() {
    // (A)
    //add the song to the playlist
  });
  yield take(`SAVE_PLAYLIST`); // (B)
  yield cancel(addTask); // (C)
}

//////////////////////////////////////////////////////
// step-by-step
//////////////////////////////////////////////////////

function* chooseFlight() {
  /* ... */
} // (A)

function* fillDetails() {
  /* ... */
} // (B)

function* paymentSaga() {
  /* ... */
} // (C)

function* bookFlight() {
  // (A)
  let breakLoop = false;
  let step = 0; // (B)
  const backTask = yield takeEvery(`BACK`, function*() {
    // (C)
    if (step > 0) {
      step--;
    }
  });
  while (true) {
    // (D)
    switch (
      step // (E)
    ) {
      case 0: {
        yield call(selectFlight); // (F)
        step++; // (G)
        break;
      }
      case 1: {
        yield call(fillDetails);
        step++;
        break;
      }
      case 2: {
        yield call(paymentSaga);
        step++;
        break;
      }
      case 3: {
        breakLoop = true; // (H)
        yield cancel(backTask); // (I)
        break;
      }
    }
    if (breakLoop) {
      // (J)
      break;
    }
  }
}
