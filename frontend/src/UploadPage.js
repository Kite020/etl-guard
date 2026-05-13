import React, { useState } from "react";
import axios from "axios";

function UploadPage() {

  const [file, setFile] = useState(null);

  const [response, setResponse] = useState(null);

  const handleUpload = async () => {

    console.log("Upload Started");

    if (!file) {

      alert("Please select a CSV file");

      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {

      console.log("Sending request...");

      const token = localStorage.getItem("token");

      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      console.log("Response received");

      console.log(res.data);

      setResponse(res.data);

    } catch (error) {

      console.error("UPLOAD ERROR:");

      console.error(error);

      alert("Upload failed");
    }
  };

  const renderTable = (data) => {

    if (!data || data.length === 0) {

      return <p>No data available</p>;
    }

    const columns = Object.keys(data[0]);

    return (

      <div className="table-responsive">

        <table className="table table-bordered table-hover">

          <thead className="table-dark">

            <tr>

              {columns.map((column) => (

                <th key={column}>
                  {column}
                </th>

              ))}

            </tr>

          </thead>

          <tbody>

            {data.map((row, index) => (

              <tr key={index}>

                {columns.map((column) => (

                  <td key={column}>
                    {String(row[column])}
                  </td>

                ))}

              </tr>

            ))}

          </tbody>

        </table>

      </div>
    );
  };

  return (

    <div className="container mt-5 mb-5">

      <div className="card shadow p-4">

        <h1 className="text-center mb-4">
          ETL Guard
        </h1>

        <p className="text-center text-muted">
          Upload, validate, and clean datasets
        </p>

        <div className="mb-3">

          <input
            type="file"
            className="form-control"
            accept=".csv"
            onChange={(e) =>
              setFile(e.target.files[0])
            }
          />

        </div>

        <button
          className="btn btn-primary w-100"
          onClick={handleUpload}
        >
          Upload CSV
        </button>

      </div>

      {response && (

        <div className="mt-4">

          {/* Upload Summary */}

          <div className="card shadow p-4 mb-4">

            <h3 className="mb-3">
              Upload Summary
            </h3>

            <p>
              <strong>Filename:</strong>
              {" "}
              {response.filename}
            </p>

            <p>
              <strong>Total Rows:</strong>
              {" "}
              {response.rows}
            </p>

            <p>
              <strong>Columns:</strong>
              {" "}
              {response.columns.join(", ")}
            </p>

          </div>

          {/* Raw Uploaded Dataset */}

          <div className="card shadow p-4 mb-4">

            <h3 className="mb-3">
              Raw Uploaded Dataset
            </h3>

            {renderTable(response.preview)}

          </div>

          {/* Validation Report */}

          <div className="card shadow p-4 mb-4">

            <h3 className="mb-3">
              Validation Report
            </h3>

            <pre>
              {JSON.stringify(
                response.validation_report,
                null,
                2
              )}
            </pre>

          </div>

          {/* Schema Drift Report */}

          <div className="card shadow p-4 mb-4">

          <h3 className="mb-3">
            Schema Drift Report
          </h3>

          <pre>
            {JSON.stringify(
              response.schema_drift_report,
              null,
              2
            )}
          </pre>

          </div>

          {/* Cleaning Report */}

          <div className="card shadow p-4 mb-4">

            <h3 className="mb-3">
              Cleaning Report
            </h3>

            <pre>
              {JSON.stringify(
                response.cleaning_report,
                null,
                2
              )}
            </pre>

          </div>

          {/* Cleaned Dataset */}

          <div className="card shadow p-4 mb-4">

            <h3 className="mb-3">
              Cleaned Dataset
            </h3>
            <a
              href={`http://127.0.0.1:8000/download/${response.download_file}`}
              className="btn btn-success mb-3"
            >

              Download Cleaned CSV

            </a>

            {renderTable(response.cleaned_preview)}

          </div>

        </div>
      )}

    </div>
  );
}

export default UploadPage;