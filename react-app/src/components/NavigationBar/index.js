import React from "react";
import { NavLink } from "react-router-dom";
import LogoutButton from "../auth/LogoutButton";
import { useSelector } from "react-redux";

import "./navbar.css";

const NavBar = ({ authenticated, setAuthenticated }) => {
  const sessionUser = useSelector((state) => state?.session?.user);

  return authenticated ? (
    <nav className="navBarContainer">
      <ul className="topNavBarLinks">
        <div className="homeLogo">
          <i class="fab fa-airbnb" /> <span> KappaBnB</span>
        </div>

        <li>
          <NavLink
            to="/"
            exact={true}
            activeClassName="active"
            className="links"
          >
            Home
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/explore"
            exact={true}
            activeClassName="active"
            className="links"
          >
            Explore
          </NavLink>
        </li>
        <li>
          <NavLink to={`/${sessionUser?.email}`}>
            <img
              src={sessionUser?.profileImage}
              className="profileImage"
              alt="profilePic"
            />
          </NavLink>
        </li>
        <li>
          <LogoutButton setAuthenticated={setAuthenticated} />
        </li>
      </ul>
    </nav>
  ) : (
    <nav className="navBarContainer">
      <ul className="topNavBarLinks">
        <li>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
        </li>
        <li>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
