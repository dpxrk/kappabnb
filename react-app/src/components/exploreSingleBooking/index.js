import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
import "./exploreSingleBooking.css";
import { useParams, useHistory } from "react-router-dom";
import { getSingleBooking, getAllBookings } from "../../store/booking";
import { DateRange } from "react-date-range";
import { reserveBooking } from "../../store/reservation";
import "react-date-range/dist/styles.css"; // main style file
import "react-date-range/dist/theme/default.css"; // theme css file
// import { getAllReviews } from "../../store/review";

const ExploreSingleBooking = () => {
  const history = useHistory();
  const { id } = useParams();
  const [booking, setBooking] = useState({});
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state?.session?.user);
  const bookings = useSelector((state) => state.booking.listOfBookings);
  // const reviews = useSelector((state) => state?.reviews?.newReviews);

  const [reservationDates, setReservationDates] = useState([
    {
      startDate: new Date(),
      endDate: new Date(),
      key: "selection",
    },
  ]);

  const total = Math.ceil(
    ((reservationDates[0].endDate - reservationDates[0].startDate) *
      booking.price) /
      86400000
  );

  const mapStyles = {
    height: "100%",
    width: "100%",
  };

  useEffect(() => {
    dispatch(getAllBookings(bookings));
    // dispatch(getAllReviews());

    const data = async () => {
      const singleBooking = await getSingleBooking(id);
      setBooking(singleBooking);
    };
    data();
  }, [dispatch, id]);

  const defaultLocation = {
    lat: booking.lat,
    lng: booking.lng,
  };

  const handleMarkerClick = (e, id) => {
    history.push(`/explore/${id}`);
  };

  const handleReviewSubmit = (e) => {
    e.preventDefault();
  };

  const handleZoomOut = (e) => {
    e.preventDefault();
    history.push(`/explore`);
  };

  const handleReservationSubmit = (e) => {
    e.preventDefault();
    if (
      reservationDates[0].startDate === null ||
      reservationDates[0].endDate === null
    ) {
      alert("Please enter valid dates for your trip.");
    } else {
      dispatch(
        reserveBooking(
          sessionUser.id,
          booking.id,
          reservationDates[0].startDate.toLocaleDateString(
            {},
            { dateStyle: "short" }
          ),
          reservationDates[0].endDate.toLocaleDateString(
            {},
            { dateStyle: "short" }
          )
        )
      );
      alert("Your booking has been reserved!");
    }
  };
  const today = new Date();
  return (
    <div className="explorerContainer">
      <div className="map">
        <LoadScript googleMapsApiKey={process.env.REACT_APP_GMAPIKEY}>
          {defaultLocation && (
            <GoogleMap
              mapContainerStyle={mapStyles}
              center={defaultLocation}
              zoom={15}
            >
              {bookings.map((booking, idx) => (
                <Marker
                  position={{ lat: booking.lat, lng: booking.lng }}
                  key={idx}
                  onClick={(e) => handleMarkerClick(e, booking.id)}
                />
              ))}
            </GoogleMap>
          )}
        </LoadScript>
        <button type="click" className="recenter">
          Recenter
        </button>
      </div>
      <div className="rightHalfOfPage1">
        <div className="bookingContainer">
          <div className="bookingTitle">
            <h2>
              {" "}
              Welcome to {booking.title} in {booking.state} hosted by{" "}
              {booking.userId}{" "}
            </h2>
            <hr className="bottomLineUnderTitle" />
          </div>
          <div className="bookingLocation">
            <h3>
              The address to this location is&nbsp;<span> </span>
              {booking.address}, {booking.capitol}&nbsp;{booking.state}
            </h3>
          </div>
          <div>
            <hr className="bottomLineAddress" />
            <div className="pictureContainerTitle">
              <h3> Here are some beautiful photos for you to check out </h3>{" "}
            </div>
            <div className="pictureContainer">
              {booking?.pictures?.map((picture) => (
                <div key={picture.id}>
                  <img src={picture} alt="" className="pictures" />
                </div>
              ))}
            </div>
          </div>
          <hr className="bottomLinePictures" />
          <div className="descriptionContainer">
            <h3> Description </h3>
            <h4> {booking.description}</h4>
          </div>
          <hr className="bottomLineDescription" />
          <div className="reviewsContainer">
            <h3>
              {" "}
              Check out some reviews which have an average of:{" "}
              <i class="far fa-star" /> {booking.averageReview}
            </h3>
            {booking?.reviews?.map((review) => (
              <div className="reviewContent" key={review.id}>
                <div className="reviewImageAndName">
                  {" "}
                  <img src={review.photo} alt="" className="reviewImage" />{" "}
                  {review.userName}{" "}
                </div>
                <div className="reviewContent">{review.content} </div>
                <form
                  onSubmit={(e) => handleReviewSubmit(e, sessionUser.id)}
                ></form>
              </div>
            ))}
          </div>
          <div className="bookingFormContainer">
            <div className="bookingForm">
              <form
                onSubmit={(e) => handleReservationSubmit(e)}
                className="bookingForm"
              >
                <div className="bookingFormTitle">
                  <h2>${booking.price}/night </h2>
                </div>
                <div className="bookingFormCalendar">
                  <DateRange
                    minDate={today}
                    editableDateInputs={true}
                    onChange={(dates) => setReservationDates([dates.selection])}
                    moveRangeOnFirstSelection={false}
                    ranges={reservationDates}
                  />
                </div>
                <div>
                  <button type="submit" className="bookingFormButton">
                    Book the capitol building
                  </button>
                </div>
                <div className="bookingPrice">
                  Your current total for booking per night is : ${total}
                </div>
              </form>
            </div>
            <button onClick={(e) => handleZoomOut(e)} className="resetButton">
              Want to cancel and look for another place?
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExploreSingleBooking;
