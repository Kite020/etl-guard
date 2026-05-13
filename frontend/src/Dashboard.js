import React, { useEffect, useState } from "react";

import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function Dashboard() {

  const [uploads, setUploads] = useState([]);

  const [analytics, setAnalytics] = useState({});

  useEffect(() => {

    fetchUploads();

    fetchAnalytics();

  }, []);

  const fetchUploads = async () => {

    try {

      const token = localStorage.getItem("token");

      const response = await axios.get(
        "http://127.0.0.1:8000/uploads",
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      setUploads(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const fetchAnalytics = async () => {

    try {

      const token = localStorage.getItem("token");

      const response = await axios.get(
        "http://127.0.0.1:8000/analytics",
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      setAnalytics(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  const chartData = [

    {
      name: "Uploads",
      value: analytics.total_uploads || 0
    },

    {
      name: "Rows",
      value: analytics.total_rows_processed || 0
    }
  ];

  return (

    <div className="container mt-5 mb-5">

      <div className="card shadow p-4 mb-4">

        <h2 className="mb-4">
          Analytics Overview
        </h2>

        <div className="row">

          <div className="col-md-6">

            <div className="card p-3 shadow-sm">

              <h5>Total Uploads</h5>

              <h2>
                {analytics.total_uploads || 0}
              </h2>

            </div>

          </div>

          <div className="col-md-6">

            <div className="card p-3 shadow-sm">

              <h5>Total Rows Processed</h5>

              <h2>
                {analytics.total_rows_processed || 0}
              </h2>

            </div>

          </div>

        </div>

      </div>

      <div className="card shadow p-4 mb-4">

        <h2 className="mb-4">
          Upload Analytics Chart
        </h2>

        <BarChart
          width={600}
          height={300}
          data={chartData}
        >

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="name" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="value" />

        </BarChart>

      </div>

      <div className="card shadow p-4">

        <h2 className="mb-4">
          Upload History Dashboard
        </h2>

        <div className="table-responsive">

          <table className="table table-bordered table-hover">

            <thead className="table-dark">

              <tr>

                <th>ID</th>

                <th>Filename</th>

                <th>Total Rows</th>

                <th>Created At</th>

              </tr>

            </thead>

            <tbody>

              {uploads.map((upload) => (

                <tr key={upload.id}>

                  <td>{upload.id}</td>

                  <td>{upload.filename}</td>

                  <td>{upload.total_rows}</td>

                  <td>{upload.created_at}</td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;