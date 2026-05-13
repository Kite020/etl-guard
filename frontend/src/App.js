import React, { useState } from "react";

import UploadPage from "./UploadPage";

import Dashboard from "./Dashboard";

import LoginPage from "./LoginPage";

import SignupPage from "./SignupPage";


function App() {

  const [isLoggedIn, setIsLoggedIn] = useState(

    !!localStorage.getItem("token")
  );

  const [showLogin, setShowLogin] = useState(true);


  const handleLogout = () => {

    localStorage.removeItem("token");

    setIsLoggedIn(false);
  };

  return (

    <div>

      {!isLoggedIn ? (

        showLogin ? (

          <LoginPage
            setIsLoggedIn={setIsLoggedIn}
            setShowLogin={setShowLogin}
          />

        ) : (

          <SignupPage
            setShowLogin={setShowLogin}
          />

        )

      ) : (

        <div>

          <div className="container mt-3">

            <button
              className="btn btn-danger"
              onClick={handleLogout}
            >
              Logout
            </button>

          </div>

          <UploadPage />

          <Dashboard />

        </div>
      )}

    </div>
  );
}

export default App;