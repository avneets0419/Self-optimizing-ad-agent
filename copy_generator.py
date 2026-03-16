import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ad_copy(product_description):

    prompt = f"""
    Create ad copy for this product.

    Product: {product_description}

    Return ONLY valid JSON in this format:

    {{
        "title": "...",
        "description": "...",
        "cta": "..."
    }}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    import json

    response_text = completion.choices[0].message.content

    start = response_text.find("{")
    end = response_text.rfind("}") + 1

    json_text = response_text[start:end]

    ad_copy = json.loads(json_text)

    return ad_copy


def suggest_marketing_details(product_description):

    prompt = f"""
    Suggest marketing targeting for this product.

    Product: {product_description}

    Return ONLY valid JSON:

    {{
        "age_group": "...",
        "gender": "...",
        "interests": ["...", "..."],
        "platform": "...",
        "tone": "..."
    }}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    import json

    response_text = completion.choices[0].message.content

    start = response_text.find("{")
    end = response_text.rfind("}") + 1

    json_text = response_text[start:end]

    data = json.loads(json_text)

    return data