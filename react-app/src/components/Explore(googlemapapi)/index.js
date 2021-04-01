import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
import "./explore.css";

import { getAllBookings } from "../../store/booking";

const Explore = () => {
  const dispatch = useDispatch();
  const bookings = useSelector((state) => state?.booking?.listOfBookings);
  const sessionUser = useSelector((state) => state?.session?.user);

  const mapStyles = {
    height: "100%",
    width: "100%",
  };

  useEffect(() => {
    dispatch(getAllBookings(bookings));
  }, []);

  const defaultLocation = {
    lat: 37.0902,
    lng: 180 + 95.7129,
  };

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
                />
              ))}
            </GoogleMap>
          )}
        </LoadScript>
      </div>
      <div className="rightHalfOfPage">
        <div className='Center'>Click on a city!</div>
      </div>
    </div>
  );
};

export default Explore;
