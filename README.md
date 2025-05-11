# Colour Harmony: AI for Skin Tone Detection and Palette Prediction

This project is an AI-based application that recommends personalized color palettes based on a user’s skin tone using image analysis and machine learning.

## Problem Statement

Selecting the right colors to complement an individual's natural skin tone can be difficult. Traditional methods are manual, subjective, and time-consuming. This project provides an automated solution for detecting skin tone and recommending a suitable seasonal color palette.

## Objective

- Predict a user’s skin undertone and seasonal color type using an uploaded image.
- Recommend a personalized color palette based on the prediction.
- Simplify and automate the color analysis process for better decision-making in fashion, makeup, and accessories.

## Solution Overview

- Built a web application using **Streamlit** for easy interaction.
- Users upload an image and click to select a skin tone region.
- The app uses **KMeans Clustering** to determine the dominant skin tone.
- A rule-based logic determines the season type (e.g., Warm Spring, Cool Winter).
- A tailored color palette is displayed based on the user's detected season.

## Technologies Used

- Python
- Streamlit
- OpenCV (for image processing)
- Pandas (for data handling)
- Scikit-learn (for KMeans clustering)

## Methodology

- **Image Processing**: Convert and reshape images using OpenCV.
- **KMeans Clustering**: Identify the dominant skin color cluster.
- **Tone Classification**: Brightness-based logic to determine light or deep tone.
- **Season Mapping**: Categorize into seasonal palettes based on RGB and tone.
- **Data Logging**: Store all results in a CSV file (`dataset.csv`) for analysis.

## Key Features

- Web app interface for uploading and selecting image points.
- Automatic skin tone detection using unsupervised learning.
- Rule-based seasonal classification and palette display.
- Lightweight and easy to use, with potential for real-world application.

## Conclusion

This project demonstrates how computer vision and machine learning can be applied to solve real-world fashion and design challenges. It automates color harmony analysis and empowers users with instant and accurate suggestions.

> "The best colour in the whole world is the one that looks good on you." – Coco Chanel
