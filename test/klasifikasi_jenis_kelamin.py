# Hermon Jay 14-10-2017
# klasifikasi jenis kelamin dengan 
# Decision Tree, SVM, KNN, dan Naive Bayes

from sklearn import tree
from sklearn import svm
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
import numpy as np 

# model untuk ketiga classifier
cDT = tree.DecisionTreeClassifier()
cSVM = svm.SVC()
cKNN = neighbors.KNeighborsClassifier()
cNB = GaussianNB()

# data latih
# [tingi, berat, ukuran_sepatu]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42],
     [181, 85, 43]]

Y = ['pria', 'pria', 'wanita', 'wanita', 'pria', 'pria', 'wanita', 'wanita',
     'wanita', 'pria', 'pria']

# latih classifier
cDT = cDT.fit(X, Y)
cSVM = cSVM.fit(X, Y)
cKNN = cKNN.fit(X, Y)
cNB = cNB.fit(X, Y)

# data test
X_test = [[198, 92, 48], [184, 84, 44], [183, 83, 44], [166, 47, 36],
         [170, 60, 38], [172, 64, 39], [182, 80, 42], [180, 80, 43]]
Y_test = ['pria', 'pria', 'pria', 'wanita', 'wanita', 'wanita', 'pria', 'pria']
#X_test=np.array(float(input("type some number based on age, weight, and shoes size :", )))
# prediksi data test
Y_DT = cDT.predict(X_test)
Y_SVM = cSVM.predict(X_test)
Y_KNN = cKNN.predict(X_test)
Y_NB = cNB.predict(X_test)

print ('type of X_test {}'.format(type(X_test)))
# print prediksi
print("Prediksi Decision Tree : ", Y_DT)
print("Prediksi SVM : ", Y_SVM)
print("Prediksi KNN : ", Y_KNN)
print("Prediksi Naive Bayes : ", Y_NB)
	
# print akurasi
print("Akurasi Decision Tree : ", accuracy_score(Y_test, Y_DT))
print("Akurasi SVM : ", accuracy_score(Y_test, Y_SVM))
print("Akurasi KNN : ", accuracy_score(Y_test, Y_KNN))
print("Akurasi Naive Bayes : ", accuracy_score(Y_test, Y_NB))