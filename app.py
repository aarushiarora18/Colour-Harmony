import streamlit as st
import cv2
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates


def get_rgb_at_point(image, x, y):
    return image[y, x].tolist()

def get_season(skin_tone, r, g, b):
    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    if skin_tone == 'warm':
        return 'Warm Spring' if brightness > 150 else 'Warm Autumn'
    elif skin_tone == 'cool':
        return 'Cool Summer' if brightness > 150 else 'Cool Winter'
    elif skin_tone == 'neutral':
        return 'Soft Summer' if brightness > 150 else 'Soft Autumn'
    else:
        return 'Unknown'

def get_palette(season):
    palettes = {
    'Warm Spring': [
        '#FF7F50',  # Coral
        '#FFDAB9',  # Peach
        '#FFF8DC',  # Warm ivory
        '#FFD700',  # Golden yellow
        '#40E0D0',  # Turquoise
        '#FF69B4',  # Warm pink
        '#C3CDE6',  # Light periwinkle
        '#7CFC00'   # Leaf green
    ],
    'Warm Autumn': [
        '#808000',  # Olive green
        '#CC5500',  # Burnt orange
        '#FFDB58',  # Mustard yellow
        '#E2725B',  # Terracotta
        '#F5DEB3',  # Warm beige
        '#B7410E',  # Rust
        '#006D5B',  # Deep teal
        '#8B4513'   # Chocolate brown
    ],
    'Cool Summer': [
        '#DCAE96',  # Dusty rose
        '#B0E0E6',  # Powder blue
        '#E6E6FA',  # Lavender
        '#98FF98',  # Cool mint
        '#6A5ACD',  # Soft navy
        '#D3D3D3',  # Sky gray
        '#C8A2C8',  # Light mauve
        '#9FE2BF'   # Seafoam green
    ],
    'Cool Winter': [
        '#4169E1',  # Royal blue
        '#50C878',  # Emerald green
        '#990000',  # Cool crimson
        '#FFDEE9',  # Icy pink
        '#000000',  # Jet black
        '#FFFFFF',  # Bright white
        '#FF00FF',  # Fuchsia
        '#0047AB'   # Cobalt blue
    ],
    'Soft Summer': [
        '#B0C4DE',  # Misty blue
        '#C8A2C8',  # Dusty lavender
        '#9DC183',  # Sage green
        '#D8BFD8',  # Soft mauve
        '#D8CAB8',  # Light taupe
        '#FADADD',  # Powder pink
        '#7393B3',  # Blue-gray
        '#66A5AD'   # Dusty teal
    ],
    'Soft Autumn': [
        '#9DC183',  # Sage
        '#BAB86C',  # Soft olive
        '#D2B48C',  # Warm taupe
        '#F88379',  # Muted coral
        '#FFDAB9',  # Dusty peach
        '#967969',  # Mocha
        '#D4AF37',  # Muted gold
        '#E9967A'   # Soft terracotta
    ]
}

    return palettes.get(season, ['#FFFFFF'])  


st.set_page_config(page_title="Color Analysis", layout="centered")
st.markdown("<style>div[data-testid='stImage'] img {cursor: crosshair;}</style>", unsafe_allow_html=True)

st.title("Colour Harmony 🎨 Find your recommended palette as per your Skin Tone!")

st.write("🔎 **Instruction:** Click on your skin area to pick the color!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

skin_tone = st.selectbox("Select your skin tone:", ['warm', 'cool', 'neutral'])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)

    st.write("🧪 **Dropper activated! Click to pick a color below:**")

    coords = streamlit_image_coordinates(image)

    if coords is not None:
        x = int(coords['x'])
        y = int(coords['y'])

        st.write(f"You clicked at: **({x}, {y})**")

        r, g, b = get_rgb_at_point(img_array, x, y)
        st.write(f"**Selected RGB Color:** [{r}, {g}, {b}]")

        season = get_season(skin_tone, r, g, b)
        st.success(f"Predicted Season: **{season}**")

        palette = get_palette(season)
        st.write("### Recommended Colors:")

        cols = st.columns(4)  

        for idx, hex_color in enumerate(palette):
            with cols[idx % 4]:
                st.markdown(
                    f"<div style='width:100%; height:60px; background-color:{hex_color}; border-radius:10px'></div>",
                    unsafe_allow_html=True
                )
                st.caption(hex_color)
