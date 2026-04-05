import streamlit as st
from main import run_agents  # ou run_agents.py si tu changes le nom

st.set_page_config(page_title="AI Learning Assistant", page_icon="🤖")

st.title("🤖 AI Learning Assistant")
st.write("Analyze your problem and get a smart solution using AI Agents")

user_input = st.text_area("✍️ Describe your problem:")

if st.button("🚀 Analyze"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = run_agents(user_input)

        st.success("Analysis complete ✅")
        st.subheader("📊 Analysis")
        st.info(result["analysis"])

        st.subheader("💡 Suggested Solution")
        st.success(result["solution"])
    else:
        st.warning("⚠️ Please enter a problem first!")