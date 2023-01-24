import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Fraud Detection App",layout="centered",initial_sidebar_state="expanded")

st.title('Fraud Detection App')
st.image('https://www.bing.com/images/search?view=detailV2&ccid=Kd4S7FUp&id=16831012D45778BCE4591F0CF99542F3C5D42516&thid=OIP.Kd4S7FUpa3aYRmBQJPd_jwHaF5&mediaurl=https%3a%2f%2fi2.wp.com%2fdailyfintech.com%2fwp-content%2fuploads%2f2017%2f07%2ffraud-detection.png%3fresize%3d546%252C435%26ssl%3d1&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.29de12ec55296b769846605024f77f8f%3frik%3dFiXUxfNClfkMHw%26pid%3dImgRaw%26r%3d0&exph=435&expw=546&q=fraud+detection+imge&simid=608042480637603277&FORM=IRPRST&ck=A136C740205184A5496D86F177871C81&selectedIndex=15&ajaxhist=0&ajaxserp=0')

# Take inputs from user

amt = st.number_input("Transaction Amount")

amount_std= st.number_input("Amount StandardDevation")

hour = st.slider("Hour", 0, 23)

month= st.selectbox ("month",range(1,12))


# Convert inputs to DataFrame
df_new = pd.DataFrame({'amt': [amt], 'amount_std': [amount_std], 'hour': [hour],'month':[month]})

# Load the transformer
transformer = pkl.load(open('transformer.pkl', 'rb'))

# Apply the transformer on the inputs
X_new = transformer.transform(df_new)

# Load the model
loaded_model = pkl.load(open('final_project.pkl', 'rb'))

# Predict the output
fra = loaded_model.predict(X_new)


if st.button("Predict"): 
    if fra == 1:
        st.error('Warning! The Transaction is Fraud')
    elif fra ==0:
        st.success('Normal Transaction')

        

st.sidebar.subheader("About App")
st.sidebar.info("This web app is helps you to know if your transactions are fraud or not.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have fraud or normal transaction")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
    st.header("Thank you for rating the app!")



