import React, {
  useState,
  createContext,
  useContext,
  useEffect,
  useCallback,
} from "react";
import { Navigate, useNavigate } from "react-router-dom";
import {login} from "../service/Auth";
// Create the context
const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();
  const [authed, setAuthed] = useState(!!localStorage.getItem("accessToken") || false);

  console.log("object", authed);
  // const [authed, setAuthed] = useState(false);
  const [userProfileData, setUserProfileData] = useState(null);

  useEffect(() => {
    // localStorage.clear();
  }, []);

  const fetchAndSetUserProfileData = async (apiParams) => {};

  const logout = async () => {
    setAuthed(false);
    setUserProfileData(null);
    localStorage.clear();
    window.location.href = '/';
  };

  const sinIn = useCallback((body) => {
    login(body)
      .then((res) => {
        localStorage.setItem("accessToken",res.data.access)
        localStorage.setItem("refreshToken",res.data.refresh)
        // navigate("/task")
        window.location.href = '/task';
      })
      .catch((err) => {
        console.error(err);
      });
      navigate("/task")
  }, []);

  // return !globalLoader ? (
  // Using the provider so that ANY component in our application can
  // use the values that we are sending.
  return (
    <AuthContext.Provider
      value={{
        authed,
        userProfileData,
        setAuthed,
        logout,
        setUserProfileData,
        sinIn,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

// Finally creating the custom hook
export const useAuth = () => useContext(AuthContext);
