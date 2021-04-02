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

const ExploreSingleBooking = () => {
  const history = useHistory();
  const { id } = useParams();
  const [booking, setBooking] = useState({});
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state?.session?.user);
  const bookings = useSelector((state) => state.booking.listOfBookings);
  const [reservationDates, setReservationDates] = useState([
    {
      start: new Date(),
      endDate: new Date(),
      key: "selection",
    },
  ]);

  const mapStyles = {
    height: "100%",
    width: "100%",
  };

  useEffect(() => {
    dispatch(getAllBookings(bookings));

    const data = async () => {
      const singleBooking = await getSingleBooking(id);
      setBooking(singleBooking);
    };
    data();
  }, [dispatch, id]);

  const defaultLocation = {
    lat: 40.281238995065614,
    lng: -100.17976810973792,
  };

  const handleMarkerClick = (e, id) => {
    // e.preventDefault();
    // history.push(`/explore/${id}`);
  };

  const handleReservationSubmit = (e) => {
    e.preventDefault();
    if (
      reservationDates[0].starteDate === null ||
      reservationDates[0].endDate === null
    ) {
      alert("Please enter valid dates for your trip.");
    } else {
      dispatch(
        reserveBooking(
          sessionUser.id,
          booking.id,
          reservationDates[0].startDate,
          reservationDates[0].endDate
        )
      );
    }
  };
  const today = new Date();
  console.log("this is the current booking", booking.pictures);
  return (
    <div className="explorerContainer">
      <div className="map">
        <LoadScript googleMapsApiKey={process.env.REACT_APP_GMAPIKEY}>
          {defaultLocation && (
            <GoogleMap
              mapContainerStyle={mapStyles}
              center={defaultLocation}
              // onCenterChanged={() => {
              //   console.log("center change");
              // }}
              zoom={5}
            >
              {bookings.map((booking, idx) => (
                <Marker
                  position={{ lat: booking.lat, lng: booking.lng }}
                  key={idx}
                  onClick={handleMarkerClick(booking.id)}
                />
              ))}
            </GoogleMap>
          )}
        </LoadScript>
      </div>
      <div className="rightHalfOfPage1">
        <div className="bookingContainer">
          <div className="bookingTitle">
            <h2>
              {" "}
              Welcome to {booking.title} in {booking.state} hosted by:{" "}
              {booking.userId}{" "}
            </h2>
          </div>
          <div className="bookingLocation">
            <h3>
              The address to this location is: <span>{booking.address}, </span>
              {booking.state} {booking.capital}
            </h3>
          </div>
          <div className="descriptionContainer">
            <h4>Description: {booking.description}</h4>
          </div>
          <div className="reviews">
            Check out some reviews which have an average of:
            {booking?.reviews?.forEach((review) => (
              <div>{review} </div>
            ))}
          </div>
          <div>
            <h3> Here are some beautiful photos for you to check out! </h3>{" "}
            {booking?.pictures?.forEach((picture) => (
              <div key={picture.id}>
                <img src={picture} alt="" />
              </div>
            ))}
          </div>
        </div>
        <div className="bookingFormContainer">
          <div className="bookingForm">
            <form onSubmit={(e) => handleReservationSubmit(e)}>
              <div className="bookingFormTitle">
                <h2>${booking.price}/night </h2>
              </div>
              <div className="bookingFormCalendar">
                <DateRange
                  minDate={today}
                  editableDateInputs={true}
                  onChange={(dates) => setReservationDates([dates.selection])}
                  moveRangeOnFirstSelection={false}
                  reservationDates={reservationDates}
                />
              </div>
              <div>
                <button type="submit" className="bookingFormButton">
                  Book the capitol building
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExploreSingleBooking;
