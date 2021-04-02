const GET_BOOKINGS = "GET_BOOKINGS";

const loadBookings = (bookings) => {
  return {
    type: GET_BOOKINGS,
    bookings,
  };
};

export const getAllBookings = () => async (dispatch) => {
  const response = await fetch(`/api/bookings`);
  if (response.ok) {
    const data = await response.json();
    dispatch(loadBookings(data));
    return data;
  }
};

export const getSingleBooking = async (id) => {
  const response = await fetch(`/api/bookings/${id}`, {
    headers: {
      "Content-type": "application/json",
    },
  });
  const data = await response.json();
  return data;
};

const initialState = { listOfBookings: [] };

const bookingReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_BOOKINGS:
      const allBookings = [];
      action.bookings.bookings.forEach((booking) => {
        allBookings.push(booking);
      });
      return {
        listOfBookings: allBookings,
      };
    default:
      return state;
  }
};

export default bookingReducer;
