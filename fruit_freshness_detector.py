import streamlit as st
import cv2
import os
import numpy as np
from PIL import Image

st.set_page_config(layout="wide", page_title="Fruit Freshness Detector 🍎🍌")

st.title("🍏 Fruit Freshness Detector")
st.markdown("Detects freshness of apple and banana fruits based on image color analysis.")

# Directory containing fruit folders
dataset_dir = "images"

# Result counters
results = {
    "apple fruit": {"Fresh": 0, "Not Fresh": 0},
    "banana fruit": {"Fresh": 0, "Not Fresh": 0}
}

def detect_freshness(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None, None, None

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_brown = np.array([5, 50, 20])
    upper_brown = np.array([20, 255, 200])
    brown_mask = cv2.inRange(hsv, lower_brown, upper_brown)

    brown_area = cv2.countNonZero(brown_mask)
    total_area = image.shape[0] * image.shape[1]
    brown_ratio = brown_area / total_area

    score = 100 - int(brown_ratio * 1000)
    score = max(score, 0)

    if brown_ratio < 0.05:
        label = "Fresh"
    else:
        label = "Not Fresh"

    return label, score, image

# Main display logic
if os.path.exists(dataset_dir):
    for fruit_type in os.listdir(dataset_dir):
        fruit_path = os.path.join(dataset_dir, fruit_type)
        if not os.path.isdir(fruit_path):
            continue

        st.header(f"📦 {fruit_type.capitalize()}")
        cols = st.columns(3)

        i = 0
        for img_name in os.listdir(fruit_path):
            img_path = os.path.join(fruit_path, img_name)
            label, score, image = detect_freshness(img_path)
            if label is None:
                continue

            results[fruit_type][label] += 1

            # Prepare label image
            image = cv2.resize(image, (300, 300))
            color = (0, 255, 0) if label == "Fresh" else (0, 0, 255)
            cv2.putText(image, f"{label} - {score}%", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            # Convert BGR to RGB for Streamlit
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            with cols[i % 3]:
                st.image(image_rgb, caption=f"{img_name} - {label} ({score}%)", use_column_width=True)
            i += 1

    # Show summary
    st.subheader("📊 Freshness Summary")
    for fruit, counts in results.items():
        total = counts["Fresh"] + counts["Not Fresh"]
        if total == 0:
            continue
        fresh_pct = (counts["Fresh"] / total) * 100
        not_fresh_pct = (counts["Not Fresh"] / total) * 100

        st.markdown(f"**{fruit.capitalize()}**")
        st.write(f"✅ Fresh: {counts['Fresh']} ({fresh_pct:.1f}%)")
        st.write(f"❌ Not Fresh: {counts['Not Fresh']} ({not_fresh_pct:.1f}%)")
else:
    st.warning("No images found. Make sure the `images/` folder exists and contains fruit subfolders.")
