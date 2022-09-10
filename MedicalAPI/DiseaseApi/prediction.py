import numpy as np
import pandas as pd

def disease_prediction(psymptoms):

    disease_set = {}
    file_path = "C:\\Users\\Amrtya srivastav\\PycharmProjects\\MedicalApi\\DiseaseApi\\"
    def DecisionTree(psymptoms):
        from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
        clf3 = clf3.fit(X, y)

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = clf3.predict(X_test)
        #     print('Accuracy:-',accuracy_score(y_test, y_pred))
        #     print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        for k in range(0, len(l1)):
            # print (k,)
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]

        predict = clf3.predict(inputtest)
        predicted = predict[0]
        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            return disease[a], accuracy_score(y_test, y_pred)
        else:
            return "Not Found"

    def LogisticReg(psymptoms):
        from sklearn.linear_model import LogisticRegression
        clf4 = LogisticRegression()
        clf4 = clf4.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = clf4.predict(X_test)
        #     print('Accuracy:-',accuracy_score(y_test, y_pred))
        #     print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted = predict[0]
        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            return disease[a], accuracy_score(y_test, y_pred)
        else:
            return "Not Found"

    def knn(psymptoms):
        from sklearn.neighbors import KNeighborsClassifier
        knnobj = KNeighborsClassifier()
        knnobj = knnobj.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = knnobj.predict(X_test)
        #     print('Accuracy:-',accuracy_score(y_test, y_pred))
        #     print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = knnobj.predict(inputtest)
        predicted = predict[0]
        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            return disease[a], accuracy_score(y_test, y_pred)
        else:
            return "Not Found"

    def NaiveBayes(psymptoms):
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb = gnb.fit(X, np.ravel(y))

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred = gnb.predict(X_test)

        '''
        accuracy = total no. of correct prediction / total no. of prediction 
        '''
        #     print('Accuracy:-',accuracy_score(y_test, y_pred))
        #     print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        for k in range(0, len(l1)):
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted = predict[0]
        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        if (h == 'yes'):
            return disease[a], accuracy_score(y_test, y_pred)
        else:
            return "Not Found"

    l1 = ['back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine',
          'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach',
          'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation',
          'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs',
          'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool',
          'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs',
          'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails',
          'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips',
          'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints',
          'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness',
          'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine',
          'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)',
          'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain',
          'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria',
          'family history', 'mucoid sputum',
          'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion',
          'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen',
          'history of alcohol consumption', 'fluid overload', 'blood in sputum', 'prominent veins on calf',
          'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling',
          'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose',
          'yellow crust ooze']

    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
               'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis',
               'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
               'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
               'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
               'Impetigo']

    # Prepare empty List as per the range of symptoms
    l2 = []
    for x in range(0, len(l1)):
        l2.append(0)

    # Reading Training data from CSV

    df1 = pd.read_csv(file_path+"Training.csv")
    column = []
    for i in df1.columns:
        column.append(i.replace("_", " "))
    df = pd.read_csv(file_path+'Training.csv', header=None, skiprows=1, names=column)

    df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                              'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                              'Bronchial Asthma': 9, 'Hypertension ': 10,
                              'Migraine': 11, 'Cervical spondylosis': 12,
                              'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                              'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                              'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                              'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                              'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                              'Varicose veins': 30, 'Hypothyroidism': 31,
                              'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                              '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                              'Psoriasis': 39,
                              'Impetigo': 40}}, inplace=True)

    # print(df.head())
    # Create Feature and Label Matrix -

    X = df[l1]
    y = df[["prognosis"]]
    np.ravel(y)

    # TRAINING DATA
    tr1 = pd.read_csv(file_path+"Testing.csv")
    column_test = []
    for i in tr1.columns:
        column_test.append(i.replace("_", " "))
    tr = pd.read_csv(file_path+'Testing.csv', header=None, skiprows=1, names=column_test)
    tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                              'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                              'Bronchial Asthma': 9, 'Hypertension ': 10,
                              'Migraine': 11, 'Cervical spondylosis': 12,
                              'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                              'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                              'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                              'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                              'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                              'Varicose veins': 30, 'Hypothyroidism': 31,
                              'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                              '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                              'Psoriasis': 39,
                              'Impetigo': 40}}, inplace=True)

    X_test = tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)

    d, c = NaiveBayes(psymptoms)
    dl, cl = LogisticReg(psymptoms)
    dd, cd = DecisionTree(psymptoms)
    dk, ck = knn(psymptoms)
    # print(d, c, '\n', '\n', dd, cd, '\n', dk, ck)
    # print(d)
    return d,dl,dd,dk