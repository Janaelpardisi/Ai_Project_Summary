import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

#  Set your Google Gemini API Key here
GOOGLE_API_KEY =os.getenv(" GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

def summarize_text(text):
    # Prepare the prompt for summarization
    prompt = f"Summary this text:\n\n{text}"
    
    # Generate the summary from the model
    response = model.generate_content(prompt)
    
    return response.text