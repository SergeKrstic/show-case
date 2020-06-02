import reducer, * as actions from './session.slice';
import * as selectors from './session.selectors';

const userId = 'user-id-01';
const userName = 'John Smith';

const state = {
  session: {
    userId,
    userName
  }
};

describe('session reducer', () => {
  it('should return the initial state', () => {
    expect(reducer(undefined, {})).toEqual({
      userId: '',
      userName: ''
    });
  });

  it('should handle UPDATE_USER', () => {
    const action = actions.updateUser({ userId, userName });
    expect(reducer({}, action)).toEqual({ userId, userName });
  });
});

describe('session selectors', () => {
  it('should return get the userId', () => {
    expect(selectors.selectUserId(state)).toEqual(userId);
  });

  it('should return get the userName', () => {
    expect(selectors.selectUserName(state)).toEqual(userName);
  });
});
