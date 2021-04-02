const RESERVE_BOOKING = "RESERVE_BOOKING";

const addReservation = () => {
  return {
    type: RESERVE_BOOKING,
  };
};

export const reserveBooking = (userId, bookingId, startDate, endDate) => async (
  dispatch
) => {
  const response = await fetch(`/api/reservation`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      userId,
      bookingId,
      startDate,
      endDate,
    }),
  });

  const data = await response.json();
  dispatch(addReservation(data));
  return data;
};

const initialState = {};

const reservationReducer = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case RESERVE_BOOKING:
      newState = action.payload;
      return newState;
    default:
      return state;
  }
};

export default reservationReducer;
