const RESERVE_BOOKING = "RESERVE_BOOKING";
const GET_RESERVATION = "GET_RESERVATION";

const loadReservations = (reservations) => {
  return {
    type: GET_RESERVATION,
    reservations,
  };
};

const addReservation = (reservation) => {
  return {
    type: RESERVE_BOOKING,
    reservation,
  };
};

export const getAllReservations = () => async (dispatch) => {
  const response = await fetch(`/api/reservations`);

  if (response.ok) {
    const data = await response.json();
    dispatch(loadReservations(data.reservations));
    return data;
  }
};

export const reserveBooking = (userId, bookingId, startDate, endDate) => async (
  dispatch
) => {
  const response = await fetch(`/api/reservations`, {
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

const initialState = { listOfReservations: [] };

const reservationReducer = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case GET_RESERVATION:
      const allReservations = [...action.reservations];
      return {
        listOfReservations: allReservations,
      };
    case RESERVE_BOOKING:
      newState = action.reservation;
      return newState;
    default:
      return state;
  }
};

export default reservationReducer;
