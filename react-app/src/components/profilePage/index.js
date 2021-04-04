import React, { useState } from "react";
import { useSelector } from "react-redux";
import "./profilePage.css";

const ProfilePage = () => {
  const sessionUser = useSelector((state) => state?.session?.user);

  console.log(sessionUser);

  return (
    <div className="EntirePageContainer">
      <div className="titleContainer">
        <h2> Trips</h2>
        <div className="categoriesContainer">
          <div className="upcoming">Upcoming</div>
          <div className="past">Past</div>
        </div>
        <hr className="lineUnderTrip" />
      </div>
    </div>
  );
};

export default ProfilePage;
