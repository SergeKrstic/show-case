import { createSlice } from '@reduxjs/toolkit';

const cardViewSlice = createSlice({
  name: 'cardView',
  initialState: {
    isCardViewOpen: false,
    openCardId: null
  },
  reducers: {
    openCardView(state, action) {
      const { id } = action.payload;
      state.isCardViewOpen = true;
      state.openCardId = id;
    },
    hideCardView(state, action) {
      state.isCardViewOpen = false;
      state.openCardId = null;
    }
  }
});

export const { openCardView, hideCardView } = cardViewSlice.actions;

export default cardViewSlice.reducer;
