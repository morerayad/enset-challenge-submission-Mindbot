import streamlit as st
from main import run_agents

st.set_page_config(page_title="AI Learning Assistant", page_icon="🤖")

# Page title
st.title("🤖 AI Learning Assistant")
st.write("Analyze your problem and get a smart solution using AI Agents")

# User input
user_input = st.text_area("✍️ Describe your problem:")

# Button
if st.button("🚀 Analyze"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = run_agents(user_input)

        st.success("Analysis complete ✅")

        # Show analysis
        st.subheader("📊 Analysis")
        st.info("This section explains the AI's analysis of your problem.")

        # Show solution
        st.subheader("💡 Suggested Solution")
        st.success("Here is a smart solution based on the analysis.")

        # Full output for reference
        st.subheader("📦 Full Output")
        st.write(result)

    else:
        st.warning("⚠️ Please enter a problem first!")