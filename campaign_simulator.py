import random

def calculate_ad_quality(ad_copy, marketing_details):

    score = 0.5

    # Better title improves score
    if "🚀" in ad_copy["title"]:
        score += 0.2

    # Strong CTA improves score
    if ad_copy["cta"].lower() in ["try it now", "start today", "get started"]:
        score += 0.1

    # Motivational tone helps engagement
    if marketing_details["tone"] == "motivational":
        score += 0.1

    # Interest match
    if "fitness" in marketing_details["interests"]:
        score += 0.1

    return min(score, 1.0)


def run_campaign(ad_copy, marketing_details):

    quality = calculate_ad_quality(ad_copy, marketing_details)

    impressions = random.randint(8000, 20000)

    # CTR depends on ad quality
    ctr = random.uniform(0.01, 0.02) + quality * 0.03

    clicks = int(impressions * ctr)

    # Conversion rate also depends on quality
    conversion_rate = random.uniform(0.02, 0.05) + quality * 0.1

    conversions = int(clicks * conversion_rate)

    cost = clicks * random.uniform(0.2, 0.6)

    revenue = conversions * random.uniform(15, 40)

    data = {
        "impressions": impressions,
        "clicks": clicks,
        "conversions": conversions,
        "cost": cost,
        "revenue": revenue
    }

    return data