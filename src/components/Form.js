import React, { useState, useRef } from 'react';
import axios from 'axios';

const Form = () => {
  const [formData, setFormData] = useState({
    age: '', sex: '', cp: '', trestbps: '', chol: '',
    fbs: '', restecg: '', thalach: '', exang: '',
    oldpeak: '', slope: '', ca: '', thal: ''
  });

  const [result, setResult] = useState(null);
  const reportRef = useRef();

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post('http://localhost:5000/predict', formData);

    setResult(res.data.prediction === 1 ? "Heart Disease Detected" : "No Heart Disease");
  };

  const handlePrint = () => {
    const printContent = reportRef.current.innerHTML;
    const newWindow = window.open('', '', 'width=800,height=600');
    newWindow.document.write('<html><head><title>Heart Disease Report</title></head><body>');
    newWindow.document.write(printContent);
    newWindow.document.write('</body></html>');
    newWindow.document.close();
    newWindow.print();
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map(key => (
          <div key={key}>
            <label>{key}</label>
            <input type="number" name={key} onChange={handleChange} required />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>

      {result && (
        <div ref={reportRef}>
          <h2>Prediction: {result}</h2>
          <h3>Submitted Data:</h3>
          <ul>
            {Object.entries(formData).map(([key, value]) => (
              <li key={key}><strong>{key}</strong>: {value}</li>
            ))}
          </ul>
        </div>
      )}

      {result && <button onClick={handlePrint}>🖨 Print Report</button>}
    </div>
  );
};

export default Form;