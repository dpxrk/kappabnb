import React from "react";
import { logout } from "../../store/auth";
import { useDispatch } from "react-redux";

const LogoutButton = ({ setAuthenticated }) => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    await dispatch(logout());
    setAuthenticated(false);
  };

  return <button onClick={onLogout} className="logout"></button>;
};

export default LogoutButton;
