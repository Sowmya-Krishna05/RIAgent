import streamlit as st
from agent import answer_question

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="National Policy Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

    st.markdown("## 👥 Stakeholder View")
    persona = st.selectbox(
        "Select perspective",
        ["Student", "Startup", "Bank / Financial Institution", "Policy Analyst"]
    )

    st.divider()

    st.markdown("## ⚙️ System Behavior")
    st.markdown(
        """
        - Continuous ingestion  
        - Instant update reflection  
        - No stale knowledge  
        - Deterministic reasoning  
        """
    )

    st.caption("Demo environment simulates live regulatory feeds")

# ---------------- HEADER ----------------
st.markdown(
    """
    # 📜 National Live Policy Intelligence Agent
    **From regulatory noise to actionable policy intelligence — in real time**
    """
)

st.divider()

# ---------------- SYSTEM INTRO ----------------
st.markdown(
    """
    ### 🧠 What this system does
    - Monitors policy updates across critical public sectors  
    - Ingests changes continuously from authoritative sources  
    - Surfaces only relevant, actionable regulatory signals  
    - Adapts instantly as policies evolve  
    """
)

st.divider()

# ---------------- QUERY INPUT ----------------
question = st.text_input(
    "Query live regulatory intelligence",
    placeholder="e.g. What recent RBI changes affect banks?"
)

# ---------------- ANSWER SECTION ----------------
if question:
    with st.spinner("Analyzing live policy sources..."):
        answer, last_updated = answer_question(question)

    st.markdown("### 📌 Policy Intelligence Output")

    # -------- SAFE OUTPUT (NO WHITE SPACE, NO ERRORS) --------
    if answer and answer.strip():
        st.success(answer)

        if last_updated:
            st.caption(f"🕒 Last policy update detected at: {last_updated}")

        st.divider()

        st.markdown("### 🔍 Why this matters")

        if persona == "Student":
            st.write(
                "These policy updates may affect eligibility criteria, scholarships, "
                "or benefits relevant to students."
            )
        elif persona == "Startup":
            st.write(
                "These regulatory changes may influence compliance requirements, "
                "funding norms, or operational conditions for startups."
            )
        elif persona == "Bank / Financial Institution":
            st.write(
                "These updates may introduce new compliance obligations, reporting "
                "requirements, or operational constraints for financial institutions."
            )
        else:
            st.write(
                "These updates reflect evolving regulatory intent and highlight "
                "areas requiring policy analysis or continuous monitoring."
            )

        st.info(
            "Insights are derived from authoritative sources and updated dynamically "
            "as policies change."
        )

    else:
        st.warning(
            "No directly matching policy updates were found for this query.\n\n"
            "Try rephrasing the question or asking about a specific sector "
            "(e.g., education, finance, healthcare)."
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
