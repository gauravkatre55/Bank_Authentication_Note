import joblib
import numpy as np
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Banknote Authentication System",
    page_icon="💳",
    layout="centered"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

classifier = joblib.load("classifier.pkl")

# --------------------------------------------------
# PROFESSIONAL BANKING THEME
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(37, 99, 235, 0.18), transparent 25%),
        radial-gradient(circle at 90% 80%, rgba(14, 165, 233, 0.12), transparent 25%),
        linear-gradient(135deg, #06101f 0%, #0b1b32 50%, #071426 100%);
    color: white;
}

/* Remove extra top space */
.block-container {
    padding-top: 2rem;
    max-width: 850px;
}

/* Main Title */
.title {
    text-align: center;
    padding: 30px 20px 25px;
}

.title h1 {
    font-size: 38px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}

.title p {
    color: #94a3b8;
    font-size: 16px;
    margin: 0;
}

/* Bank symbol */
.bank-icon {
    text-align: center;
    font-size: 42px;
    margin-bottom: 5px;
}

/* Input Card */
.input-card {
    background: rgba(15, 30, 52, 0.92);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #243b5a;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.30);
}

/* Labels */
label {
    color: #cbd5e1 !important;
    font-weight: 500 !important;
}

/* Input fields */
div[data-baseweb="input"] {
    background-color: #091525 !important;
    border: 1px solid #2b4668 !important;
    border-radius: 9px !important;
}

div[data-baseweb="input"]:focus-within {
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 0 0 1px #3b82f6 !important;
}

input {
    color: white !important;
}

/* Prediction Button */
.stButton > button {
    width: 100%;
    height: 55px;

    background: linear-gradient(
        135deg,
        #2563eb,
        #0ea5e9
    );

    color: white;
    border: none;
    border-radius: 11px;

    font-size: 17px;
    font-weight: 600;

    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.30);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(37, 99, 235, 0.45);
}

/* Result */
.result {
    margin-top: 25px;
    padding: 22px;
    text-align: center;

    background: rgba(15, 30, 52, 0.95);

    border: 1px solid #294564;
    border-radius: 15px;
}

.result-label {
    color: #94a3b8;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.result-value {
    color: #ffffff;
    font-size: 26px;
    font-weight: 700;
    margin-top: 8px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown("""
<div class="title">

    <div class="bank-icon">🏦</div>

    <h1>Banknote Authentication System</h1>

    <p>Machine Learning Based Banknote Verification</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    variance = st.number_input(
        "Variance",
        value=0.0,
        format="%.6f"
    )

    skewness = st.number_input(
        "Skewness",
        value=0.0,
        format="%.6f"
    )

with col2:

    curtosis = st.number_input(
        "Curtosis",
        value=0.0,
        format="%.6f"
    )

    entropy = st.number_input(
        "Entropy",
        value=0.0,
        format="%.6f"
    )

st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

predict = st.button(
    "🔍  Verify Banknote",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if predict:

    input_data = np.array([
        [variance, skewness, curtosis, entropy]
    ])

    prediction = classifier.predict(input_data)[0]

    if prediction == 0:
        result = "✓ Authentic Banknote"
    else:
        result = "⚠ Potentially Forged Banknote"

    st.markdown(f"""
    <div class="result">

        <div class="result-label">
            Verification Result
        </div>

        <div class="result-value">
            {result}
        </div>

    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    AI-powered banknote verification using Machine Learning
</div>
""", unsafe_allow_html=True)