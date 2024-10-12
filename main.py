import streamlit as st

# Title of the app
st.title("Emergency Department Assessment of Chest Pain Score (EDACS)")

st.markdown("""
This score applies only to patients: 
1. ≥18 years old with normal vital signs 
2. Chest pain consistent with ACS
3. No ongoing chest pain or crescendo angina
""")

# Age input
age = st.number_input("Age (years)", min_value=0, max_value=120, step=1)

# Sex input
sex = st.radio("Sex", ("Female (0 points)", "Male (+6 points)"))
sex_score = 0 if sex == "Female (0 points)" else 6

# Symptoms and Signs inputs
st.subheader("Symptoms and Signs")

diaphoresis = st.radio("Diaphoresis", ["No (0 points)", "Yes (+3 points)"])
diaphoresis_score = 3 if diaphoresis == "Yes (+3 points)" else 0

radiating_pain = st.radio("Pain radiates to arm, shoulder, neck, or jaw", ["No (0 points)", "Yes (+5 points)"])
radiating_pain_score = 5 if radiating_pain == "Yes (+5 points)" else 0

inspiration_pain = st.radio("Pain occurred or worsened with inspiration", ["No (0 points)", "Yes (-4 points)"])
inspiration_pain_score = -4 if inspiration_pain == "Yes (-4 points)" else 0

palpation_pain = st.radio("Pain is reproduced by palpation", ["No (0 points)", "Yes (-6 points)"])
palpation_pain_score = -6 if palpation_pain == "Yes (-6 points)" else 0

# Calculate total score
total_score = sex_score + diaphoresis_score + radiating_pain_score + inspiration_pain_score + palpation_pain_score

# Display result
st.write(f"Your total EDACS score is: **{total_score}**")

# Explain interpretation of the score
if total_score <= 16:
    st.markdown("**Low Risk**: Patient has a low risk of a major adverse cardiac event.")
elif 17 <= total_score <= 20:
    st.markdown("**Moderate Risk**: Patient may require further assessment.")
else:
    st.markdown("**High Risk**: Patient is at a higher risk of a major adverse cardiac event. Immediate evaluation is needed.")
