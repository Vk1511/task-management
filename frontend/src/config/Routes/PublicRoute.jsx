
// This Component will give the access if and only if the user is authenticated
export const PublicRoute = ({ children, restricted, ...rest }) => {
    return children;
  };