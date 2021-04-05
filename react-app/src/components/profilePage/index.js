import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import "./profilePage.css";
import { getAllReservations, deleteReservation } from "../../store/reservation";
import { useHistory } from "react-router-dom";

const ProfilePage = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const reservations = useSelector(
    (state) => state.reservation.listOfReservations
  );

  const handleReservationClick = (e, id) => {
    e.preventDefault();
    history.push(`/explore/${id}`);
  };

  useEffect(() => {
    // dispatch(getAllBookings(bookings));
    dispatch(getAllReservations(reservations));
  }, [dispatch]);

  const handleCancelButton = (e, id) => {
    dispatch(deleteReservation(id));
    history.go(0);
  };
  const today = new Date();

  return (
    <div className="EntirePageContainer">
      <div className="titleContainer">
        <h2> Trips</h2>
        <div className="categoriesContainer">
          <div className="upcoming">Upcoming & Past</div>
        </div>
        <hr className="lineUnderTrip" />
      </div>
      <div className="entireCardContainer">
        <div className="bottomHalf">
          {reservations &&
            reservations.map((reservation) => {
              const startDate = new Date(reservation.startDate);
              const endDate = new Date(reservation.endDate);
              return (
                <div className="reservationCardContainer">
                  <img
                    src={reservation.picture}
                    alt="reservationPhoto"
                    className="picture"
                    onClick={(e) =>
                      handleReservationClick(e, reservation.bookingId)
                    }
                  ></img>

                  <div className="reservationDate">
                    {startDate.toLocaleDateString({}, { dateStyle: "short" })} -{" "}
                    {endDate.toLocaleDateString({}, { dateStyle: "short" })}
                  </div>
                  <div className="reservationState">{reservation.state} </div>
                  <div className="reservationTitle">
                    {reservation.title}{" "}
                    {today <= startDate && (
                      <div className="cancelButton">
                        <div class="leftright"></div>
                        <div class="rightleft"></div>
                        <button
                          className="actualButton"
                          onClick={(e) => handleCancelButton(e, reservation.id)}
                        >
                          {" "}
                          Cancel Reservation{" "}
                        </button>
                      </div>
                    )}{" "}
                  </div>
                </div>
              );
            })}
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;
