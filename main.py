import streamlit as st

from image_analyzer import analyze_image
from copy_generator import generate_ad_copy, suggest_marketing_details
from campaign_simulator import run_campaign
from monitoring_engine import calculate_metrics
from optimization_agent import diagnose, optimize_ad


# CONFIG
MAX_ITERATIONS = 3

st.set_page_config(page_title="Agentic AI Ad Manager", layout="wide")

st.title("🚀 Agentic AI Ad Manager")
st.write("Generate, test, and optimize ad campaigns using AI")

# USER INPUT
product_description = st.text_input("Enter Product Description", "AI Fitness App")

uploaded_file = st.file_uploader("Upload Ad Creative Image", type=["jpg", "png"])

if st.button("Run Campaign"):

    if not product_description:
        st.warning("Please enter a product description")
        st.stop()

    image_path = None

    # Save uploaded image
    if uploaded_file:
        image_path = "ad_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.read())

    # Handle both cases
    if image_path:
        analysis = analyze_image(image_path, product_description)
        if analysis.get("mismatch_detected"):
            st.error("⚠️ Image does not match product!")

    else:
        analysis = {
            "image_theme": "No image provided",
            "product_description": product_description,
            "visual_elements": [],
            "target_emotion": "unknown",
            "recommended_style": "general",
            "improvement_suggestions": []
        }

    st.subheader("🧠 Creative Analysis")
    st.write(analysis)

    # STEP 2 — Generate Ad Copy
    ad_copy = generate_ad_copy(product_description)

    st.subheader("✍️ Generated Ad Copy")
    st.json(ad_copy)

    # STEP 3 — Marketing Details
    marketing_details = suggest_marketing_details(product_description)

    st.subheader("🎯 Marketing Strategy")
    st.json(marketing_details)

    # AGENT LOOP
    for i in range(MAX_ITERATIONS):

        st.markdown(f"---")
        st.subheader(f"📊 Campaign Run {i+1}")
        if i > 0:
            ad_copy = optimize_ad(ad_copy, metrics,issues)

            st.subheader("✨ Improved Ad Copy")
            st.json(ad_copy)

        # Run campaign
        campaign_data = run_campaign(ad_copy, marketing_details)
        st.write("Campaign Data:", campaign_data)

        # Metrics
        metrics = calculate_metrics(campaign_data)
        st.write("Performance Metrics:", metrics)

        # Diagnose
        issues = diagnose(metrics)
        st.write("Agent Diagnosis:", issues)

        # Check if good
        if not issues:
            st.success("✅ Campaign is performing well. No optimization needed.")
            break

        # Optimize
        st.warning("⚠️ Optimizing Ad Copy using AI...")

        

    else:
        st.error("❌ Max iterations reached. Performance still below threshold.")