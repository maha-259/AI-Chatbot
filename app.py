import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDSuWrK1dyqv4frbx9VQIdzncRT4KJ_9QI")

model = genai.GenerativeModel("gemini-1.5-pro") 

st.set_page_config(page_title="Thingavin Carpentry Chatbot", layout="wide")

st.sidebar.image("https://via.placeholder.com/150", caption="Thingavin Carpentry", use_column_width=True)
language = st.sidebar.radio("🌍 Choose Language / اختر اللغة", ["English", "العربية"])

contexts = {
    "English": """
    You are a smart assistant specialized in carpentry and woodworking, especially with Thingavin Carpentry.
    Your answers must be accurate and based on reliable information about types of wood, designs, tools, painting,
    and everything related to professional carpentry.
    """,
    "العربية": """
    أنت مساعد ذكي متخصص في النجارة وصناعة الأخشاب، خاصة مع Thingavin Carpentry.
    يجب أن تكون إجاباتك دقيقة ومبنية على معلومات موثوقة حول أنواع الأخشاب، التصاميم، الأدوات، الطلاء،
    وكل ما يتعلق بالنجارة الاحترافية.
    """
}
context = contexts[language]

# UI Title
st.markdown(
    """
    <h1 style='text-align: center; color: #8B4513;'>🪵 Thingavin Carpentry Chatbot</h1>
    <h4 style='text-align: center; color: #555;'>Ask me anything about carpentry and woodworking!</h4>
    """,
    unsafe_allow_html=True,
)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input field
user_input = st.chat_input("Type your question here..." if language == "English" else "اكتب سؤالك هنا...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate AI response
    response = model.generate_content(context + "\n\n" + user_input).text
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Save response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
