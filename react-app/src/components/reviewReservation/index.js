import React, { useState, useEffect } from "react";
import "./reviewReservation.css";
import {
  getAllReviews,
  getAllReviewsOfOneBooking,
  createSingleReview,
} from "../../store/review";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

const ReviewReservation = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const [review, setReview] = useState("");
  const [numberOfStars, setNumberOfStars] = useState("");
  const sessionUser = useSelector((state) => state?.session?.user);
  const reviews = useSelector((state) => state?.review?.reviewsArray);

  console.log("THESE ARE THE REVIEWS", reviews);

  useEffect(() => {
    dispatch(getAllReviews(id));
  }, [dispatch, id]);

  const handleReviewFormSubmit = (e) => {
    e.preventDefault();
    e.target.reset();

    const bookingId = id;
    const userId = sessionUser.id;
    dispatch(createSingleReview(userId, bookingId, numberOfStars, review));
  };

  return (
    <div className="entireReviewsContainer">
      <div className="reviewContainer">
        Check out other reviews and write your own
        <hr className="lineUnderTitle" />
        <div className="otherReviewsContainer"> You are here </div>
        <form
          className="reviewForm"
          onSubmit={(e) => handleReviewFormSubmit(e)}
        >
          <textarea
            placeHolder="Add a review.."
            onChange={(e) => setReview(e.target.value)}
          />
          <input
            placeHolder="Rate the reservation from 1-5"
            onChange={(e) => setNumberOfStars(e.target.value)}
          />
        </form>
      </div>
    </div>
  );
};

export default ReviewReservation;
