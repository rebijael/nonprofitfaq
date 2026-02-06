import streamlit as st
import json

st.set_page_config(
    page_title="CareConnect – Nonprofit FAQ Assistant",
    page_icon="🌱",
    layout="centered"
)

def load_faqs():
    with open("data/faqs.json", "r") as file:
        return json.load(file)

faqs = load_faqs()

st.title("🌱 CareConnect")
st.subheader("Nonprofit Organization FAQ Assistant")

st.write(
    "CareConnect helps nonprofit organizations communicate essential information "
    "clearly and compassionately to volunteers and donors."
)

st.markdown("### FAQ Categories")
st.markdown(
    "- 🤝 Volunteering\n"
    "- 💝 Donations\n"
    "- 🌍 Mission & Impact\n"
    "- 📞 Contact & Support"
)

st.markdown("### Quick Actions")

col1, col2 = st.columns(2)
with col1:
    if st.button("🤝 Volunteering"):
        st.session_state["q"] = "How can I volunteer?"

with col2:
    if st.button("💝 Donations"):
        st.session_state["q"] = "How can I donate?"

col3, col4 = st.columns(2)
with col3:
    if st.button("🌍 Our Mission"):
        st.session_state["q"] = "What is this nonprofit about?"

with col4:
    if st.button("📞 Contact"):
        st.session_state["q"] = "How can I contact the organization?"

question = st.text_input(
    "Ask a question:",
    value=st.session_state.get("q", "")
)

def get_answer(user_q):
    user_q = user_q.lower()

    for faq in faqs:
        keywords = faq["question"].lower().replace("?", "").split()
        keywords = [word for word in keywords if len(word) > 3]

        if any(keyword in user_q for keyword in keywords):
            return faq["answer"]

    return (
        "Thank you for reaching out 🌱 "
        "We truly appreciate your interest. "
        "Please contact us through official channels for further assistance."
    )

if question:
    st.markdown("### 💬 Response")
    st.write(get_answer(question))

st.markdown("---")
st.markdown("### Contact Information")

st.write(
    "📧 Email: contact@careconnect.org\n\n"
    "🌐 Website: www.careconnect.org\n\n"
    "📍 Location: Community Outreach Center"
)

st.caption(
    "Built with empathy and clarity • Designed for nonprofit communities <3"
)