import subprocess
import google.generativeai as gemini_ai

# Define your API key here
GEMINI_API_KEY = "your_gemini_api_key_here"

def run_clamscan():
    result = subprocess.run(['clamscan', '-r', '/path/to/scan'], capture_output=True, text=True)
    return result.stdout

def send_report_to_generative_ai(report):
    gemini_ai.Client.configure(api_key=GEMINI_API_KEY)
    response = gemini_ai.TextGenerator.generate(prompt=report, max_tokens=100)
    return response

def main():
    report = run_clamscan()
    print("ClamAV Report:\n", report)
    
    response = send_report_to_generative_ai(report)
    print("Generative AI Response:\n", response)

if __name__ == "__main__":
    main()
