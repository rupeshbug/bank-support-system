import os
import streamlit as st
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./t5-main-chatbot-model")
tokenizer = T5Tokenizer.from_pretrained("./t5-main-chatbot-model")

# setup
st.title("Customer Support System")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "audio_processing" not in st.session_state:
    st.session_state.audio_processing = False

def speak(text):
    """Convert text to speech and play it."""
    tts = gTTS(text)
    tts.save("response.mp3")
    playsound("response.mp3")
    # delete the file after playing
    os.remove("response.mp3")

def generate_response(text):
    """Generate response based on the user input."""
    input_ids = tokenizer.encode(f"Intent: {text}", return_tensors='pt')
    output = model.generate(input_ids, max_new_tokens=50)
    response = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    
    if "|||" in response:
        intent, response_text = response.split("||| ")
        return intent, response_text
    else:
        return "Unknown", "Cannot answer that question. Please contact support."

def listen_and_respond():
    """Listen for audio input, generate a response, and speak it out."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        listening_message = st.info("Listening...")
        audio = recognizer.listen(source)
    
    try:
        user_input = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        user_input = "Sorry, I didn't understand that."
    except sr.RequestError:
        user_input = "Sorry, I'm having trouble with my speech recognition service."
    
    listening_message.empty()

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate and speak the response
    intent, response = generate_response(user_input)
    with st.chat_message("assistant"):
        # Display the intent in green
        st.markdown(f"<span style='color:green;'>Intent: {intent}</span>", unsafe_allow_html=True)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": f"<span style='color:green;'>Intent: {intent}</span><br>{response}"})
    
    speak(response)
    
    # Mark that the audio processing has finished
    st.session_state.audio_processing = False

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

if not st.session_state.audio_processing:
    # Handle text input
    if prompt := st.chat_input("Type your question:"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        intent, response = generate_response(prompt)
        with st.chat_message("assistant"):
            st.markdown(f"<span style='color:green;'>Intent: {intent}</span>", unsafe_allow_html=True)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": f"<span style='color:green;'>Intent: {intent}</span><br>{response}"})

    # Handle audio input
    if st.button("🎤 Speak"):
        st.session_state.audio_processing = True
        listen_and_respond()
