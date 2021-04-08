import React, { useState, useEffect } from "react";
import "./reviewReservation.css";
import { createSingleReview, deleteReview } from "../../store/review";
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getSingleBooking } from "../../store/booking";

const ReviewReservation = () => {
  const history = useHistory();
  const { id } = useParams();
  const dispatch = useDispatch();
  const [review, setReview] = useState("");
  const [numberOfStars, setNumberOfStars] = useState("");
  const [booking, setBooking] = useState({});
  const sessionUser = useSelector((state) => state?.session?.user);

  console.log(booking);

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
    dispatch(createSingleReview(userId, bookingId, numberOfStars, review));
    history.go(0);
  };

  const handleDeleteReview = (e, id) => {
    dispatch(deleteReview(id));
    history.go(0);
  };

  const handleRerouteToBooking = (e, id) => {
    history.push(`/explore/${booking.id}`);
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
                  <i class="far fa-star" /> {review.numberOfStars}{" "}
                  <img src={review.photo} alt="" className="reviewImage1" />{" "}
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
              className="reviewContent"
              placeHolder="Add a review.."
              onChange={(e) => setReview(e.target.value)}
            />
            <input
              className="numberOfStarsInputBox"
              placeHolder="Rating from 1-5"
              onChange={(e) => setNumberOfStars(e.target.value)}
            />
            <button type="Submit" className="submitButton">
              {" "}
              Submit
            </button>
          </form>
          <button className='cancelReviewButton'> Want to cancel review and go back to explore?</button>
        </div>
      </div>
    </div>
  );
};

export default ReviewReservation;
