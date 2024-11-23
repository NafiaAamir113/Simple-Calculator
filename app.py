import streamlit as st

# Streamlit app for a simple calculator
st.title("Simple Calculator")

# Dropdown menu to select the operation
operation = st.selectbox(
    "Select an operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)")
)

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number:", value=0.0, format="%.2f")

# Button to calculate
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Division by zero is not allowed.")

