#!/usr/bin/env python3
import os
import subprocess
import google.generativeai as genai

# Directly set your API key
api_key = "PLACE_YOUR_API_IN_HERE"

# Configure the Gemini API key
genai.configure(api_key=api_key)


# Adding Generative AI model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

def run_clamscan():
    result = subprocess.run(['clamscan', '-r', '/path/to/scan'], capture_output=True, text=True)
    return result.stdout

def send_report_to_generative_ai(report):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(report)
    return response.text

def main():
    report = run_clamscan()
    print("ClamAV Report:\n", report)
    
    response = send_report_to_generative_ai(report)
    print("Generative AI Response:\n", response)

if __name__ == "__main__":
    main()
