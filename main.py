import streamlit as st
import pandas as pd
import pickle 

def load_model(filename):
  with open(filename, "rb") as file:
    return pickle.load(file)
    

st.title("Customer Churn Prediction")

df = pd.read_csv("churn.csv")

customers = [
    f"{row['CustomerId']} - {row['Surname']}" for _, row in df.iterrows()
]

selected_customer_option = st.selectbox("Select a customer", customers)

if selected_customer_option:
  selected_customer_id = int(selected_customer_option.split(" - ")[0])

print("Selected customer ID:", selected_customer_id)

selected_surname = selected_customer_option.split(" - ")[1]

print("Surname:", selected_surname)

selected_customer = df.loc[df["CustomerId"] == selected_customer_id].iloc[0]

print("Selected Customer:", selected_customer)

col1, col2 = st.columns(2)

with col1:
  # Input for Credit Score
  credit_score = st.number_input("Credit Score",
                                 min_value=300,
                                 max_value=850,
                                 value=int(selected_customer['CreditScore']))

  # Input for Location (Geography)
  location = st.selectbox("Location", ["Spain", "France", "Germany"],
                          index=["Spain", "France", "Germany"
                                 ].index(selected_customer['Geography']))

  # Input for Gender
  gender = st.radio("Gender", ["Male", "Female"],
                    index=0 if selected_customer['Gender'] == 'Male' else 1)

  # Input for Age
  age = st.number_input("Age",
                        min_value=18,
                        max_value=100,
                        value=int(selected_customer['Age']))

  # Input for Tenure
  tenure = st.number_input("Tenure (years)",
                           min_value=0,
                           max_value=50,
                           value=int(selected_customer['Tenure']))

with col2:
  # Input for Balance
  balance = st.number_input("Balance",
                            min_value=0.0,
                            value=float(selected_customer['Balance']))

  # Input for Number of Products
  num_products = st.number_input("Number of Products",
                                 min_value=1,
                                 max_value=10,
                                 value=int(selected_customer['NumOfProducts']))

  # Checkbox for Has Credit Card
  has_credit_card = st.checkbox("Has Credit Card",
                                value=bool(selected_customer['HasCrCard']))

  # Checkbox for Is Active Member
  is_active_member = st.checkbox("Is Active Member",
                                 value=bool(
                                     selected_customer['IsActiveMember']))
