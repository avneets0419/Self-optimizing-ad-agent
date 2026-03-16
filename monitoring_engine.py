def calculate_metrics(data):

    impressions = data["impressions"]
    clicks = data["clicks"]
    conversions = data["conversions"]
    cost = data["cost"]
    revenue = data["revenue"]

    ctr = clicks / impressions if impressions else 0
    conversion_rate = conversions / clicks if clicks else 0
    cpc = cost / clicks if clicks else 0
    roi = (revenue - cost) / cost if cost else 0

    metrics = {
        "CTR": ctr,
        "Conversion Rate": conversion_rate,
        "CPC": cpc,
        "ROI": roi
    }

    return metrics