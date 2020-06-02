import { createSlice } from '@reduxjs/toolkit';

const homeViewSlice = createSlice({
  name: 'popOver',
  initialState: {
    isPopOverOpen: false,
    isFocusOnPopOver: false
  },
  reducers: {
    showPopOver(state, action) {
      state.isPopOverOpen = true;
    },
    hidePopOver(state, action) {
      state.isPopOverOpen = false;
    },
    focusOnPopOver(state, action) {
      state.isFocusOnPopOver = true;
    },
    blurOnPopOver(state, action) {
      state.isFocusOnPopOver = false;
    }
  }
});

export const { openHomeView, closeHomeView } = homeViewSlice.actions;

export default homeViewSlice.reducer;
