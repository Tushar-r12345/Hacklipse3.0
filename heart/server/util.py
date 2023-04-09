import json
import pickle
import numpy as np
# import joblib

__previous_illness=None
__cardiac_CT=None
__model1=None
__model2=None
__data_columns=None
__diagnosis=None
__treatment=None

# location.lower() ki location ko lower case mein kar de
def get_predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic,
                    Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender):
    # Initialize x array with zeros of length equal to number of columns in X
    try:
        loc_index1=__data_columns.index(previous_illness.lower())
        loc_index2=__data_columns.index(cardiac_CT.lower())

    except:
        loc_index1=-1
        loc_index2=-1

    x = np.zeros(len(__data_columns))

    # Find the index of Cardiac_CT and Previous_illnesses in the X.columns array
    # loc_index1 = np.where(X.columns == Previous_illnesses)[0][0]
    # loc_index2 = np.where(X.columns == Cardiac_CT)[0][0]

    # Set the corresponding feature values in the x array
    x[2] = Age
    x[3] = Chest_pain
    x[4] = Shortness_of_breath
    x[5] = Systolic
    x[6] = Diastolic
    x[7] = Heart_rate
    x[8] = Cholesterol_level
    x[9] = Diabetes
    x[10] = Hypertension
    x[11] = Smoking
    x[12] = Obesity
    x[13] = Gender

    # Set the values of the Cardiac_CT and Previous_illnesses features to 1
    if loc_index1 > 0:
        x[loc_index1] = 1
    if loc_index2 > 0:
        x[loc_index2] = 1

    # Use the trained random forest classifier model to predict the diagnosis
    prediction1 = __model1.predict([x])[0]
    prediction2 = __model2.predict([x])[0]

    # Look up the original value
    original_value1 = __diagnose_mapping[str(prediction1)]
    original_value2 = __treatment_mapping[str(prediction2)]

    return {"Diagnosis": original_value1, "treatment" : original_value2}

# def predict_disease(previous_illness, cardiac_CT, Age, Chest_pain, Shortness_of_breath, Systolic, Diastolic,
#                     Heart_rate, Cholesterol_level, Diabetes, Hypertension, Smoking, Obesity, Gender):
#     # Initialize x array with zeros of length equal to number of columns in X
#     try:
#         loc_index1=__data_columns.index(previous_illness.lower())
#         loc_index2=__data_columns.index(cardiac_CT.lower())
#
#     except:
#         loc_index1=-1
#         loc_index2=-1
#
#     x = np.zeros(len(__data_columns))
#
#     # Find the index of Cardiac_CT and Previous_illnesses in the X.columns array
#     # loc_index1 = np.where(X.columns == Previous_illnesses)[0][0]
#     # loc_index2 = np.where(X.columns == Cardiac_CT)[0][0]
#
#     # Set the corresponding feature values in the x array
#     x[2] = Age
#     x[3] = Chest_pain
#     x[4] = Shortness_of_breath
#     x[5] = Systolic
#     x[6] = Diastolic
#     x[7] = Heart_rate
#     x[8] = Cholesterol_level
#     x[9] = Diabetes
#     x[10] = Hypertension
#     x[11] = Smoking
#     x[12] = Obesity
#     x[13] = Gender
#
#     # Set the values of the Cardiac_CT and Previous_illnesses features to 1
#     if loc_index1 > 0:
#         x[loc_index1] = 1
#     if loc_index2 > 0:
#         x[loc_index2] = 1
#
#     # Use the trained random forest classifier model to predict the diagnosis
#     __model1.predict([x])[0]
#     __model2.predict([x])[0]
#
#     # # Example encoded result
#     # encoded_result1 = diagnosis
#     # encoded_result2 = treatment
#
#     # Look up the original value
#     original_value1 = __diagnose_mapping[str(__model1.predict([x])[0])]
#     original_value2 = __treatment_mapping[str(__model2.predict([x])[0])]
#
#     # return original_value1
#     return {"Diagnosis": original_value1, "treatment" : original_value2}
#     # return {original_value1,original_value2}
#     # print("diagnosis : ",original_value1)
#     # print("Diagnosis : ",original_value1)
#     # print("Treatment : ",original_value2)


def get_previous_illness():
    return __previous_illness

def get_cardiac_CT():
    return __cardiac_CT

def load_saved_artifacts():
    print("loading saved artifacts")
    global __columnns_final
    global __previous_illness
    global __cardiac_CT
    global __diagnose_mapping
    global __treatment_mapping
    global __data_columns
    global __data_columns2
    global __data_columns3

    with open("./artifacts/columns_final2.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        # idhar niche [3:] ka matlab hai jo data cols mein save kara hai waha se saare cols le lo kyuki humne locations par one hot encoding kari hai
        __previous_illness = __data_columns[12:18]
        __cardiac_CT = __data_columns[18:]

    with open("./artifacts/inverse_mapping_diagnose.json",'r') as f:
        __data_columns2 = json.load(f)
        __diagnose_mapping = __data_columns2["diagnose"]

    with open("./artifacts/inverse_mapping_treatment.json",'r') as f:
        __data_columns3=json.load(f)
        __treatment_mapping = __data_columns3["treatment"]

    global __model1
    global __model2

    with open("./artifacts/rfc_model_diagnosis2.pickle",'rb') as f:
        __model1 = pickle.load(f)

    with open("./artifacts/rfc_model_treatment2.pickle",'rb') as f:
        __model2 = pickle.load(f)
    print("loading saved artifacts........")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_previous_illness())
    print(get_cardiac_CT())
    print(get_predict_disease('no serious illness','shows pericarditis with myocarditis',30,1,0,130,80,100,220,0,1,1,0,0))
    print(get_predict_disease('no serious illness','25% - 45% dilation of the infrarenal aorta',65,1,1,130,80,100,220,0,1,1,0,1))
    print(get_predict_disease('no serious illness','none',50,1,1,155,105,100,210,0,1,1,0,0))
    print(get_predict_disease('mitral valve replacement surgery','none',65,1,1,130,80,110,215,0,1,1,0,0))
    print(get_predict_disease('no serious illness','severe stenosis in the mitral valve',62,1,1,120,80,100,200,0,0,0,0,1))