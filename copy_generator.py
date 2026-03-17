import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ad_copy(product_description):

    prompt = f"""
    You are an experienced and results-driven ads manager. Create high-converting ad copy for the following product:

    Product: {product_description}

    Ensure the copy is clear, engaging, and tailored to the target audience. Highlight the key benefits and unique selling points, craft a compelling headline, and include a strong call-to-action.
    Where possible, incorporate persuasive elements such as urgency, social proof, or emotional appeal, and ensure the tone aligns with the product and audience. 

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
    You are an experienced and data-driven marketing strategist. Suggest the most effective audience targeting for the following product:

    Product: {product_description}

    Analyze the product and determine the ideal customer profile, including demographics, psychographics, and platform behavior. Recommend targeting that maximizes reach, relevance, and conversion potential across advertising platforms.
    Base your suggestions on likely buyer intent, interests, and platform fit only the top 2 which would give best result for the product. Ensure the tone aligns with the target audience and product positioning.

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