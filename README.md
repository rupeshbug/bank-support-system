## Customer Support Chatbot

### About the Project

This project is a customer support chatbot designed to handle common banking-related queries using both text and audio input. Built with Streamlit, the chatbot leverages a fine-tuned T5 model to understand user intents and 
generate relevant predefined responses. The app can interact with users through typed questions or voice commands, offering flexibility in communication.

### Dataset

The chatbot is trained using a subset of the Bank77 dataset, which includes 77 distinct banking-related intents. To simplify the model and reduce complexity, this project focuses on the top 20 most common intents from the dataset. 
These intents cover the most frequent customer support queries, ensuring the chatbot is both effective and efficient in handling typical banking inquiries.

### Key features

- Text and Voice Interaction: The chatbot can process both text and voice inputs, making it accessible in various contexts.
- Intent Recognition: By utilizing a T5 model, the chatbot identifies the user's intent and provides predefined responses based on the identified intent.
- Real-Time Response: The chatbot provides instant feedback, including spoken responses for audio input, making the interaction seamless and user-friendly.
- Chat History: The app maintains a conversation history that users can refer back to during their interaction with the chatbot.

### Why T5 Model?

The T5 (Text-To-Text Transfer Transformer) model was chosen for its versatility in natural language processing tasks. It excels in understanding and generating text by treating every NLP task as a text-to-text problem, 
which makes it particularly effective for intent recognition and response generation in this chatbot. The model has been fine-tuned on a subset of the Bank77 dataset, which is known for its comprehensive coverage of banking-related intents.
