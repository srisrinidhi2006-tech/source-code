import urllib.request
import json
import os
from datetime import datetime

# ==================== CONFIG ====================
API_KEY = "gsk_your_actual_key_here"   # ← REPLACE WITH YOUR GROQ KEY

# Sample prompts
prompts = [
    "Explain machine learning in one simple paragraph.",
    "Write a short funny poem about Python programming.",
    "What are the top 3 benefits of learning to code in 2026?"
]

print("🚀 Free Groq AI API Demo (Using only standard library)")
print("=" * 65)

# ==================== MAKE API CALLS ====================
for i, prompt in enumerate(prompts, 1):
    print(f"\n📝 Request {i}:")
    print(f"   {prompt}")
    print("-" * 50)
    
    try:
        url = "[https://api.groq.com/openai/v1/chat/completions](https://api.groq.com/openai/v1/chat/completions)"
        
        payload = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 300
        }
        
        data = json.dumps(payload).encode("utf-8")
        
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            ai_text = result["choices"][0]["message"]["content"].strip()
            
            print("✅ Response:")
            print(ai_text)
            print("=" * 65)
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code} - {e.reason}")
        print("   Check your API key and internet connection.")
    except Exception as e:
        print(f"❌ Error: {e}")

print(f"\n✅ Completed at {datetime.now().strftime('%H:%M:%S')}")
