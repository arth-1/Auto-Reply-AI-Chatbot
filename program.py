import pyautogui
import pyperclip
import time
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Model setup for generating responses using LLaMA 3.2
model_name = "meta-llama/Llama-3.2-3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate a response based on the prompt
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():  # Disable gradient computation for faster inference
        outputs = model.generate(**inputs, max_length=100)  # Adjust max_length as needed
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Step 1: Click on the icon at (990, 1058)
pyautogui.click(990, 1058)
time.sleep(1)  # Wait for the click action to complete
# Loop to keep checking for messages
while True:

    # Step 2: Drag from (669, 181) to (733, 943) to select text
    pyautogui.moveTo(669, 181)
    pyautogui.dragTo(733, 943, duration=0.5, button="left")

    # Step 3: Copy the selected text to clipboard
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(669, 181)  # Click again to unselect or reset position if needed
    time.sleep(0.5)  # Give time for the copy action to complete

    # Step 4: Retrieve the copied text from the clipboard
    copied_text = pyperclip.paste()
    print(f"Copied text: {copied_text}")  # Optional: verify copied text

    # Split copied text into lines and get the last line
    lines = copied_text.strip().split('\n')
    if lines:
        last_message = lines[-1]  # Get the last message
        sender_name = last_message.split(':')[0].strip()  # Extract sender's name

        # Check if the sender is not the bot
        if sender_name != "Arth":  # Replace "Arth" with your bot's name
            # Step 5: Generate response using the entire copied text as a prompt
            response = generate_response(copied_text)
            print(f"Generated response: {response}")

            # Step 6: Click on the specified coordinates
            pyautogui.click(1101, 978)  # Click at (1101, 978)
            time.sleep(0.5)  # Optional: wait for a moment before pasting

            # Step 7: Paste the generated response and press Enter
            pyperclip.copy(response)  # Copy the generated response to the clipboard
            pyautogui.hotkey("ctrl", "v")  # Paste the response
            time.sleep(0.5)  # Wait for a moment before pressing Enter
            pyautogui.press("enter")  # Press Enter

    # Optional: wait for a bit before checking again to avoid rapid looping
    time.sleep(5)  # Adjust this delay as necessary
