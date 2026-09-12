from google import genai
from datetime import datetime

# ==========================================
# CONFIGURATION
# ==========================================

MODEL_NAME = "gemini-2.5-flash"

# ==========================================
# CHECK INVALID API KEY
# ==========================================

def is_invalid_key(error):
    error = str(error).lower()

    keywords = [
        "api key not valid",
        "invalid api key",
        "api_key_invalid",
        "unauthenticated",
        "401"
    ]

    return any(word in error for word in keywords)

# ==========================================
# ASK GEMINI
# ==========================================

def ask_gemini(client, question):

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question clearly and naturally.

USER QUESTION:
{question}
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if response.text:
            return response.text

        return "No response received."

    except Exception as e:

        error = str(e).lower()

        if "429" in error or "resource_exhausted" in error:
            return (
                "Gemini quota exceeded.\n"
                "Please wait for quota reset or upgrade billing."
            )

        if is_invalid_key(e):
            return "Invalid Gemini API Key."

        return f"Gemini Error: {e}"

# ==========================================
# MAIN PROGRAM
# ==========================================

print("=" * 70)
print("         GEMINI AI UNIVERSAL CHATBOT")
print("=" * 70)

api_key = input("\nEnter Gemini API Key: ").strip()

if not api_key:
    print("\nNo API key entered.")
    exit()

# ==========================================
# CONNECT TO GEMINI
# ==========================================

try:

    client = genai.Client(api_key=api_key)

    test = client.models.generate_content(
        model=MODEL_NAME,
        contents="Hello"
    )

    print("\n✓ API Key Verified")
    print("✓ Gemini Connected Successfully")

except Exception as e:

    if is_invalid_key(e):
        print("\n✗ Invalid Gemini API Key")

    elif "429" in str(e).lower():
        print("\n✗ Gemini Quota Exceeded")

    else:
        print("\n✗ Connection Failed")
        print(e)

    exit()

# ==========================================
# CHAT LOOP
# ==========================================

print("\n" + "=" * 70)
print("CHATBOT READY")
print("=" * 70)

print("""
Type anything and Gemini will answer.

Commands:
time  -> current time
date  -> current date
done  -> exit
exit  -> exit
quit  -> exit
""")

print("=" * 70)

while True:

    user_question = input("\nYou: ").strip()

    if not user_question:
        print("Please enter a question.")
        continue

    command = user_question.lower()

    if command in ["done", "exit", "quit"]:
        print("\nGemini AI: Goodbye!")
        break

    if command == "time":

        current_time = datetime.now().strftime(
            "%I:%M:%S %p"
        )

        print("\nGemini AI:")
        print(current_time)
        continue

    if command == "date":

        current_date = datetime.now().strftime(
            "%d-%m-%Y"
        )

        print("\nGemini AI:")
        print(current_date)
        continue

    answer = ask_gemini(
        client,
        user_question
    )

    print("\nGemini AI:")
    print("-" * 70)
    print(answer)
    print("-" * 70)

print("\nChatbot Closed Successfully.")