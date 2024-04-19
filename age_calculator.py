"""Calculate a cat's age in human years."""


import streamlit as st


st.title("🐱 Cat Age Calculator")
st.markdown("Human [age calculator](https://age-calculator.app)")

# Build conversion dictionary: keys are cat years, values are human years.
conversion = {1: 15}

for age in (2, 3):
    conversion[age] = conversion[age - 1] + 6

for age in range(4, 21):
    conversion[age] = conversion[age - 1] + 4

cat_age = st.number_input(
    label="Enter your cat's age in years:",
    min_value=0,
    max_value=20,
)

human_age = conversion.get(cat_age)

if human_age:
    st.write(
        "In human years, your cat would be "
        f":blue[**{human_age} years**] old."
    )
