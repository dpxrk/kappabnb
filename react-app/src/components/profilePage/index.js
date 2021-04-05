import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import "./profilePage.css";
import { getAllReservations } from "../../store/reservation";

const ProfilePage = () => {
  const dispatch = useDispatch();
  const [openUpcoming, setOpenUpcoming] = useState(false);
  const [openPast, setOpenPast] = useState(false);
  const [emptyPage, setEmptyPage] = useState("true");
  const sessionUser = useSelector((state) => state?.session?.user);
  const reservations = useSelector(
    (state) => state.reservation.listOfReservations
  );

  console.log("THIS IS RESERVATIONS", reservations);

  useEffect(() => {
    // dispatch(getAllBookings(bookings));
    dispatch(getAllReservations(reservations));
  }, [dispatch]);

  const today = new Date();

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
      <div className="entireCardContainer">
        <div className="bottomHalf">
          {reservations &&
            reservations.map((reservation) => {
              return (
                <div className="reservationCardContainer">
                  <img
                    src={reservation.picture}
                    alt="reservationPhoto"
                    className="picture"
                  ></img>

                  <div className="reservationDate">
                    {reservation.startDate} - {reservation.endDate}
                  </div>
                  <div className="reservationState">{reservation.state} </div>
                  <div className="reservationTitle">{reservation.title} </div>
                </div>
              );
            })}
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
