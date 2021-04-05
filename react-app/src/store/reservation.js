const RESERVE_BOOKING = "RESERVE_BOOKING";
const GET_RESERVATION = "GET_RESERVATION";
const DELETE_RESERVATION = "DELETE_RESERVATION";

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

const removeReservation = (id) => {
  return {
    type: DELETE_RESERVATION,
    id,
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

export const deleteReservation = (id) => async (dispatch) => {
  const build = { method: "DELETE" };

  const response = await fetch(`/api/reservations/${id}`, build);
  const result = response.json();
  dispatch(removeReservation(result));
  return response;
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
    case DELETE_RESERVATION:
      newState = { ...state };
      delete newState[action.id];
      return newState;
    default:
      return state;
  }
};

export default reservationReducer;
