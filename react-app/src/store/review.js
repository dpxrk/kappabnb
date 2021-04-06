const GET_REVIEWS = "GET_REVIEWS";
const CREATE_REVIEWS = "CREATE_REVIEWS";
const DELETE_REVIEW = "DELETE_REVIEW";

const getReviews = (reviews) => ({
  type: GET_REVIEWS,
  reviews,
});

const createReview = (reviews) => ({
  type: CREATE_REVIEWS,
  reviews,
});

const removeReview = (id) => {
  return {
    type: DELETE_REVIEW,
    id,
  };
};

export const getAllReviews = () => async (dispatch) => {
  const response = await fetch(`/api/reviews`);
  if (response.ok) {
    const data = await response.json();
    dispatch(getReviews(data.reviews));
    return data;
  }
};

export const getAllReviewsOfOneBooking = (id) => async (dispatch) => {
  const response = await fetch(`/api/reviews/${id}`);
  if (response.ok) {
    const data = await response.json();
    dispatch(getReviews(data));
    return data;
  }
};

export const createSingleReview = (
  userId,
  bookingId,
  numberOfStars,
  content
) => async (dispatch) => {
  const build = {
    method: "POST",
    headers: { "Content-Type": "Application/json" },
    body: JSON.stringify({ userId, bookingId, numberOfStars, content }),
  };

  const response = await fetch(`/api/reviews/${bookingId}`, build);

  if (!response.ok) alert("SOMETHING IS WRONG");
  const result = await response.json();

  dispatch(createReview(result));
  return result;
};

export const deleteReview = (id) => async (dispatch) => {
  const build = { method: "DELETE" };

  const response = await fetch(`/api/reviews/${id}`, build);
  const result = await response.json();
  dispatch(removeReview(result));
  return response;
};

const initialState = { listOfReviews: [] };
const reviewReducer = (state = initialState, action) => {
  let newState;
  let allReviews;
  switch (action.type) {
    case GET_REVIEWS:
      allReviews = [...action.reviews];
      return {
        listOfReviews: allReviews,
      };
    case CREATE_REVIEWS:
      allReviews = [action.reviews];
      const newListOfReviews = [...allReviews, ...state.listOfReviews];
      return {
        listOfReviews: newListOfReviews,
      };
    case DELETE_REVIEW:
      newState = { ...state };
      delete newState[action.id];
      return newState;
    default:
      return state;
  }
};

export default reviewReducer;
