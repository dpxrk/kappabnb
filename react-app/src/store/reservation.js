const RESERVE_BOOKING = "RESERVE_BOOKING";

const addReservation = (reservation) => {
  return {
    type: RESERVE_BOOKING,
    reservation,
  };
};

export const reserveBooking = (userId, bookingId, startDate, endDate) => async (
  dispatch
) => {
  const response = await fetch(`/api/reservations/`, {
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
      newState = action.reservation;
      return newState;
    default:
      return state;
  }
};

export default reservationReducer;
