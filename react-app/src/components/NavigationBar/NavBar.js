import React, { useState, useEffect } from "react";
import { Link, NavLink } from "react-router-dom";
import LogoutButton from "../auth/LogoutButton";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import "./navbar.css";

const NavBar = ({ setAuthenticated }) => {
  const sessionUser = useSelector((state) => state.session.user);
  const history = useHistory();

  return (
    <nav className="navBarContainer">
      <div className="topNavBarLinks">
        <div>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
        </div>
        <div>
          <NavLink to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
        </div>
        <div>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
        </div>
        <li>
          <LogoutButton setAuthenticated={setAuthenticated} />
        </li>
      </div>
    </nav>
  );
};

export default NavBar;
