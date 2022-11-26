import pickle
import streamlit as st
import pandas as pd

pickle_in = open('C:/Users/Sushri Supravat/fraud/fraud.pkl', 'rb')
model = pickle.load(pickle_in)

def fraud(Age, Gender, Nr_Deposits_Approved, Nr_Deposits_Rejected,
        Total_Pending_Deposits , Nr_Bets_Sports,
        Nr_Distinct_Payment_Methods, Nr_days_without_activity): 
    
    if Gender == 'M':
        Gender = 1
    else:
        Gender = 0
        
        
    prediction = model.predict([[Age, Gender, Nr_Deposits_Approved, Nr_Deposits_Rejected,
            Total_Pending_Deposits , Nr_Bets_Sports,
            Nr_Distinct_Payment_Methods, Nr_days_without_activity]])
    
    
    return prediction

def main():
    html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Fraud Detection </h1> 
    </div> 
    """
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    Age = st.slider('Age', 18, 50)
    
    Gender = st.selectbox('Gender', ['M', 'F'])
    
    Nr_Deposits_Approved = st.slider('Deposit Approved', 1, 7)
    
    Nr_Deposits_Rejected = st.slider('Deposits Rejected', 1, 7)
    
    Total_Pending_Deposits = st.slider('Total Pending Deposits (INR)', 2000, 15000)
    
    Nr_Bets_Sports = st.slider('Number of Bets Sports', 1, 10)
    
    Nr_Distinct_Payment_Methods = st.slider('Number of Payment Modes', 1, 4)
    
    Nr_days_without_activity = st.slider('Days without activity', 1, 365)
    
    result = ''
    
    if st.button('Predict'):
        result = fraud(Age, Gender, Nr_Deposits_Approved, Nr_Deposits_Rejected,
                       Total_Pending_Deposits , Nr_Bets_Sports,
                       Nr_Distinct_Payment_Methods, Nr_days_without_activity)
        
        if result == 0:
            st.success('The Transactions is Not Fraud')
    
        else:
        
            st.success('The Transactions is Fraud')
        
        
if __name__ == '__main__':
    main()

    