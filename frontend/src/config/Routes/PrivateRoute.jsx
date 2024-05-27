import React, { useEffect } from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../../context/userContext";

// This Component will give the access if and only if the user is authenticated
export const PrivateRoute = ({ children }) => {
  const { authed } = useAuth();
  return authed ? children : <Navigate to="/" />;
};