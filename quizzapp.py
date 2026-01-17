import streamlit as st

st.title("🎮 Quiz Game")
st.write("Welcome to my quiz game!")

# Initialize score
score = 0

# Question 1
st.subheader("Question 1")
answer1 = st.text_input("What does CPU stand for?")

# Question 2
st.subheader("Question 2")
answer2 = st.text_input("What does GPU stand for?")

# Question 3
st.subheader("Question 3")
answer3 = st.text_input("What does RAM stand for?")

# Submit button
if st.button("Submit Quiz"):
    if answer1.lower() == "central processing unit":
        st.success("Question 1: Correct! ✅")
        score += 1
    else:
        st.error("Question 1: Incorrect! ❌")
    
    if answer2.lower() == "graphics processing unit":
        st.success("Question 2: Correct! ✅")
        score += 1
    else:
        st.error("Question 2: Incorrect! ❌")
    
    if answer3.lower() == "random access memory":
        st.success("Question 3: Correct! ✅")
        score += 1
    else:
        st.error("Question 3: Incorrect! ❌")
    
    st.write("---")
    st.write(f"### Final Score: {score}/3")
    st.write(f"### Percentage: {(score / 3) * 100:.1f}%")