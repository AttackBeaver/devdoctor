import os
from typing import List, Dict

def get_ai_suggestions(results: List[Dict]) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        return "OpenAI library not installed. Use 'pip install devdoctor[ai]'."

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OPENAI_API_KEY not found in environment."

    client = OpenAI(api_key=api_key)
    
    failed_checks = [r for r in results if r["status"] != "OK"]
    if not failed_checks:
        return "Everything looks great! No AI suggestions needed."

    prompt = "I have the following issues in my development environment:\n"
    for r in failed_checks:
        prompt += f"- {r['check']}: {r['message']}\n"
    prompt += "\nProvide concise, expert advice on how to fix these issues."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content or "No suggestions received."
    except Exception as e:
        return f"AI Error: {str(e)}"
