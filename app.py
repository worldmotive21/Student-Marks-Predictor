
import streamlit as st
import pandas as pd
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Marks Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD DATA & MODEL ----------------
df = pd.read_csv("study_hours.csv")

X = df[["StudyHours"]]
y = df["Marks"]

model = lm.LinearRegression()
model.fit(X, y)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: #eaf2ff !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(120deg, #142b52, #2764a5);
    padding: 30px;
    border-radius: 18px;
    color: white;
    margin-bottom: 24px;
}

.hero h1 {
    color: white;
    font-size: 34px;
    margin-bottom: 8px;
}

.hero p {
    color: #e2ebff;
    font-size: 17px;
    margin-bottom: 0;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #dbe5f2;
}

.stButton button {
    background: #2159a6;
    color: white;
    border-radius: 10px;
    border: none;
    min-height: 45px;
    font-weight: 600;
    width: 100%;
}

.stButton button:hover {
    background: #173f7b;
    color: white;
}

.panel {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #dbe5f2;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🎓 StudyMate")
    st.caption("STUDENT ANALYTICS")
    st.divider()

    st.write("📊 Student Marks Predictor")
    st.write("🤖 Linear Regression")

    st.info(
        "Enter your study hours to estimate your marks."
    )

    st.caption("Educational demo project")

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🎓 Student Marks Predictor</h1>
    <p>
        Estimate your marks using study hours and
        Machine Learning.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- SUMMARY CARDS ----------------
c1, c2, c3 = st.columns(3)

c1.metric("Students in Dataset", len(df))
c2.metric("Minimum Study Hours", f"{df['StudyHours'].min():g}")
c3.metric("Maximum Study Hours", f"{df['StudyHours'].max():g}")

st.write("")

# ---------------- INPUT SECTION ----------------
st.subheader("📝 Make a Prediction")
st.write("Enter your daily study hours below.")

input_col, button_col = st.columns([2, 1])

with input_col:
    hours = st.number_input(
        "Study hours per day",
        min_value=0.5,
        max_value=24.0,
        value=3.0,
        step=0.5
    )

with button_col:
    st.write("")
    st.write("")
    predict_clicked = st.button(
        "Predict My Marks",
        use_container_width=True
    )

# ---------------- VALIDATION & PREDICTION ----------------
if predict_clicked:
    min_hours = df["StudyHours"].min()
    max_hours = df["StudyHours"].max()

    if hours < min_hours or hours > max_hours:
        st.session_state.pop("last_prediction", None)
        st.warning(
            f"Please enter study hours between "
            f"{min_hours:g} and {max_hours:g}, "
            "the range covered by this dataset."
        )
    else:
        prediction = model.predict(
            pd.DataFrame({"StudyHours": [hours]})
        )[0]

        marks = max(0, min(100, float(prediction)))

        st.session_state["last_prediction"] = {
            "hours": hours,
            "marks": marks
        }

# ---------------- GRAPH & RESULT BELOW ----------------
st.divider()

graph_col, result_col = st.columns(
    [1.2, 1],
    gap="large"
)

# GRAPH ON LEFT
with graph_col:
    st.subheader("📈 Study Hours vs Marks")

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.scatter(
        df["StudyHours"],
        df["Marks"],
        color="#2463a6",
        s=85,
        label="Actual Marks"
    )

    ax.plot(
        X["StudyHours"],
        model.predict(X),
        color="#e58b36",
        linewidth=2.5,
        label="Regression Line"
    )

    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Marks")
    ax.set_title("Study Hours and Marks")
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

# PREDICTED RESULT ON RIGHT
with result_col:
    st.subheader("✨ Your Prediction")

    if "last_prediction" in st.session_state:
        result = st.session_state["last_prediction"]
        marks = result["marks"]

        st.metric(
            "Estimated Marks",
            f"{marks:.1f} / 100"
        )

        st.metric(
            "Study Hours",
            f"{result['hours']:g} hours"
        )

        if marks >= 80:
            st.success(
                "Excellent estimated result! Keep it up."
            )
        elif marks >= 60:
            st.info(
                "Good estimated result. Keep practising."
            )
        else:
            st.warning(
                "Keep practising and build a consistent routine."
            )

    else:
        st.info(
            "Enter study hours above and click "
            "'Predict My Marks' to see your result here."
        )

    st.caption(
        "Predictions are estimates based on a small dataset, "
        "not a guarantee of actual exam marks."
    )

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "Student Marks Predictor | Built with Python, "
    "Streamlit, Pandas and Scikit-learn"
)
