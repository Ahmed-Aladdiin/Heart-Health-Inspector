# %%
print('If you don\'t have joblib, then you will need to install it first.')
print('just type "pip install joblib" into the terminal.\n')

# %%
import joblib
import pandas as pd

# %%
# column names
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

# %%
# preprocess the data before using the model
def preprocess_data(data):
  """
  data: a data-frame of the test data 
  """

  # the preprocessor includes One-Hot encoding and StandardScalar
  preprocessor = joblib.load('./model/preprocessor.pkl')
  
  # Deal with the large number of zero values
  data['Zero_Oldpeak'] = (data['Oldpeak'] == 0).astype(int)
  data['Have_Cholesterol_Measurement'] = (data['Cholesterol'] == 0).astype(int)

  # Map Sex(M, F) -> Sex(0, 1) and ExerciseAngina(N, Y) -> ExerciseAngina(0, 1)
  binary_categorical_non_numerical = ['Sex', 'ExerciseAngina']
  data[binary_categorical_non_numerical] = data[binary_categorical_non_numerical].apply(
    lambda x: pd.factorize(x)[0])

  # Preserve the names of the column that won't be preprocessed
  remaining_features = ['Sex', 'FastingBS', 'ExerciseAngina', 'Zero_Oldpeak', 'Have_Cholesterol_Measurement']
  # Preprocess the data, apply StandardScaler and One-Hot encoder
  x_processed = preprocessor.transform(data)

  # Return it to a data frame
  x_df_processed = pd.DataFrame(x_processed, columns=columns)

  # Concat the remaining columns, first reset the index then concat
  x_df_processed = x_df_processed.reset_index(drop=True)
  x_df_remaining = data[remaining_features].reset_index(drop=True)
  x_df_processed = pd.concat([x_df_processed, x_df_remaining], axis=1)

  return x_df_processed

# %%
# Initialize and load the model
model = joblib.load('./model/heart_disease_model.pkl')

# %%
# ask the using to input the test-case file name
test_case_file = input("input test-case file name: (default ./test.csv)")
if test_case_file is None or test_case_file == '':
  test_case_file = './test.csv'
test_data = pd.read_csv(test_case_file)
# test_data.head()

# %%
# Preprocess the data
test_data = preprocess_data(test_data)
# test_data.head()

# %%
target_predict = model.predict(test_data)

# %%
target_predict = pd.DataFrame(target_predict, columns=['HeartDisease_Prediction'])
# target_predict.head()

# %%
output_file = input('output file name: (default ./prediction.csv)')
if output_file is None or output_file == '':
  output_file = './prediction.csv'
target_predict.to_csv(output_file, index=False)


