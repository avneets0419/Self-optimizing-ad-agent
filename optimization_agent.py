import os
from groq import Groq
from dotenv import load_dotenv
import re

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def diagnose(metrics):

    issues = []

    if metrics["CTR"] < 0.02:
        issues.append("Low CTR - Improve ad copy")

    if metrics["Conversion Rate"] < 0.05:
        issues.append("Low conversions - Adjust audience")

    if metrics["ROI"] < 10:
        issues.append("Negative ROI - Campaign losing money")

    return issues



def optimize_ad(ad_copy, metrics,issues):

    prompt = f"""

    
    You are an experienced and results-driven ads manager. Review and improve the following ad copy to maximize performance, clarity, and conversions. The campaign is currently facing these issues: {','.join(issues)}.

    Ensure the revised copy is engaging, audience-focused, and aligned with best practices for high-performing ads. Strengthen the headline, refine the value proposition, include a compelling call-to-action, and address any gaps contributing to the listed issues. Provide multiple improved variations if possible, along with a brief explanation of the changes made.

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

    match = re.search(r"\{.*?\}", response_text, re.DOTALL)

    if not match:
        raise ValueError("No valid JSON found in LLM response")

    json_text = match.group()

    data = json.loads(json_text)

    return data