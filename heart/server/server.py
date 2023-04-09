# from flask import Flask, request, jsonify
#
# import util
#
# app = Flask(__name__)
#
# @app.route('/get_previous_illness',methods=['GET'])
# def get_previous_illness():
#     response=jsonify({
#         'previous_illness': util.get_previous_illness()
#     })
#     response.headers.add('Access-Control-Allow-origin','*')
#     return response
#
# @app.route('/get_cardiac_CT',methods=['GET'])
# def get_cardiac_CT():
#     response=jsonify({
#         'previous_illness': util.get_cardiac_CT()
#     })
#     response.headers.add('Access-Control-Allow-origin','*')
#     return response
#
#
# @app.route('/predict_disease',methods=['GET','POST'])
# def predict_disease():
#     previous_illness = request.form['previous_illness']
#     cardiac_CT = request.form['cardiac_CT']
#     Age = int(request.form['Age'])
#     Chest_pain = int(request.form['Chest_pain'])
#     Shortness_of_breath = int(request.form['Shortness_of_breath'])
#     Systolic = int(request.form['Systolic'])
#     Diastolic = int(request.form['Diastolic'])
#     Heart_rate = int(request.form['Heart_rate'])
#     Cholesterol_level = int(request.form['Cholesterol_level'])
#     Diabetes = int(request.form['Diabetes'])
#     Hypertension = int(request.form['Hypertension'])
#     Smoking = int(request.form['Smoking'])
#     Obesity = int(request.form['Obesity'])
#     Gender = int(request.form['Gender'])
#
#     response = jsonify({
#         'predict_disease': util.predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic,
#                     Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
#
#
#
# def hello():
#     return "hiii"
#
# if __name__=="__main__":
#     print("starting server......")
#     util.load_saved_artifacts()
#     app.run()

# from flask import Flask, request, jsonify
# import util
#
# app = Flask(__name__)
#
# @app.route('/get_previous_illness',methods=['GET'])
# def get_previous_illness():
#     response = jsonify({
#         'previous_illness': util.get_previous_illness()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/get_cardiac_CT',methods=['GET'])
# def get_cardiac_CT():
#     response = jsonify({
#         'cardiac_CT': util.get_cardiac_CT()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/predict_disease',methods=['POST'])
# def predict_disease():
#     previous_illness = request.form['previous_illness']
#     cardiac_CT = request.form['cardiac_CT']
#     Age = int(request.form['Age'])
#     Chest_pain = int(request.form['Chest_pain'])
#     Shortness_of_breath = int(request.form['Shortness_of_breath'])
#     Systolic = int(request.form['Systolic'])
#     Diastolic = int(request.form['Diastolic'])
#     Heart_rate = int(request.form['Heart_rate'])
#     Cholesterol_level = int(request.form['Cholesterol_level'])
#     Diabetes = int(request.form['Diabetes'])
#     Hypertension = int(request.form['Hypertension'])
#     Smoking = int(request.form['Smoking'])
#     Obesity = int(request.form['Obesity'])
#     Gender = int(request.form['Gender'])
#
#     response = jsonify({
#         'predict_disease': util.predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic,
#                     Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response
#
# if __name__ == '__main__':
#     print("starting server......")
#     util.load_saved_artifacts()
#     app.run()

from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/get_previous_illness', methods=['GET'])
def get_previous_illness():
    response = jsonify({
        'previous_illness': util.get_previous_illness()
    })
    return response

@app.route('/get_cardiac_CT', methods=['GET'])
def get_cardiac_CT():
    response = jsonify({
        'cardiac_CT': util.get_cardiac_CT()
    })
    return response

@app.route('/predict_disease', methods=['POST'])
def predict_disease():
    previous_illness = request.form['previous_illness']
    cardiac_CT = request.form['cardiac_CT']
    Age = request.form['Age']
    Chest_pain = request.form['Chest_pain']
    Shortness_of_breath = request.form['Shortness_of_breath']
    Systolic = request.form['Systolic']
    Diastolic = request.form['Diastolic']
    Heart_rate = request.form['Heart_rate']
    Cholesterol_level = request.form['Cholesterol_level']
    Diabetes = request.form['Diabetes']
    Hypertension = request.form['Hypertension']
    Smoking = request.form['Smoking']
    Obesity = request.form['Obesity']
    Gender = request.form['Gender']

    response = jsonify({
        'predicted_disease_output': util.get_predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic, Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)
    })

    return response

if __name__ == "__main__":
    print("starting server......")
    util.load_saved_artifacts()
    app.run()


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import util
# app = Flask(__name__)
# CORS(app)
#
# @app.route('/get_previous_illness',methods=['GET'])
# def get_previous_illness():
#     response=jsonify({
#         'previous_illness': util.get_previous_illness()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/get_cardiac_CT',methods=['GET'])
# def get_cardiac_CT():
#     response=jsonify({
#         'cardiac_CT': util.get_cardiac_CT()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/predict_disease',methods=['POST'])
# def predict_disease():
#     previous_illness = request.form['previous_illness']
#     cardiac_CT = request.form['cardiac_CT']
#     Age = int(request.form['Age'])
#     Chest_pain = int(request.form['Chest_pain'])
#     Shortness_of_breath = int(request.form['Shortness_of_breath'])
#     Systolic = int(request.form['Systolic'])
#     Diastolic = int(request.form['Diastolic'])
#     Heart_rate = int(request.form['Heart_rate'])
#     Cholesterol_level = int(request.form['Cholesterol_level'])
#     Diabetes = int(request.form['Diabetes'])
#     Hypertension = int(request.form['Hypertension'])
#     Smoking = int(request.form['Smoking'])
#     Obesity = int(request.form['Obesity'])
#     Gender = int(request.form['Gender'])
#
#     response = jsonify({
#         'predict_disease': util.predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic, Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# if __name__=="__main__":
#     print("starting server......")
#     util.load_saved_artifacts()
#     app.run()

# from flask import Flask, request, jsonify
# import util
#
# app = Flask(__name__)
#
# @app.route('/get_previous_illness',methods=['GET'])
# def get_previous_illness():
#     response=jsonify({
#         'previous_illness': util.get_previous_illness()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/get_cardiac_CT',methods=['GET'])
# def get_cardiac_CT():
#     response=jsonify({
#         'cardiac_CT': util.get_cardiac_CT()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/predict_disease',methods=['POST'])
# def predict_disease():
#     previous_illness = request.form['previous_illness']
#     cardiac_CT = request.form['cardiac_CT']
#     Age = int(request.form['Age'])
#     Chest_pain = int(request.form['Chest_pain'])
#     Shortness_of_breath = int(request.form['Shortness_of_breath'])
#     Systolic = int(request.form['Systolic'])
#     Diastolic = int(request.form['Diastolic'])
#     Heart_rate = int(request.form['Heart_rate'])
#     Cholesterol_level = int(request.form['Cholesterol_level'])
#     Diabetes = int(request.form['Diabetes'])
#     Hypertension = int(request.form['Hypertension'])
#     Smoking = int(request.form['Smoking'])
#     Obesity = int(request.form['Obesity'])
#     Gender = int(request.form['Gender'])
#
#     response = jsonify({
#         'predict_disease': util.predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic, Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     # response.headers.add('Access-Control-Allow-Headers', '*')
#
#     return response
#
# if __name__=="__main__":
#     print("starting server......")
#     util.load_saved_artifacts()
#     app.run()

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import util
#
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
#
# @app.route('/get_previous_illness',methods=['GET'])
# def get_previous_illness():
#     response=jsonify({
#         'previous_illness': util.get_previous_illness()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/get_cardiac_CT',methods=['GET'])
# def get_cardiac_CT():
#     response=jsonify({
#         'cardiac_CT': util.get_cardiac_CT()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# @app.route('/predict_disease',methods=['GET','POST'])
# def predict_disease():
#     previous_illness = request.form['previous_illness']
#     cardiac_CT = request.form['cardiac_CT']
#     Age = int(request.form['Age'])
#     Chest_pain = int(request.form['Chest_pain'])
#     Shortness_of_breath = int(request.form['Shortness_of_breath'])
#     Systolic = int(request.form['Systolic'])
#     Diastolic = int(request.form['Diastolic'])
#     Heart_rate = int(request.form['Heart_rate'])
#     Cholesterol_level = int(request.form['Cholesterol_level'])
#     Diabetes = int(request.form['Diabetes'])
#     Hypertension = int(request.form['Hypertension'])
#     Smoking = int(request.form['Smoking'])
#     Obesity = int(request.form['Obesity'])
#     Gender = int(request.form['Gender'])
#
#     response = jsonify({
#         'predict_disease': util.predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic, Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response
#
# if __name__=="__main__":
#     print("starting server......")
#     util.load_saved_artifacts()
#     app.run()

# from flask import Flask, request, jsonify
# import util
#
# app = Flask(__name__)
#
# # enable CORS
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response
#
# @app.route('/get_previous_illness', methods=['GET'])
# def get_previous_illness():
#     response = jsonify({'previous_illness': util.get_previous_illness()})
#     return response
#
# @app.route('/get_cardiac_CT', methods=['GET'])
# def get_cardiac_CT():
#     response = jsonify({'cardiac_CT': util.get_cardiac_CT()})
#     return response
#
# @app.route('/predict_disease', methods=['POST'])
# def predict_disease():
#     data = request.get_json(force=True)
#     previous_illness = data['previous_illness']
#     cardiac_CT = data['cardiac_CT']
#     Age = int(data['Age'])
#     Chest_pain = int(data['Chest_pain'])
#     Shortness_of_breath = int(data['Shortness_of_breath'])
#     Systolic = int(data['Systolic'])
#     Diastolic = int(data['Diastolic'])
#     Heart_rate = int(data['Heart_rate'])
#     Cholesterol_level = int(data['Cholesterol_level'])
#     Diabetes = int(data['Diabetes'])
#     Hypertension = int(data['Hypertension'])
#     Smoking = int(data['Smoking'])
#     Obesity = int(data['Obesity'])
#     Gender = int(data['Gender'])
#
#     response = jsonify({'predict_disease': util.predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic, Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender)})
#     return response
#
# if __name__ == "__main__":
#     print("Starting Python Flask server for Heart Disease Prediction...")
#     util.load_saved_artifacts()
#     app.run()
#
#
