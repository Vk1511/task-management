import "./App.css";
import { createBrowserRouter, Routes, Route } from "react-router-dom";
import { AppRoutes } from "./config/Routes/AppRoutes";
import Auth from "./Components/Auth/Auth";
import Task from "./Components/Task/Task";
import { PrivateRoute } from "./config/Routes/PrivateRoute";
import { PublicRoute } from "./config/Routes/PublicRoute";

const router = createBrowserRouter(AppRoutes);

function App() {
  return (
    <Routes>
      <Route
        exact
        path="/"
        element={
          <PublicRoute>
            <Auth />
          </PublicRoute>
        }
      />
      <Route
        exact
        path="/task"
        element={
          <PrivateRoute>
            <Task />
          </PrivateRoute>
        }
      />
    </Routes>
  );
  // return <RouterProvider router={router} />;
}

export default App;
