import streamlit as st

# Function to perform the calculations
def calculate(operation, num1, num2):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num1 / num2

# Title of the app
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Select operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# Calculate button
if st.button("Calculate"):
    if operation == 'Division' and num2 == 0:
        st.error("Division by zero is not allowed!")
    else:
        result = calculate(operation, num1, num2)
        st.success(f"The result of {operation.lower()} is {result}")

# Reset button
if st.button("Reset"):
    num1 = 0.0
    num2 = 0.0
    st.experimental_rerun()