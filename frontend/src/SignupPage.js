import React, { useState } from "react";

import axios from "axios";


function SignupPage({ setShowLogin }) {

  const [username, setUsername] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");


  const handleSignup = async () => {

    try {

      await axios.post(
        `${process.env.REACT_APP_API_URL}/signup`,
        
        {
          username,
          email,
          password
        }
      );

      alert("Signup successful");

      setShowLogin(true);

    } catch (error) {

      console.error(error);

      alert("Signup failed");
    }
  };

  return (

    <div className="container mt-5">

      <div className="card shadow p-4">

        <h2 className="text-center mb-4">
          Signup
        </h2>

        <input
          type="text"
          className="form-control mb-3"
          placeholder="Enter Username"
          onChange={(e) =>
            setUsername(e.target.value)
          }
        />

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
          className="btn btn-success w-100"
          onClick={handleSignup}
        >
          Signup
        </button>

        <button
          className="btn btn-link mt-3"
          onClick={() => setShowLogin(true)}
        >
          Already have an account? Login
        </button>

      </div>

    </div>
  );
}

export default SignupPage;