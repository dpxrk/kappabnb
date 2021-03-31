import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  GoogleMap,
  useJsApiLoader,
  LoadScript,
  Marker,
} from "@react-google-maps/api";

import { getAllBookings } from "../../store/booking";

const Explore = ({ location, authenticated }) => {
  const dispatch = useDispatch();
  const bookings = useSelector((state) => state?.allBookings);
  const sessionUser = useSelector((state) => state?.session?.user);

  console.log("THIS IS SESSION USER", sessionUser);
  const mapStyles = {
    height: "510px",
    width: "100%",
  };

  useEffect(() => {
    dispatch(getAllBookings());
  });

  // return (
  //   // <LoadScript googleMapsApiKey={process.env.REACT_APP_GMAPIKEY}>
  //   //   {location && (
  //   //     <GoogleMap mapContainerStyle={mapStyles} zoom={13} center={location}>
  //   //       <Marker position={location} />
  //   //     </GoogleMap>
  //   //   )}
  //   // </LoadScript>
  // );
};

export default Explore;
