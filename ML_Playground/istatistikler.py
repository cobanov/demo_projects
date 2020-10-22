import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
from scipy import stats



st.write("# Istatistikler")
st.subheader("Normal Dağılım")
st.latex("""f(x) = {e^{-x^{2}/2}} {\sqrt{2\pi}}""")
def generate_data(mu, sigma, num_sample):
    np.random.seed(0)
    return np.random.normal(mu, sigma, num_sample)

mu = st.slider("Ortalama", -10, 10, 0, 2)
sigma = st.slider("Standart Sapma", 0.1, 10.0, 0.1, 1.0)
num_sample = st.slider("Ornek Sayisi", 100, 1000, 100, 10)

data = generate_data(mu, sigma, num_sample)
sns.kdeplot(data, shade=True)
plt.xlim(-50, 50)
st.pyplot()

st.subheader("Ortalama ve Medyan")
st.write("""Ortalama, Medyan ve Skew:

Bu parametreler şu ve budur.""")
skew = st.slider("Skew", -10, 10, 0, 2)

data = skewnorm.rvs(skew, size=1000)
sns.kdeplot(data, color="orange", shade=True)
plt.vlines([data.mean()], 0, 1, color="blue", linestyles="dashed")
plt.vlines([np.median(data)], 0, 1, color="red", linestyles="dashed")
st.pyplot()