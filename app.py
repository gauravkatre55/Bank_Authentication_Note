import joblib
import numpy as np
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Banknote Authentication",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD MODEL
# =========================================================

classifier = joblib.load("classifier.pkl")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* ---------- MAIN PAGE ---------- */

    .stApp {
        background: #0b1120;
        color: #f8fafc;
    }

    .main {
        padding: 0rem 2rem 2rem 2rem;
    }

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    section[data-testid="stSidebar"] h1 {
        color: #ffffff;
        font-size: 24px;
    }

    section[data-testid="stSidebar"] p {
        color: #9ca3af;
    }

    /* ---------- HEADER ---------- */

    .hero {
        background: linear-gradient(
            135deg,
            #172554 0%,
            #1e3a8a 50%,
            #312e81 100%
        );

        padding: 35px 40px;
        border-radius: 18px;
        margin-bottom: 30px;
        border: 1px solid #263b73;
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }

    .hero h1 {
        color: white;
        font-size: 38px;
        margin-bottom: 8px;
        font-weight: 700;
    }

    .hero p {
        color: #cbd5e1;
        font-size: 16px;
        margin: 0;
    }

    /* ---------- SECTION TITLE ---------- */

    .section-title {
        color: #e2e8f0;
        font-size: 21px;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* ---------- INPUT CARD ---------- */

    .input-card {
        background: #111827;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #1f2937;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }

    /* ---------- INPUT LABELS ---------- */

    label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }

    /* ---------- NUMBER INPUT ---------- */

    div[data-baseweb="input"] {
        background-color: #0f172a;
        border: 1px solid #334155;
        border-radius: 10px;
    }

    div[data-baseweb="input"]:focus-within {
        border: 1px solid #6366f1;
        box-shadow: 0 0 0 1px #6366f1;
    }

    input {
        color: #f8fafc !important;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        border: none;
        background: linear-gradient(
            90deg,
            #4f46e5,
            #6366f1
        );
        color: white;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #4338ca,
            #4f46e5
        );
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79,70,229,0.3);
    }

    /* ---------- RESULT ---------- */

    .result-card {
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        margin-top: 25px;
        border: 1px solid #334155;
        background: #111827;
    }

    .result-title {
        font-size: 14px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .result-value {
        font-size: 30px;
        font-weight: 700;
        margin-top: 8px;
    }

    /* ---------- INFO CARDS ---------- */

    .info-card {
        background: #111827;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #1f2937;
        height: 100%;
    }

    .info-card h3 {
        color: #e2e8f0;
        font-size: 18px;
    }

    .info-card p {
        color: #94a3b8;
        line-height: 1.6;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #1f2937;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 💳 Banknote AI")

    st.markdown("""
    <p>
    An ML-powered application for detecting whether
    a banknote is authentic or potentially forged.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🤖 Machine Learning")

    st.markdown("""
    **Algorithm:** Random Forest  
    **Task:** Binary Classification  
    **Input Features:** 4  
    **Model:** `classifier.pkl`
    """)

    st.markdown("---")

    st.markdown("### 📊 Features")

    st.markdown("""
    - Variance
    - Skewness
    - Curtosis
    - Entropy
    """)

    st.markdown("---")

    st.caption("Built with Python + Streamlit + Scikit-learn")


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

    <h1>💳 Banknote Authentication</h1>

    <p>
        Machine Learning powered system for identifying
        authentic and potentially forged banknotes.
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🔍 Enter Banknote Features</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="input-card">',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    variance = st.number_input(
        "Variance",
        value=0.0,
        format="%.6f",
        help="Variance of the wavelet transformed image"
    )

    skewness = st.number_input(
        "Skewness",
        value=0.0,
        format="%.6f",
        help="Skewness of the wavelet transformed image"
    )

with col2:

    curtosis = st.number_input(
        "Curtosis",
        value=0.0,
        format="%.6f",
        help="Curtosis of the wavelet transformed image"
    )

    entropy = st.number_input(
        "Entropy",
        value=0.0,
        format="%.6f",
        help="Entropy of the wavelet transformed image"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# PREDICTION
# =========================================================

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:

    predict_button = st.button(
        "🔎 Authenticate Banknote",
        use_container_width=True
    )


if predict_button:

    # Prepare input
    input_data = np.array([
        [variance, skewness, curtosis, entropy]
    ])

    # Prediction
    prediction = classifier.predict(input_data)[0]

    # Optional probability
    probability = None

    if hasattr(classifier, "predict_proba"):
        probability = classifier.predict_proba(input_data)[0].max()

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    if prediction == 0:

        st.markdown("""
        <div class="result-card">

            <div class="result-title">
                Authentication Result
            </div>

            <div class="result-value">
                ✅ Authentic Banknote
            </div>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-card">

            <div class="result-title">
                Authentication Result
            </div>

            <div class="result-value">
                ⚠️ Potentially Forged Banknote
            </div>

        </div>
        """, unsafe_allow_html=True)

    # Probability
    if probability is not None:

        st.progress(
            float(probability),
            text=f"Model Confidence: {probability * 100:.2f}%"
        )


# =========================================================
# PROJECT INFORMATION
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📌 About This Project</div>',
    unsafe_allow_html=True
)

info1, info2, info3 = st.columns(3)

with info1:

    st.markdown("""
    <div class="info-card">

    <h3>🎯 Objective</h3>

    <p>
    Build a machine learning classification system
    capable of distinguishing between authentic and
    forged banknotes using statistical image features.
    </p>

    </div>
    """, unsafe_allow_html=True)


with info2:

    st.markdown("""
    <div class="info-card">

    <h3>⚙️ Technology</h3>

    <p>
    Python, NumPy, Joblib, Scikit-learn and Streamlit
    are used to train, save and deploy the machine
    learning model.
    </p>

    </div>
    """, unsafe_allow_html=True)


with info3:

    st.markdown("""
    <div class="info-card">

    <h3>📈 Input Features</h3>

    <p>
    The model uses variance, skewness, curtosis and
    entropy extracted from banknote images.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    Banknote Authentication ML Application
    <br>
    Built with Python • Machine Learning • Streamlit

</div>
""", unsafe_allow_html=True)