import joblib
import pandas as pd

columns = [
    'Age', 
    'RestingBP', 
    'Cholesterol', 
    'MaxHR', 
    'Oldpeak', 
    'ChestPainType_ASY', 
    'ChestPainType_ATA', 
    'ChestPainType_NAP', 
    'ChestPainType_TA', 
    'RestingECG_LVH', 
    'RestingECG_Normal', 
    'RestingECG_ST', 
    'ST_Slope_Down', 
    'ST_Slope_Flat', 
    'ST_Slope_Up'
]

# Define the preprocessing for the input image
def preprocess_data(data):
    """
    data: a map of the data sent by the form
    """
    preprocessor = joblib.load('./app_ml/model/preprocessor.pkl')
    
    # Form tha data into a map of the right shape and column names
    x = {
        'RestingBP': [int(data['restingBP'])],
        'Cholesterol': [int(data['cholesterol'])],
        'MaxHR': [int(data['maxHR'])],
        'Oldpeak': [float(data['oldpeak'])],
        'Age': [int(data['age'])],
        'ChestPainType': [data['chestPainType']],
        'RestingECG': [data['restingECG']],
        'ST_Slope': [data['st_slope']]
    }

    # Create a data frame of the data
    x_df = pd.DataFrame(x)

    # Preprocess the data, apply StandardScaler and One-Hot encoder
    x_processed = preprocessor.transform(x_df)

    # Return it to a data frame
    x_df_processed = pd.DataFrame(x_processed, columns=columns)

    # Add the remaining columns
    x_df_processed['Sex'] = [int(data['gender'] == 'F')]
    x_df_processed['FastingBS'] = [int(data['fastingBS'])]
    x_df_processed['ExerciseAngina'] = [int(data['exerciseAngina'] == 'Y')]
    x_df_processed['Zero_Oldpeak'] = [int(data['oldpeak'] == 0)]
    x_df_processed['Have_Cholesterol_Measurement'] = [int(data['cholesterol'] == '0')]

    return x_df_processed

# Initialize and load the model
model = joblib.load('./app_ml/model/heart_disease_model.pkl')
