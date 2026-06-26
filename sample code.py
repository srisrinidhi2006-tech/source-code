import os
import google.generativeai as genai

# Get API key from environment variable
api_key = os.getenv('GEMINI_API_KEY')

if api_key:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content('Hello, Gemini!')
        print('Gemini API key is working! Here is a test response:')
        print(response.text)
    except Exception as e:
        print(f'There was an error using the Gemini API: {e}')
        print('Please check your API key and ensure it is valid and configured correctly.')
else:
    print('GEMINI_API_KEY not found in environment variables. Set it using:')
    print('  Windows: set GEMINI_API_KEY=your_key_here')
    print('  Linux/Mac: export GEMINI_API_KEY=your_key_here')