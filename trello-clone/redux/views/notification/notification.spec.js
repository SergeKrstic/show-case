import types from './notification.types';
import * as actions from './notification.actions';
import reducer from './notification.reducer';

describe('notification actions', () => {
  it('should create showNotification action', () => {
    const payload = {};
    const expectedAction = {
      type: types.SHOW_NOTIFICATION,
      payload
    };

    expect(actions.showNotification(payload)).toEqual(expectedAction);
  });

  it('should create hideNotification action', () => {
    const expectedAction = {
      type: types.HIDE_NOTIFICATION
    };

    expect(actions.hideNotification()).toEqual(expectedAction);
  });
});

describe('notification reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      errorMessages: []
    });
  });

  it('should handle SHOW_NOTIFICATION', () => {
    const payload = [
      'There was an issue with the server',
      'Try again in a few mins'
    ];
    const action = actions.showNotification(payload);
    expect(reducer({}, action)).toEqual({
      errorMessages: [
        'There was an issue with the server',
        'Try again in a few mins'
      ]
    });
  });

  it('should handle HIDE_NOTIFICATION', () => {
    const action = actions.hideNotification();
    expect(reducer({}, action)).toEqual({
      errorMessages: []
    });
  });
});
