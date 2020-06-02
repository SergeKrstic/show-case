import { createSlice } from '@reduxjs/toolkit';

const sessionSlice = createSlice({
  name: 'session',
  initialState: {
    userId: '',
    userName: ''
  },
  reducers: {
    updateUser(state, action) {
      const { userId, userName } = action.payload;
      state.userId = userId;
      state.userName = userName;
    }
  }
});

export const { updateUser } = sessionSlice.actions;

export default sessionSlice.reducer;
