import { createSlice } from '@reduxjs/toolkit';

const notificationSlice = createSlice({
  name: 'notification',
  initialState: {
    errorMessages: []
  },
  reducers: {
    showNotification(state, action) {
      state.errorMessages = action.payload;
    },
    hideNotification(state, action) {
      state.errorMessages = [];
    }
  }
});

export const { showNotification, hideNotification } = notificationSlice.actions;

export default notificationSlice.reducer;
