// src/components/HeartForm.js (example)
const handleSubmit = async (e) => {
    e.preventDefault();
  
    const formData = {
        "age": 60,
        "sex": 0,
        "cp": 23,
        "trestbps": 140,
        "chol": 540,
        "fbs": 0,
        "restecg": 1,
        "thalach": 150,
        "exang": 23,
        "oldpeak": 1.2,
        "slope": 2,
        "ca": 0,
        "thal": 78
      };
      
      //age: 52,
      //sex: 1,
      //cp: 0,
      //trestbps: 125,
      //chol: 212,
      //fbs: 0
      // Add other features your backend expe;
  
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
  
      const data = await response.json();
      console.log('Prediction:', data);
      // Update state to show result to user
    } catch (error) {
      console.error('Error:', error);
    }
  };
  