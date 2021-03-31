import React, { useState } from "react";
import { Redirect, NavLink } from "react-router-dom";
import { signUp, setUser } from "../../store/auth";
import { useDispatch } from "react-redux";
import "./index.css";

const SignUpForm = ({ authenticated, setAuthenticated }) => {
  const dispatch = useDispatch();
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onSignUp = async (e) => {
    e.preventDefault();
    const user = await signUp(fullName, email, password);
    if (!user.errors) {
      dispatch(setUser(user));
      setAuthenticated(true);
    }
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="signUpContainer">
      <div className="signup-form">
        <form onSubmit={onSignUp}>
          <div className="kappa">KappaBnB</div>
          <div>
            <input
              name="fullName"
              type="text"
              placeholder="Full Name"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
            />
          </div>
          <div>
            <input
              type="text"
              name="email"
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
              value={email}
            ></input>
          </div>

          <div>
            <input
              type="password"
              name="password"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
              value={password}
            ></input>
          </div>
          <button type="submit">Sign up</button>
        </form>
        <div className="login-link-box">
          <div className="login-link-text">
            Have an account?&nbsp;
            <NavLink
              to="/login"
              style={{ textDecoration: "none" }}
              className="login"
            >
              Log in
            </NavLink>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUpForm;
