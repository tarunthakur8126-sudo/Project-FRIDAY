import requests
import json

def friday_ai():
    print("==========================================")
    print("   🤖 PROJECT FRIDAY: ONLINE & READY   ")
    print("==========================================")
    print("Sir, main hamesha ki tarah aapke liye hazir hoon.")
    print("Aapka agla coding project kya hai?\n")

    while True:
        # Aapka input lene ke liye
        prompt = input("➤ Aapka Command (ya 'exit' likhein): ")

        if prompt.lower() in ['exit', 'quit', 'bye']:
            print("\nShutting down... Goodbye, Sir.")
            break

        print("\n⏳ Friday is thinking and coding for you...")

        try:
            # Ye API Friday ko dimaag deti hai
            url = "https://api.blackbox.ai/api/chat"
            headers = {"Content-Type": "application/json"}
            payload = {
                "messages": [
                    {
                        "role": "user", 
                        "content": f"You are FRIDAY, a master AI coder. Provide high-quality code and a simple explanation for: {prompt}"
                    }
                ],
                "model": "deepseek-v3", # Latest model for coding
                "max_tokens": 4000
            }
            
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            
            if response.status_code == 200:
                # Code extract karna
                result = response.json()['messages'][-1]['content']
                print("\n✅ FRIDAY: Kaam ho gaya! Ye raha aapka code:\n")
                print("-" * 50)
                print(result)
                print("-" * 50)
                print("\nSir, kya main is code mein kuch aur changes karoon?")
            else:
                print(f"Error: Server se connection nahi ho paya (Status: {response.status_code})")

        except Exception as e:
            print(f"Oops! Kuch technical issue hai: {e}")

if __name__ == "__main__":
    friday_ai()
