# KappaBnb
=================
[![homePage.jpg](https://i.postimg.cc/s2ZC5LS2/homePage.jpg)](https://postimg.cc/jWK1bZMV)


### [](https://github.com/dpxrk/kappabnb#live-link)[Live Link](https://kappabnb.herokuapp.com/)


Welcome to KappaBnb, a booking reservation website designed for State Capitol Buildings!

KappaBnb is a clone of the popular site, AirBnb.

KappaBnb features user's profile that lists their previous bookings and upcoming bookings. On the profile page, for past reservations, the users are able to make a review for their stay! Other features include viewing other bookings that are labeled by markers used by Google Maps Api.

This application is built upon Flask-SQLAlchemy and Postgres on the backend, while being managed by React/Redux on the front end.

[](https://github.com/dpxrk/kappabnb#technologies-used)Technologies Used
---------------------------------------------------------------------------------

1. JavaScript 
2. Python 
3. PostgreSQL
4. HTML5
5. CSS3

[](https://github.com/dpxrk/kappabnb#libraries) Libraries:
---------------------------------------------------------------------------------
1. React.js
2. Redux
3. Flask-SQLAlchemy
4. BCrypt for User Authentication
5. Google Maps API


[](https://github.com/dpxrk/kappabnb#how-to-use) How To Use
---------------------------------------------------------------------------------
```
# Clone this repository
$ git clone https://github.com/KevKodes/InstaLock.git

# Install flask dependencies in root directory
$ pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt

# Install dependencies in react-app directory
$ cd react-app
$ npm install

# Run back end server from pipenv shell
$ pipenv shell
$ flask run

# Run front end server
$ npm start
```

[![click-On-City.jpg](https://i.postimg.cc/DzmyH5GV/click-On-City.jpg)](https://postimg.cc/t1QjV3DD)
----------------------------------------------------------------------------------
The image above shows the frontend route for a user to click on markers, provided by google maps api, to look at bookings. These bookings, per se of the theme, are locations to the state capitol building for each state in the United States.


[![booking-Review.jpg](https://i.postimg.cc/bJsgGX26/booking-Review.jpg)](https://postimg.cc/7Gr0cW97)
----------------------------------------------------------------------------------
Once a booking has been clicked on, booking details on the right will be displayed for the user to know more information about the booking.

This was handled by a useEffect that created a state of the single booking which contained details of the booking that was parsed through the front end. The useEffect also contained a thunk action to obtain all the bookings from the Redux-Store in order for the markers to still have their pins located on the google maps Api
```
const [booking, setBooking] = useState({});

useEffect(() => {
    dispatch(getAllBookings(bookings));

    const data = async () => {
      const singleBooking = await getSingleBooking(id);
      setBooking(singleBooking);
    };
    data();
  }, [dispatch, id]);
  
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

```
At the bottom of the image, a calendar was implemented so that a user can choose dates of when to book. By using the DateRange npm package, I placed an onChange event handler to set reservation dates that would be stored in the database.

```
 const [reservationDates, setReservationDates] = useState([
    {
      startDate: new Date(),
      endDate: new Date(),
      key: "selection",
    },
  ]);

<DateRange
 minDate={today}
 editableDateInputs={true}
 onChange={(dates) => setReservationDates([dates.selection])}
 moveRangeOnFirstSelection={false}
 ranges={reservationDates}
 />
                  
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

```
[![reservations.jpg](https://i.postimg.cc/HnbhxGfq/reservations.jpg)](https://postimg.cc/WqbnWyp8)

Once the user has set a reservation, they would be able to go to their profile and look at their upcoming and past reservations. I placed a conditional to say that if the endDate of the reservation was passed today, then the review a reservation button would appear while on the other had, if today is before the startDate, the user will be able to cancel a reservation.

```
<div className="reservationTitle">
                    {reservation.title}{" "}
                    {today <= startDate && (
                      <div className="cancelButton">
                        <button
                          className="actualButton"
                          onClick={(e) => handleCancelButton(e, reservation.id)}
                        >
                          {" "}
                          Cancel Reservation{" "}
                        </button>
                      </div>
                    )}{" "}
                    {today >= endDate && (
                      <div className="reviewButton">
                        <button
                          className="actualButton"
                          onClick={(e) => handleReviewButton(e, reservation.id)}
                        >
                          Review the reservation
                        </button>
                      </div>
                    )}
                  </div>

```




[](https://github.com/dpxrk/kappabnb#Moving-Forward) Moving Forward:
---------------------------------------------------------------------------------
All in all, the project was a sprint with two days of planning and a week long of uninterrupted coding time. It was stressful, yet very rewarding to see my vision of a web application being developed from the group up. Moving forward, things that I want to be able to implement are functionality for users to be able to communicate with other users for messaging using websockets, and also being able to create modals throughout the project to add asthetics.





