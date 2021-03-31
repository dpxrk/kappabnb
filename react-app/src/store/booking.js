const GET_BOOKINGS = "GET_BOOKINGS";

const loadBookings = (bookings) => {
  return {
    type: SET_BOOKINGS,
    bookings,
  };
};

export const getAllBookings = () => async (dispatch) => {
  const response = await fetch(`/api/bookings`);

  if (response.ok) {
    const data = await response.json();
    dispatch(loadBookings(data));
  }
  return data;
};

const initialState = [];

const bookingReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_BOOKINGS:
      const allBookings = [];
      action.bookings.bookings.forEach((booking) => {
        allBookings.push(booking);
      });
      return {
        allBookings,
      };
  }
};

export default bookingReducer;
