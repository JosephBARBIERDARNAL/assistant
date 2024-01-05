import streamlit as st
import time
import threading
from src.ai import AI
from src.audio import record_audio, save_as_mp3
from src.ui import space

# set page title
st.markdown("<h1 style='text-align: center; color: black;'>AI Voice Assistant</h1>",
            unsafe_allow_html=True)

space(3)
def speak_in_thread(response):
    ai.speak(response)

# create an instance of the AI class
ai = AI()

# Initialize a session state for message history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# record and save audio
if st.button("Record"):
    recording = record_audio(5)
    save_as_mp3(recording, 44100, "audiofiles/input.mp3")

    # listen
    transcript = ai.listen("audiofiles/input.mp3")
    with st.chat_message("user"):
        st.markdown(transcript)
    st.session_state.messages.append({"role": "user", "content": transcript})

    # Get response using the updated history
    response = ai.think(transcript, st.session_state.messages)
    speak_thread = threading.Thread(target=speak_in_thread, args=(response,))
    speak_thread.start()
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for chunck in response.split():
            full_response += chunck + " "
            message_placeholder.markdown(full_response +  "▌")
            time.sleep(0.15)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": response})
