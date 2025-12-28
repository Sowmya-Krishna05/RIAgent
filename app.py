import streamlit as st
from agent import answer_question

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="National Policy Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE INIT ----------------
if "answer" not in st.session_state:
    st.session_state.answer = None
    st.session_state.last_updated = None

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 📊 System Scope")
    st.markdown(
        """
        **Domains Monitored**
        - 🎓 Education (UGC / AICTE)  
        - 💰 Finance (RBI)  
        - 🏥 Healthcare (MoHFW)  
        - 👷 Labour & Employment  
        - 💻 Digital & IT Policy  
        """
    )

    st.divider()

    persona = st.selectbox(
        "👥 Stakeholder View",
        ["Student", "Startup", "Bank / Financial Institution", "Policy Analyst"]
    )

    st.divider()

    st.markdown(
        """
        **System Guarantees**
        - Deterministic outputs  
        - Authoritative sources  
        - No stale knowledge  
        """
    )

# ---------------- HEADER ----------------
st.markdown(
    """
    # 📜 National Live Policy Intelligence Agent  
    **From regulatory noise to actionable policy intelligence — in real time**
    """
)

st.divider()

# ---------------- QUERY INPUT ----------------
question = st.text_input(
    "Query live regulatory intelligence",
    placeholder="e.g. What recent RBI policy changes affect banks?"
)

# ---------------- PROCESS QUERY ----------------
if question:
    with st.spinner("Analyzing regulatory sources..."):
        answer, last_updated = answer_question(question)
        st.session_state.answer = answer
        st.session_state.last_updated = last_updated

# ---------------- OUTPUT ----------------
if st.session_state.answer:
    st.markdown("## 📌 Policy Intelligence Output")

    st.markdown(
        f"""
        ```text
        {st.session_state.answer}
        ```
        """
    )

    if st.session_state.last_updated:
        st.caption(f"🕒 Knowledge last updated at: {st.session_state.last_updated}")

    st.divider()

    st.markdown("### 🔍 Why this matters")

    if persona == "Student":
        st.write(
            "These policy updates may impact eligibility criteria, scholarships, "
            "or student benefits."
        )
    elif persona == "Startup":
        st.write(
            "These updates may affect regulatory compliance, funding norms, "
            "or operational constraints."
        )
    elif persona == "Bank / Financial Institution":
        st.write(
            "These policies introduce or modify compliance, reporting, "
            "and risk management obligations."
        )
    else:
        st.write(
            "These updates signal evolving regulatory intent and areas "
            "requiring continuous monitoring."
        )

    st.info(
        "Insights are derived from authoritative government sources "
        "and structured for decision-making."
    )

elif question:
    st.warning(
        "No directly matching policy updates were found.\n\n"
        "Try rephrasing the question or specifying a sector "
        "(education, finance, healthcare, etc.)."
    )

# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    """
    <div style="text-align:center; font-size:13px; color:gray;">
    © 2024 National Policy Intelligence System • Built for real-time regulatory clarity
    </div>
    """,
    unsafe_allow_html=True
)
