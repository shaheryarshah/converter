# Import required libraries
import streamlit as st

# Define conversion factors
conversion_factors = {
    'Meters to Kilometers': 0.001,
    'Kilometers to Meters': 1000,
    'Grams to Kilograms': 0.001,
    'Kilograms to Grams': 1000,
    'Celsius to Fahrenheit': (lambda c: (c * 9/5) + 32),
    'Fahrenheit to Celsius': (lambda f: (f - 32) * 5/9)
}

# Define the conversion function
def convert_units(value, conversion_type):
    if callable(conversion_factors[conversion_type]):
        return conversion_factors[conversion_type](value)
    else:
        return value * conversion_factors[conversion_type]

# Streamlit UI elements
st.title("Unit Converter")

value = st.number_input("Enter the value to convert:", value=0.0)
conversion_type = st.selectbox("Select the conversion type:", list(conversion_factors.keys()))

if st.button("Convert"):
    result = convert_units(value, conversion_type)
    st.write(f"The result of converting {value} using '{conversion_type}' is: {result}")
