import streamlit as st
import numpy as np
import pandas as pd
from sklearn import linear_model, datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt
import operator

def data_generator():
    random_numbers_x = np.random.randn(150)
    random_numbers_y = [i + np.random.random()* (np.random.randint(3, 13)*np.random.random()) for i in random_numbers_x]
    dataset = pd.DataFrame({"x":random_numbers_x, "y": random_numbers_y})
    return dataset

def data_generator2():
    np.random.seed(0)
    x = 2 - 3 * np.random.normal(0, 1, 20)
    y = x - 2 * (x ** 2) + 0.5 * (x ** 3) + np.random.normal(-3, 3, 20)
    # transforming the data to include another axis
    x = x[:, np.newaxis]
    y = y[:, np.newaxis]
    return x, y 

def get_data():
    X, y = datasets.load_diabetes(return_X_y=True)
    X = X[:, np.newaxis, 2]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, y_train, X_test, y_test

def linear_regression(X_train, y_train):

    lr = linear_model.LinearRegression()

    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)

    errors = {'coef': [i for i in lr.coef_][0], 'mse': mean_squared_error(y_test, y_pred), 'r2':r2_score(y_test, y_pred)}
    return y_pred, errors

def ridge_regression(X_train, y_train, alpha):

    rr = linear_model.Ridge(alpha=alpha)
    
    rr.fit(X_train, y_train)
    y_pred = rr.predict(X_test)

    errors = {'coef': [i for i in rr.coef_][0], 'mse': mean_squared_error(y_test, y_pred), 'r2':r2_score(y_test, y_pred)}
    return y_pred, errors

def poly_regression(x, y, degree):
    polynomial_features= PolynomialFeatures(degree=degree)
    x_poly = polynomial_features.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)
    y_poly_pred = model.predict(x_poly)

    rmse = np.sqrt(mean_squared_error(y,y_poly_pred))
    r2 = r2_score(y,y_poly_pred)


    errors = {'rmse': rmse, 'r2':r2}
    return y_poly_pred, errors

st.title("Machine Learning Playground")

st.write("""
Merhaba herkese, çeşitli ML algoritmalarını çok iyi bir şekilde öğreneceksiniz""")

st.write("""## Gözetimli Öğrenme
Denetimli öğrenme , bir girdiyi örnek girdi-çıktı çiftlerine dayalı olarak çıktıyla eşleyen bir işlev öğrenmeyi içerir.
Örneğin, yaş (girdi) ve yükseklik (çıktı) olmak üzere iki değişkenli bir veri kümem olsaydı, bir kişinin yaşına göre yüksekliğini tahmin etmek için denetimli bir öğrenme modeli uygulayabilirim.


## Regresyon Modelleri

Regresyon modellerinde çıktı süreklidir. Aşağıda en yaygın regresyon modellerinden bazıları verilmiştir.""")


st.subheader("Linear Regression")
st.write("""Doğrusal regresyon fikri, sadece verilere en uygun çizgiyi bulmaktır. Doğrusal regresyonun uzantıları arasında çoklu doğrusal regresyon (örn. En uygun düzlemi bulma) ve polinom regresyonu (örn. En uygun eğri bulma) bulunur.""")
st.latex("y(w,x) = w0+w1x1+...wpxp")

# Get Data for all models
X_train, y_train, X_test, y_test = get_data()


################## Linear Regression #################


lr_preds, lr_errors = linear_regression(X_train, y_train)

# Linear Regression Plots
plt.scatter(x=X_train, y=y_train, color="black")
plt.plot(X_test, lr_preds, color="blue", linewidth=3)
st.write(lr_errors)
st.pyplot()


################## Ridge Regression ###################
st.subheader("Ridge Regression")

# Adjust Alpha Parameter
alpha = st.slider("Alpha", 0.0, 1.0, 0.5, 0.1)

# Run model
rr_preds, rr_errors = ridge_regression(X_train, y_train, alpha)

# Ridge Regression Plots
plt.scatter(x=X_train, y=y_train, color="black")
plt.plot(X_test, rr_preds, color="blue", linewidth=3)
st.write(rr_errors)
st.pyplot()

################## Ridge Regression ###################
st.subheader("Poly Regression")

# Adjust Alpha Parameter
degree = st.slider("Degree", 2, 10, 2, 1)

# Run model
pr_x, pr_y = data_generator2()
pr_preds, pr_errors = poly_regression(pr_x, pr_y, degree)

# Ridge Regression Plots
plt.scatter(pr_x, pr_y, s=10)

sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(pr_x, pr_preds), key=sort_axis)
pr_x, pr_preds = zip(*sorted_zip)
plt.plot(pr_x, pr_preds, color='m')

st.write(pr_errors)
st.pyplot()