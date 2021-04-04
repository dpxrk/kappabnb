import React, { useState, useEffect } from "react";
import { Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavigationBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import { authenticate, restoreUser } from "./store/auth";
import SplashPage from "./components/splashPage";
import Explore from "./components/Explore(googlemapapi)";
import { useDispatch } from "react-redux";
import ExploreSingleBooking from "./components/exploreSingleBooking";
import ProfilePage from "./components/profilePage";

function App() {
  const dispatch = useDispatch();
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
      const user = await authenticate();
      if (!user.errors) {
        setAuthenticated(true);
        dispatch(restoreUser());
      }
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <>
      <NavBar
        authenticated={authenticated}
        setAuthenticated={setAuthenticated}
      />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/" exact={true}>
          <SplashPage />
        </Route>
        <ProtectedRoute
          path="/explore"
          exact={true}
          authenticated={authenticated}
          setAutheenticated={setAuthenticated}
        >
          <Explore />
        </ProtectedRoute>
        <ProtectedRoute
          path="/:email"
          exact={true}
          authenticated={authenticated}
        >
          <ProfilePage />
        </ProtectedRoute>
        <ProtectedRoute
          path="/explore/:id"
          exact={true}
          authenticated={authenticated}
        >
          <ExploreSingleBooking />
        </ProtectedRoute>
        <Route path="/sign-up" exact={true}>
          <SignUpForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
      </Switch>
    </>
  );
}

export default App;
