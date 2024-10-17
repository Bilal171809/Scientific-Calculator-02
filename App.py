import streamlit as st
import math

# Function definitions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Square root of negative number."

def logarithm(x, base=10):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error! Logarithm of non-positive number."

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "Error! Factorial of negative number."

# Streamlit UI
st.title("Scientific Calculator")

# Select the operation from a dropdown
operation = st.selectbox("Select operation", 
                         ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"])

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number", step=1.0)
    num2 = st.number_input("Enter second number", step=1.0)
    
    if operation == "Add":
        st.write(f"Result: {add(num1, num2)}")
    elif operation == "Subtract":
        st.write(f"Result: {subtract(num1, num2)}")
    elif operation == "Multiply":
        st.write(f"Result: {multiply(num1, num2)}")
    elif operation == "Divide":
        st.write(f"Result: {divide(num1, num2)}")
    elif operation == "Power":
        st.write(f"Result: {power(num1, num2)}")

elif operation == "Square Root":
    num = st.number_input("Enter number", step=1.0)
    st.write(f"Result: {square_root(num)}")

elif operation == "Logarithm":
    num = st.number_input("Enter number", step=1.0)
    base = st.number_input("Enter base (default 10)", value=10, step=1.0)
    st.write(f"Result: {logarithm(num, base)}")

elif operation == "Sine":
    angle = st.number_input("Enter angle in degrees", step=1.0)
    st.write(f"Result: {sine(angle)}")

elif operation == "Cosine":
    angle = st.number_input("Enter angle in degrees", step=1.0)
    st.write(f"Result: {cosine(angle)}")

elif operation == "Tangent":
    angle = st.number_input("Enter angle in degrees", step=1.0)
    st.write(f"Result: {tangent(angle)}")

elif operation == "Factorial":
    num = st.number_input("Enter number", step=1.0, format="%.0f")
    st.write(f"Result: {factorial(int(num))}")
