import streamlit as st

# Title and Header
st.title("🌟 Welcome to Streamlit!")
st.header("📸 Simple Image Viewer App")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

# Text input and display
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, **{name}**! 👋")
