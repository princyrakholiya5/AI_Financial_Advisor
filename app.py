import streamlit as st
from finance_ai import get_financial_advice
from visualization import create_chart

st.title("AI Finance Advisor")

st.write("Enter your financial details")

income = st.number_input("Monthly Income", min_value=0)
expenses = st.number_input("Monthly Expenses", min_value=0)

if st.button("Generate Advice"):

    savings = income - expenses

    st.subheader("Financial Summary")

    st.write("Income:", income)
    st.write("Expenses:", expenses)
    st.write("Savings:", savings)

    chart = create_chart(expenses, savings)

    st.pyplot(chart)

    st.subheader("AI Financial Advice")

    advice = get_financial_advice(income, expenses, savings)

    st.write(advice)