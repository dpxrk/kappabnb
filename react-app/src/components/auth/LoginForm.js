import React, { useState } from "react";
import { Redirect, NavLink } from "react-router-dom";
import { login } from "../../store/auth";
import "./index.css";
import { useDispatch } from "react-redux";
import { setUser } from "../../store/auth";

const LoginForm = ({ authenticated, setAuthenticated }) => {
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const user = await login(email, password);
    if (!user.errors) {
      dispatch(setUser(user));
      setAuthenticated(true);
    } else {
      setErrors(user.errors);
    }
  };

  const handleDemoClick = async (e) => {
    const demoUser = await login("demo@aa.io", "password");
    dispatch(setUser(demoUser));
    setAuthenticated(true);
  };


  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="Big">
      <div className="login-form">
        <form onSubmit={onLogin}>
          <div className="kappa">KappaBnB</div>

          <div>
            <input
              name="email"
              type="text"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div>
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit" onSubmit={onLogin}>
              Login
            </button>
            <div className="err">
              {errors.map((error) => (
                <div>{error}</div>
              ))}
            </div>
          </div>
        </form>
        <button type="click" onClick={handleDemoClick} className="demoButton">
          Demo User
        </button>
        {/* <button type="click" onClick={handleHostClick} className="demoButton">
          Host User
        </button> */}
        <div className="signup-link-box">
          <div className="signup-link-text">
            Don't have an account?&nbsp;
            <NavLink
              to="/sign-up"
              style={{ textDecoration: "none" }}
              className="signUp"
            >
              Sign up
            </NavLink>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
