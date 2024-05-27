import { PrivateRoute } from "./PrivateRoute";
import { PublicRoute } from "./PublicRoute";
import Auth from "../../Components/Auth/Auth";
import Task from "../../Components/Task/Task";

export const AppRoutes = [
  {
    path: "/",
    element: (
      <PublicRoute>
        <Auth />
      </PublicRoute>
    ),
  },
  {
    path: "task",
    element: (
      <PrivateRoute>
        <Task />
      </PrivateRoute>
    ),
  },
];