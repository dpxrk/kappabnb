import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
import "./exploreSingleBooking.css";
import { useParams, useHistory } from "react-router-dom";
import { getSingleBooking, getAllBookings } from "../../store/booking";

const ExploreSingleBooking = () => {
  const history = useHistory();
  const { id } = useParams();
  const [booking, setBooking] = useState({});
  const dispatch = useDispatch();
  const bookings = useSelector((state) => state.booking.listOfBookings);
  // const [bookingIsClickedOn, setBookingIsClickedOn] = useState("false");

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
    // history.push(`/explore/${id}`);
  };

  console.log("this is the current booking", booking);
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
      <div className="rightHalfOfPage">
        <div className="centerContainer">
          <div>
            {" "}
            Welcome to <span className="bookingTitle">
              {booking.title}{" "}
            </span> in <span className="bookingState">{booking.state} </span>
          </div>
          <div> </div>
          <div> Here are some beautiful photos for you to check out! </div>
          <div>
            {" "}
            {booking?.pictures?.forEach((picture) => (
              <img src={picture} alt="">
                {" "}
                PHOTOS
              </img>
            ))}
          </div>
          <div>
            The address to this location is: {booking.address}, {booking.state}{" "}
            {booking.capital}
          </div>
          <div>
            Check out some reviews which have an average of:
            {booking?.reviews?.forEach((review) => (
              <div>{review} </div>
            ))}
          </div>
          <div>The host is: {booking.userId}</div>
        </div>
      </div>
    </div>
  );
};

export default ExploreSingleBooking;
