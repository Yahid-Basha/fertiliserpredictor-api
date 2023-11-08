# Fertilizer Predictor API

Welcome to the Fertilizer Predictor API repository! This project is an API service designed to predict the most suitable fertilizer for a given crop based on various soil parameters. The API is currently deployed and can be accessed at [https://fertiliserprediction.onrender.com/predict](https://fertiliserprediction.onrender.com/predict).

## Overview

The Fertilizer Predictor API leverages a trained machine learning model to provide fertilizer recommendations. It takes into account factors such as crop type, soil moisture, and the content of nitrogen, potassium, and phosphorous in the soil.

## Repository Contents

- `application.py`: The main Flask application file that defines the API endpoints and the logic for predictions.
- `model.pkl`: A pickle file containing the trained machine learning model.
- `crop_encoder.pkl`, `fertilizer_encoder.pkl`, `label_encoder.pkl`: Serialized label encoders for converting categorical data into a machine-readable format.
- `npklong.csv`: The dataset file that was used to train the machine learning model.
- `requirements.txt`: This file lists all the Python dependencies required to run the project.

## API Testing through Postman
<img width="1245" alt="image" src="https://github.com/Yahid-Basha/fertiliserpredictor/assets/97111767/b2f8e08b-cd51-47c5-9b0c-74a81d60df18">




## API Usage

### Using JavaScript

You can interact with the API using JavaScript by sending a POST request with the appropriate headers and body. Below is an example of how you can do this using the Fetch API:

```javascript
// Define the API endpoint
const apiUrl = 'https://fertiliserprediction.onrender.com/predict';

// Create the data object with the parameters for the prediction
const data = {
  crop_type: "Wheat",
  moisture: 10,
  nitrogen: 10,
  potassium: 10,
  phosphorous: 10
};

// Use the fetch API to send a POST request to the server
fetch(apiUrl, {
  method: 'POST', // Specify the method
  headers: {
    'Content-Type': 'application/json', // Specify the content type as JSON
  },
  body: JSON.stringify(data), // Convert the JavaScript object to a JSON string
})
.then(response => response.json()) // Parse the JSON response
.then(data => {
  console.log('Success:', data); // Log the success response
})
.catch((error) => {
  console.error('Error:', error); // Log any errors
});
```
This script will send the crop and soil parameters to the API and log the predicted fertilizer type to the console.

## Local Setup

To run this project locally:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Start the Flask application by executing `python application.py`.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
