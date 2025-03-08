import os
import google.generativeai as genai

# Step 1: Configure Gemini API Key
GEMINI_API_KEY = "AIzaSyBXD8YgGGsmWcUNQZyzy21DjfaueACQl-g"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Step 2: Set up Model Configuration
generation_config = {
    "temperature": 0.7,  # Less creativity for accurate responses
    "top_p": 0.95,
    "top_k": 50,
    "max_output_tokens": 1024,
}

# Step 3: Initialize the Model
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",  # Ensure this matches the supported model name
    generation_config=generation_config,
)

# Step 4: Define Initial Health Context and Instructions
initial_context = [
    {"role": "user", "parts": ["Hello!"]},
    {"role": "model", "parts": ["Hello! I’m your health assistant. How can I help you today?"]}
]

# Step 5: Define the Health Chatbot Function
def health_chatbot():
    global initial_context
    chat_session = model.start_chat(history=initial_context)

    print("Health-Specific Chatbot (Type 'exit' to end the chat)")
    while True:
        # Step 6: Get User Input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Take care of your health.")
            break
        
        # Step 7: Send Message to Model
        try:
            response = chat_session.send_message(user_input)
            parsed_response = parse_medical_condition(response.text)
            print(f"Chatbot: Medical Condition: {parsed_response}")

            # Step 8: Update Context (optional, to persist the conversation)
            initial_context.append({"role": "user", "parts": [user_input]})
            initial_context.append({"role": "model", "parts": [response.text]})
 
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def parse_medical_condition(response_text):
    # Logic to parse the response and extract the medical condition
    # Replace this with your actual logic based on the model's response format
    # Example: Extracting medical condition assuming the format is predictable
    # This part needs to be tailored to how responses are structured by your model
    medical_condition = response_text  # Placeholder, replace with actual parsing logic
    return medical_condition

# Step 9: Run the Health Chatbot
if __name__ == "__main__":
    health_chatbot()
