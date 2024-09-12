from flask import request, render_template
from app_ml.models import model, preprocess_data
from app_ml import app

@app.route('/')
def index():
  print('here')
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  data = dict(request.form)
  print(data)

  try:
    data_preprocessed = preprocess_data(data)

    predicted_class = model.predict(data_preprocessed)
    prediction = predicted_class[0]

    result_class = None
    image_filename = None
    result_message = None
    additional_message = None

    if prediction == 1:
      result_class = 'warning'
      image_filename = 'warning.png'
      result_message = 'You may have a heart problem.'
      additional_message = 'We recommend visiting a heart doctor as soon as possible'
    else :
      result_class = 'healthy'
      image_filename = 'healthy.png'
      result_message = 'You have a well, strong heart.'
      additional_message = 'Have a healthy and happy life.'

    return render_template('result.html', result_class=result_class,
      image_filename=image_filename, result_message=result_message,
      additional_message = additional_message
    )
  except Exception as e:
    result_class = 'error'
    image_filename = 'error.png'
    result_message = 'An error has occurred.'
    additional_message = 'Please try again later.'

    print('An Error has occurred:' + str(e))
    return render_template('result.html', result_class=result_class,
      image_filename=image_filename, result_message=result_message,
      additional_message = additional_message
    )

