import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def diagnose(metrics):

    issues = []

    if metrics["CTR"] < 0.02:
        issues.append("Low CTR - Improve ad copy")

    if metrics["Conversion Rate"] < 0.05:
        issues.append("Low conversions - Adjust audience")

    if metrics["ROI"] < 4:
        issues.append("Negative ROI - Campaign losing money")

    return issues



def optimize_ad(ad_copy, metrics):

    prompt = f"""
    Improve this ad copy.

    Current Ad Copy:
    {ad_copy}

    Metrics:
    CTR: {metrics['CTR']}
    Conversion Rate: {metrics['Conversion Rate']}
    ROI: {metrics['ROI']}

    Return ONLY JSON:

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

    data = json.loads(json_text)

    return data