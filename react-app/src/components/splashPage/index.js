import React, { useEffect } from "react";
import "./splashpage.css";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { getAllBookings } from "../../store/booking";

const SplashPage = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const bookings = useSelector((state) => state?.allBookings);

  useEffect(() => {
    dispatch(getAllBookings(bookings));
  }, [dispatch, bookings]);

  const handleClickForImages = (e) => {
    e.preventDefault();
    history.push(`/explore`);
  };

  return (
    <div className="entireBackGround">
      <div className="blackBar">
        <div className="landingPage">
          <img
            alt="capitalBackGroundPhoto"
            src="https://wallpapercave.com/wp/wp4204392.jpg"
          />
        </div>
        <div className="middleText">
          <div className="madePossible"> Made possible by Hosts</div>
        </div>
        <div className="fourImageContainer">
          <div className="stayAnywhere">Stay anywhere</div>
          <div className="fourCenterImages">
            <div
              className="differentCapitalBuildings"
              onClick={(e) => handleClickForImages(e)}
            >
              <img alt="" src="https://wallpapercave.com/wp/wp4204401.jpg" />
              <h2>Different State</h2>
            </div>
            <div
              className="differentCapitalBuildings"
              onClick={(e) => handleClickForImages(e)}
            >
              <img alt="" src="https://wallpapercave.com/wp/wp4064278.jpg" />
              <h2>Different Capital</h2>
            </div>
            <div
              className="differentCapitalBuildings"
              onClick={(e) => handleClickForImages(e)}
            >
              <img alt="" src="https://wallpapercave.com/wp/wp4204405.jpg" />
              <h2>One Nation</h2>
            </div>
            <div
              className="differentCapitalBuildings"
              onClick={(e) => handleClickForImages(e)}
            >
              <img alt="" src="https://wallpapercave.com/wp/wp4204408.jpg" />
              <h2>One Country</h2>
            </div>
          </div>
        </div>
        <div className="becomeAHostContainer">
          <img
            alt="bottomHostImage"
            src="https://wallpapercave.com/wp/wp4204425.jpg"
          />
          <div className="becomeAHostContainerText">
            <h1>Your state capital is worth staying at</h1>
            <h4>
              Come learn more about the history
              <span> of your state.</span>
            </h4>
            {/* <button>Become a Host</button> */}
          </div>
        </div>
        <div className="footerContainer">
          <div className="footerInformation">
            <div className="footers">
              <section className="footers">
                {" "}
                <ul className="contactList">
                  Developed By : Daniel Park
                  <a href="https://www.linkedin.com/in/danielpark0503/">
                    LinkedIn
                  </a>
                  <a href="https://angel.co/u/daniel-park-70">Angellist</a>
                  <a href="https://github.com/dpxrk">Github</a>
                </ul>
              </section>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SplashPage;
