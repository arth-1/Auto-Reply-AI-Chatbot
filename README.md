# Auto-Reply-AI-Chatbot

This project implements an auto-reply chatbot using the LLaMA 3.2 language model. The chatbot is designed to monitor a chat interface, copy messages, generate appropriate replies based on the last message, and send responses while considering the sender's identity.

## Features

- **Automatic Message Retrieval**: Continuously monitors a specified chat window for incoming messages.
- **Sender Check**: Responds only to messages from users other than the bot itself.
- **Multi-line Message Support**: Handles messages that span multiple lines.
- **AI-Powered Responses**: Uses the LLaMA 3.2 model to generate contextually relevant replies.

## Requirements

- Python 3.x
- Libraries:
  - `pyautogui`
  - `pyperclip`
  - `torch`
  - `transformers`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-reply-chatbot.git
   cd auto-reply-chatbot

   How to Use OpenAI Models
## In this project, you can also use OpenAI's models to generate responses instead of the LLaMA model. Here’s how:

Create an OpenAI Account: Sign up on the OpenAI website and obtain an API key.

Install the OpenAI Python Package:

bash
Copy code
pip install openai
Set Up Your API Key: You can set your API key in your environment variables or directly in your code (not recommended for security reasons):

python
Copy code
import openai
openai.api_key = "your-api-key"
Generate Responses: Use the OpenAI API to generate responses based on the copied message. You can do this by calling the openai.ChatCompletion.create() function with the necessary parameters to send messages and retrieve responses.

Replace the LLaMA Model Calls: In your code, wherever you call the LLaMA model, replace it with the OpenAI API call to generate a response based on the copied text.

## Code Explanation
The script uses pyautogui to interact with the GUI, selecting and copying messages.
It utilizes pyperclip to manage clipboard operations.
The transformers library loads the LLaMA 3.2 model for generating replies based on the copied text.
A continuous loop checks for new messages, and responses are sent to a specified chat window.
## Important Notes
Ensure that the chat window is active and positioned correctly for the script to function without issues.
Adjust sleep durations in the code as needed to match the responsiveness of your chat application.
The sender's name is extracted dynamically from the message format, so ensure that the messages follow a consistent format (e.g., Sender: Message).
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments
LLaMA Model
OpenAI API
Transformers Library
PyAutoGUI
vbnet
Copy code

### Instructions for Use:
- Replace `yourusername` in the clone URL with your actual GitHub username.
- Adjust the license section according to your project's license if it's different from MIT.
- You may want to update the "How to Use OpenAI Models" section with specific details on how to implement OpenAI's API in your project based on your experience.
