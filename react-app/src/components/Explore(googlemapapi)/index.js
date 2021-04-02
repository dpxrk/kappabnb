import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";
import "./explore.css";
import { useHistory, Redirect } from "react-router-dom";

import { getAllBookings } from "../../store/booking";

const Explore = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const bookings = useSelector((state) => state.booking.listOfBookings);

  const mapStyles = {
    height: "100%",
    width: "100%",
  };

  useEffect(() => {
    dispatch(getAllBookings(bookings));
  }, [dispatch]);

  const defaultLocation = {
    lat: 40.281238995065614,
    lng: -100.17976810973792,
  };

  const handleMarkerClick = (e, id) => {
    // return <Redirect to={`/explore/${id}`} />;

    history.push(`/explore/${id}`);
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
                  onClick={(e) => handleMarkerClick(e, booking.id)}
                />
              ))}
            </GoogleMap>
          )}
        </LoadScript>
      </div>
      <div className="rightHalfOfPage">
        <div className="centerContainer">
          <div className="centerText"> Click on a City!</div>
        </div>
      </div>
    </div>
  );
};

export default Explore;
