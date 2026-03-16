from image_analyzer import analyze_image
from copy_generator import generate_ad_copy, suggest_marketing_details
from campaign_simulator import run_campaign
from monitoring_engine import calculate_metrics
from optimization_agent import diagnose, optimize_ad



image_path = "ad_image.jpg"
product_description = input("Enter product description: ")


analysis = analyze_image(image_path, product_description)



ad_copy = generate_ad_copy(product_description)

print("\nGenerated Ad Copy:")
print(ad_copy)



marketing_details = suggest_marketing_details(product_description)

print("\nSuggested Marketing Details:")
print(marketing_details)



campaign_data = run_campaign(ad_copy, marketing_details)

print("\nCampaign Data:")
print(campaign_data)



metrics = calculate_metrics(campaign_data)

print("\nPerformance Metrics:")
print(metrics)



issues = diagnose(metrics)

print("\nAgent Diagnosis:")
print(issues)



if issues:
    improved_copy = optimize_ad(ad_copy,metrics)

    print("\nOptimized Ad Copy:")
    print(improved_copy)

    print("\nRunning new simulation...")

    campaign_data = run_campaign(improved_copy, marketing_details)
    metrics = calculate_metrics(campaign_data)

    print("\nNew Metrics:")
    print(metrics)