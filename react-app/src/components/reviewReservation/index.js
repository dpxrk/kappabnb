import React, { useState, useEffect } from "react";
import "./reviewReservation.css";
import {
  getAllReviews,
  getAllReviewsOfOneBooking,
  createSingleReview,
} from "../../store/review";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getSingleBooking } from "../../store/booking";

const ReviewReservation = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const [review, setReview] = useState("");
  const [numberOfStars, setNumberOfStars] = useState("");
  const [booking, setBooking] = useState({});
  const sessionUser = useSelector((state) => state?.session?.user);
  const reviews = useSelector((state) => state?.review?.reviewsArray);

  console.log("THESE ARE THE REVIEWS", reviews);
  console.log("THIS IS THE BOOKING", booking);

  useEffect(() => {
    dispatch(getAllReviews(id));
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
  };

  return (
    <div className="entireReviewsContainer">
      <div className="reviewContainer">
        Check out other reviews
        <hr className="lineUnderTitle" />
        <div className="otherReviewsContainer">
          {booking?.reviews?.map((review) => (
            <div className="reviewContent" key={review.id}>
              <div className="reviewImageAndName">
                {" "}
                <img src={review.photo} alt="" className="reviewImage" />{" "}
                {review.userName}{" "}
              </div>
              <div className="reviewContent">{review.content} </div>
            </div>
          ))}
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
              placeHolder="Rate the reservation from 1-5"
              onChange={(e) => setNumberOfStars(e.target.value)}
            />
            <button type="Submit"> Submit</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ReviewReservation;
