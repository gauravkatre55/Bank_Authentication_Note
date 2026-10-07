import joblib
import numpy as np
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Banknote Authentication System",
    page_icon="🏦",
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

/* ================= BACKGROUND ================= */

.stApp {
    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(37, 99, 235, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 85%,
            rgba(14, 165, 233, 0.12),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #06101f 0%,
            #0b1b32 50%,
            #071426 100%
        );

    color: #ffffff;
}

/* ================= PAGE WIDTH ================= */

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ================= TITLE ================= */

h1 {
    text-align: center !important;
    font-size: 40px !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin-bottom: 5px !important;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 35px;
}

/* ================= INPUT LABEL ================= */

label {
    color: #dbeafe !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* ================= INPUT ================= */

div[data-baseweb="input"] {
    background-color: #101b2d !important;
    border: 1px solid #304866 !important;
    border-radius: 10px !important;
    min-height: 48px;
}

div[data-baseweb="input"]:focus-within {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 1px #3b82f6 !important;
}

input {
    color: #ffffff !important;
    font-size: 16px !important;
}

/* ================= PREDICT BUTTON ================= */

.stButton > button {
    width: 100%;
    height: 58px;

    margin-top: 20px;

    background: linear-gradient(
        135deg,
        #2563eb,
        #0ea5e9
    );

    color: #ffffff;

    border: none;
    border-radius: 12px;

    font-size: 18px;
    font-weight: 650;

    box-shadow:
        0 8px 20px rgba(37, 99, 235, 0.30);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 28px rgba(37, 99, 235, 0.45);
}

/* ================= RESULT ================= */

.result-box {
    margin-top: 28px;
    padding: 25px;

    text-align: center;

    background: rgba(15, 30, 52, 0.95);

    border: 1px solid #294564;
    border-radius: 14px;
}

.result-label {
    color: #94a3b8;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.result-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: 700;
    margin-top: 8px;
}

/* ================= FOOTER ================= */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROFESSIONAL HEADER
# --------------------------------------------------

st.title("🏦 Banknote Authentication System")

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Banknote Verification'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# INPUT FEATURES
# --------------------------------------------------

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


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

predict = st.button(
    "🔍  Verify Banknote",
    use_container_width=True
)


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

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-label">
                Verification Result
            </div>

            <div class="result-value">
                {result}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'AI-powered banknote verification using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)