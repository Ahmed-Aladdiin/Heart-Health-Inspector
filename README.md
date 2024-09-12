# Heart Health Inspector
Heart Health Inspector is a machine learning project designed to predict heart disease based on various health metrics. The project includes a web application built with Flask to provide a user-friendly graphical interface for users to input their health data and receive predictions.

## Project Structure
```
.
├── .gitignore
├── app/
│   ├── app_ml/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── app.py
│   ├── dockerfile
│   └── requirements.txt
├── data/
│   ├── cardiovascular_preprocessed_dataset.csv
│   ├── cardiovascular_raw_dataset.csv
│   ├── features_training_data_v2.csv
│   └── features_training_data.csv
├── Building_Models.ipynb
├── Data_Preprocessing.ipynb
├── Exploratory_Data_Analysis.ipynb
├── LICENSE
├── model/
├── test_model.ipynb
└── test_script.py
```

## Notebooks
- Data_Preprocessing.ipynb: Contains the steps to preprocess the raw data.
- Exploratory_Data_Analysis.ipynb: Provides insights into the data through various visualizations.
- Building_Models.ipynb: Details the process of building and training the machine learning models.
- test_model.ipynb: Used for testing the trained models with new data.

## Web Application
- app.py: The main entry point for the Flask application.
- app_ml/: Contains the machine learning model and preprocessing logic.
  - models.py: Defines the model and preprocessing functions.
  - routes.py: Defines the routes for the web application.
  - init.py: Initializes the Flask application.

## Usage
Navigate into the ./app directory inside the project  
`cd app`

### Install Requirements
The required Python packages are listed in requirements.txt. To install them, run:  
```bash
pip install -r requirements.txt
```

## Run the app
1. Run the Web Application:
```bash
python app.py
```
The application will be available at http://localhost:5000.

2. Input Data: Enter your health metrics into the form on the web page and submit to receive a prediction.
3. Test the Model: Use test_script.py to test the model with a CSV file containing test data.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
This project uses various open-source libraries and tools. Special thanks to the contributors of these projects.

---

Feel free to contribute to this project by submitting issues or pull requests. For any questions, please contact the project maintainers.