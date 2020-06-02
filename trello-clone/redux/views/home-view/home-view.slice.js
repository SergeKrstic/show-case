import { createSlice } from '@reduxjs/toolkit';

const homeViewSlice = createSlice({
  name: 'homeView',
  initialState: {
    isHomeViewOpen: false
  },
  reducers: {
    openHomeView(state, action) {
      state.isHomeViewOpen = true;
    },
    closeHomeView(state, action) {
      state.isHomeViewOpen = false;
    }
  }
});

export const { openHomeView, closeHomeView } = homeViewSlice.actions;

export default homeViewSlice.reducer;
