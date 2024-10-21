import tkinter as tk
from datetime import datetime

# Function to handle sending messages and bot responses
def send_message(event=None):  # Modified to send message on Enter key press
    user_message = user_input.get().strip()
    if user_message == "":
        return  # Ignore empty messages

    display_message(user_message, "user")  # Show user message
    user_input.delete(0, tk.END)  # Clear input field

    # Generate and display bot response
    bot_response = get_bot_response(user_message.lower())
    chat_window.after(500, lambda: display_message(bot_response, "bot"))  # Simulate response delay

# Function to display messages in the chat window
def display_message(message, sender):
    frame = tk.Frame(chat_window, bg=chat_bg_color, padx=10, pady=5)

    if sender == "user":
        msg_label = tk.Label(frame, text=message, bg=user_bg_color, fg="white",
                             font=("Arial", 12), wraplength=250, justify="right")
        msg_label.pack(anchor="e")
    else:
        msg_label = tk.Label(frame, text=message, bg=bot_bg_color, fg="black",
                             font=("Arial", 12), wraplength=250, justify="left")
        msg_label.pack(anchor="w")

    frame.pack(anchor="w" if sender == "bot" else "e", padx=10, pady=2)
    chat_window.update_idletasks()
    chat_window.yview_moveto(1.0)  # Scroll to bottom

# Function to generate bot responses based on user input
def get_bot_response(input):
    if "hello" in input or "hi" in input:
        return "Hello! 😊 How can I assist you today?"
    elif "your name" in input:
        return "I'm your friendly chatbot 🤖. What's your name?"
    elif "weather" in input:
        return "I can help with weather updates 🌦️. Which city's weather do you need?"
    elif "time" in input:
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰."
    elif "joke" in input:
        return "Why don't scientists trust atoms? Because they make up everything! 😄"
    elif "bye" in input or "exit" in input:
        return "Goodbye! Have a nice day! 👋"
    elif "love" in input:
        return "Love is in the air! ❤️"
    elif "sad" in input:
        return "I'm here to cheer you up! 🌻 You're amazing!"
    else:
        return "I'm sorry, I didn't understand that. 🤔 Could you rephrase?"

# Create the main application window
root = tk.Tk()
root.title("AI Chatbot 🤖")
root.geometry("400x500")
root.config(bg="#e0f7fa")  # Light blue background

# Define custom colors for chat window
chat_bg_color = "#bbdefb"  # Light blue for chat background
user_bg_color = "#1e88e5"  # Blue for user messages
bot_bg_color = "#e3f2fd"   # Very light blue for bot messages

# Chat window to display messages
chat_window = tk.Text(root, bg=chat_bg_color, fg="black", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.DISABLED)  # Make chat window read-only

# Frame for user input and send button
input_frame = tk.Frame(root, bg="#e0f7fa")
input_frame.pack(pady=10)

# User input field with rounded corners and border styling
user_input = tk.Entry(input_frame, font=("Arial", 14), width=25,
                      relief="flat", bg="#e1f5fe", highlightthickness=1, highlightbackground="#64b5f6")
user_input.grid(row=0, column=0, padx=10, ipady=5)  # Added padding for better appearance

# Bind Enter key to send message
user_input.bind("<Return>", send_message)

# Send button with blue styling
send_button = tk.Button(input_frame, text="Send", font=("Arial", 12), bg="#1e88e5", fg="white",
                        relief="flat", command=send_message)
send_button.grid(row=0, column=1)

# Start the Tkinter event loop
root.mainloop()
