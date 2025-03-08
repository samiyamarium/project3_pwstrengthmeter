import streamlit as st
import re

st.set_page_config(" Password Stregth Meter",layout="centered")
st.title(":green :maple_leaf: Password Strength Meter :maple_leaf: \r by  :maple_leaf:  Samiya Marium    :maple_leaf:")
def passwordstrength(pw):
    score = 0


    if len(pw) >= 8:
        score += 1
    elif len(pw) >= 6:
        score += 0.5

    # Checks for lowercase letters
    if re.search(r'[a-z]', pw):
        score += 1

    # Checks for uppercase letters
    if re.search(r'[A-Z]', pw):
        score += 1

    # Checks for numbers
    if re.search(r'[0-9]', pw):
        score += 1

    # Checks for special characters
    if re.search(r'[@$!%*?&]', pw):
        score += 1

   
    return score

# Mapping score to strength
def strength_check(score):
    if score == 5:
        return "Meets all criteria"
    elif score >= 4:
        return "Good but missing some security features"
    elif score >= 2:
        return "Incomplete,missing key elements"
    else:
        return "Very Weak"



pw = st.text_input(":green[Type your password]:")


if pw:
    score = passwordstrength(pw)
    strength = strength_check(score)
    st.write(f" :red[ Your password] : \r  :blue[{strength}]")

    
    if strength == "Very Weak":
        st.warning(":red[Add special characters and more digits/alphabets to make it strong]")
    elif strength == "Incomplete,missing key elements":
        st.warning(":green[could be better by adding more characters/digits/lowercase/uppercase to ensure security]")
    elif strength == "Good but missing some security features":
        st.info(":blue[It's almost fine but make it more secure by adding more digits to it] ")
    else:
        st.success("Excellent! Your password is very strong.")

