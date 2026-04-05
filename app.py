import streamlit as st
from main import run_agents

st.set_page_config(page_title="AI Learning Assistant", page_icon="🤖")

st.title("🤖 AI Learning Assistant")
st.write("حلل مشكلتك وخذ حل ذكي باستعمال AI Agents")

user_input = st.text_area("✍️ Describe your problem:")

if st.button("🚀 Analyze"):
    if user_input:
        with st.spinner("Analyzing your problem..."):
            result = run_agents(user_input)

        st.success("Done ✅")

        # تقسيم النتيجة (حتى إلا كانت mocked)
        st.subheader("📊 Analysis")
        st.info("Here the AI analyzes your problem")

        st.subheader("💡 Solution")
        st.success("Here the AI gives you a solution")

        # عرض النتيجة الكاملة (debug أو demo)
        st.subheader("📦 Full Output")
        st.write(result)

    else:
        st.warning("⚠️ Please enter a problem first!")