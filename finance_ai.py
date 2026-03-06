import google.generativeai as genai
import os

# 1. INITIALIZE THE CLIENT
# It is best to replace "YOUR_API_KEY" with the actual key you just got.
client = genai.Client(api_key="AIzaSyApviOTFoJYht1218U5Z9ijH2W6Sv25vBs")

def get_financial_advice(income, expenses, savings):
    """
    Takes financial data and returns AI-generated advice using Gemini 3 Flash.
    """
    # 2. CRAFT THE PROMPT
    prompt = f"""
    You are a professional financial advisor. 
    Analyze the following data:
    - Monthly Income: ${income}
    - Monthly Expenses: ${expenses}
    - Current Savings: ${savings}
    
    Provide a concise 3-step plan to improve this person's financial health.
    """

    try:
        # 3. CALL THE 2026 GENERATE CONTENT METHOD
        # 'gemini-2.0-flash' or 'gemini-3-flash' are the current standards.
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt
        )
        
        # 4. RETURN THE TEXT DATA
        return response.text

    except Exception as e:
        return f"Error generating advice: {str(e)}"

# Example usage (for testing):
if __name__ == "__main__":

    print(get_financial_advice(5000, 3000, 10000))
