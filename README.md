# FreshFruits
Python script that takes a fruit image and outputs freshness score
Fruit Freshness Detector
This project is a Streamlit-based web application that detects the freshness of apples and bananas using image color analysis techniques. It utilizes simple image processing logic to estimate spoilage based on the presence of brown coloration in fruit images.

Features
Automatically processes and classifies images of apples and bananas

Determines fruit freshness using HSV color analysis

Displays individual image results with freshness labels and confidence scores

Generates a summary of freshness statistics for each fruit type

Responsive web layout for organized image display

How It Works
Images are loaded from a dataset directory (images/), which contains subfolders for each fruit type.

Each image is converted to HSV color space.

A mask is applied to detect brown areas, which are indicative of spoilage.

The ratio of brown area to total image area is calculated.

If the brown ratio is below 5%, the fruit is considered fresh; otherwise, it is labeled not fresh.

A freshness score is derived as:
score = 100 - int(brown_ratio * 1000) (score is capped at a minimum of 0)

Directory Structure
bash
Copy
Edit
Fruit-Freshness-Detector/
│
├── app.py               
├── images/               
│   ├── apple fruit/
│   │   ├── image1.jpg
│   │   └── ...
│   └── banana fruit/
│       ├── image1.jpg
│       └── ...
└── README.md              
Installation
Prerequisites
Python 3.7 or higher

Install Dependencies
pip install streamlit opencv-python-headless numpy pillow

Add Dataset
Place your images into the appropriate subfolders within the images/ directory:

images/apple fruit/

images/banana fruit/

Ensure all image files are in .jpg, .jpeg, or .png format.

Run the Application
streamlit run app.py
This will launch the application in your default web browser.

Notes
This implementation is based on simple HSV-based color thresholding.

It may not be robust against variations in lighting, background, or fruit varieties.

For improved accuracy, consider incorporating machine learning or deep learning techniques.

License
This project is open-source and available under the MIT License.

