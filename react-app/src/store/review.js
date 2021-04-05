const GET_REVIEWS = "GET_REVIEWS";
const CREATE_REVIEWS = "CREATE_REVIEWS";

const getReviews = (reviews) => ({
  type: GET_REVIEWS,
  reviews,
});

const createReview = (reviews) => ({
  type: CREATE_REVIEWS,
  reviews,
});

export const getAllReviews = () => async (dispatch) => {
  const response = await fetch(`/api/reviews/`);
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
  const result = response.json();
  return dispatch(createReview(result));
};

const initialState = { reviewsArray: [] };
const reviewReducer = (state = initialState, action) => {
  let allReviews = [];
  switch (action.type) {
    case GET_REVIEWS:
      allReviews = [];
      action.reviews.reviews.forEach((review) => {
        allReviews.push(review);
      });
      return {
        reviewsArray: allReviews,
      };
    case CREATE_REVIEWS:
      allReviews = [];
      action.reviews.forEach((review) => {
        allReviews.push(review);
      });
      const newReviewsArray = [...allReviews, ...state.reviewsArray];
      return {
        reviewsArray: newReviewsArray,
      };
    default:
      return state;
  }
};

export default reviewReducer;
