from groq import Groq
from dotenv import load_dotenv
import os
import base64
import json
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_image(image_path, product_description):

    print("\nAnalyzing ad creative with AI...")

     # Convert image to base64
    image_base64 = encode_image(image_path)

    prompt = f"""
    You are an expert visual marketing analyst.

    IMPORTANT:
    - The IMAGE is the PRIMARY source of truth.
    - The product description is SECONDARY.
    - If there is a conflict, TRUST THE IMAGE MORE.

    Product Description:
    {product_description}

    Analyze the advertisement image.

    Return JSON:

    {{
        "image_theme": "...",
        "visual_elements": ["...", "..."],
        "target_emotion": "...",
        "recommended_style": "...",
        "product_match_score": "low/medium/high",
        "mismatch_detected": true/false,
        "reason_for_mismatch": "...",
        "improvement_suggestions": ["...", "..."]
    }}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt + "\n\nImage (base64): " + image_base64[:1000]  # limit size
            }
        ]
    )

    response_text = completion.choices[0].message.content

    # Extract JSON safely
    match = re.search(r"\{.*?\}", response_text, re.DOTALL)

    if match:
        return json.loads(match.group())

    # fallback
    return {
        "image_theme": "unknown",
        "visual_elements": [],
        "target_emotion": "neutral",
        "recommended_style": "general",
        "improvement_suggestions": []
    }