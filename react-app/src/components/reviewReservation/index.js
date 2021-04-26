import React, { useState, useEffect } from "react";
import "./reviewReservation.css";
import { createSingleReview, deleteReview } from "../../store/review";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getSingleBooking } from "../../store/booking";
import Rating from "@material-ui/lab/Rating";

const ReviewReservation = () => {
  const history = useHistory();
  const { id } = useParams();
  const dispatch = useDispatch();
  const [review, setReview] = useState("");
  const [numberOfStars, setNumberOfStars] = useState("");
  const [booking, setBooking] = useState({});
  const sessionUser = useSelector((state) => state?.session?.user);

  useEffect(() => {
    const data = async () => {
      const singleBooking = await getSingleBooking(id);
      setBooking(singleBooking);
    };
    data();
  }, [dispatch, id]);

  const handleReviewFormSubmit = (e) => {
    e.preventDefault();
    e.target.reset();

    const bookingId = id;
    const userId = sessionUser.id;
    if (!review) {
      alert("Please Insert a review!");
    } else if (!numberOfStars) {
      alert("Please Rate With Number of Stars!");
    } else {
      dispatch(createSingleReview(userId, bookingId, numberOfStars, review));
      history.go(0);
    }
  };

  const handleDeleteReview = (e, id) => {
    dispatch(deleteReview(id));
    history.go(0);
  };

  const handleRerouteToBooking = (e) => {
    history.push(`/explore`);
  };

  return (
    <div className="entireReviewsContainer">
      <div className="reviewContainer">
        Check out other reviews for {booking.title} located at {booking.state},{" "}
        {booking.capitol}
        <hr className="lineUnderTitle" />
        <div className="otherReviewsContainer">
          <div className="reviewCardContainer">
            {booking?.reviews?.map((review) => (
              <div className="reviewCard" key={review.id}>
                <div className="reviewImageAndName1">
                  {" "}
                  {review.numberOfStars}✮{" "}
                  <img src={review.photo} alt="" className="reviewImage1" />{" "}
                  Written By: <br />
                  {review.userName}
                </div>
                <div className="existingReviewContent">
                  {review.content}{" "}
                  {sessionUser.id === review.userId && (
                    <button
                      className="deleteButton"
                      onClick={(e) => handleDeleteReview(e, review.id)}
                    >
                      Delete Review{" "}
                    </button>
                  )}{" "}
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className="theBottomFormContainer">
          Write your review here
          <hr className="lineUnderTitle" />
          <form
            className="reviewForm"
            onSubmit={(e) => handleReviewFormSubmit(e)}
          >
            <textarea
              className="reviewContent1"
              placeHolder="Add a review.."
              onChange={(e) => setReview(e.target.value)}
            />
            <Rating
              name="hover-feedback"
              value={numberOfStars}
              precision={1}
              onChange={(event, newValue) => {
                setNumberOfStars(newValue);
              }}
              required
            />
            <button type="Submit" className="submitButton">
              {" "}
              Submit
            </button>
          </form>
          <button
            className="cancelReviewButton"
            onClick={(e) => handleRerouteToBooking(e)}
          >
            {" "}
            Cancel Review and Go Back to Explore!
          </button>
        </div>
      </div>
    </div>
  );
};

export default ReviewReservation;
