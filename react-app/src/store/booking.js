const SET_BOOKINGS = "SET_BOOKINGS";

const allBookings = (bookings) => {
  return {
    type: SET_BOOKINGS,
    bookings,
  };
};

export const getAllBookings = () => async (dispatch) => {
  const response = await fetch(`/api/bookings`);

  if (response.ok) {
    const data = await response.json();
    dispatch(allBookings(data));
  }
  return data;
};
