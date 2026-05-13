import React, { useState } from "react";

import axios from "axios";


function LoginPage({

  setIsLoggedIn,

  setShowLogin

}) {

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");


  const handleLogin = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/login",
        {
          email,
          password
        }
      );

      const token = response.data.access_token;

        if (!token) {

        alert("Invalid credentials");

        return;
        }

        localStorage.setItem(
        "token",
        token
        );

        setIsLoggedIn(true);

        alert("Login successful");

    } catch (error) {

      console.error(error);

      alert("Login failed");
    }
  };

  return (

    <div className="container mt-5">

      <div className="card shadow p-4">

        <h2 className="mb-4 text-center">
          Login
        </h2>

        <input
          type="email"
          className="form-control mb-3"
          placeholder="Enter Email"
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          className="form-control mb-3"
          placeholder="Enter Password"
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          className="btn btn-primary w-100"
          onClick={handleLogin}
        >
          Login
        </button>

        <button
          className="btn btn-link mt-3"
          onClick={() => setShowLogin(false)}
        >
          Don't have an account? Signup
        </button>

      </div>

    </div>
  );
}

export default LoginPage;