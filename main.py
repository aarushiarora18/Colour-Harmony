import cv2
import numpy as np
import os
import pandas as pd
from sklearn.cluster import KMeans

def get_dominant_rgb(image, k=1):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(image)
    dominant = kmeans.cluster_centers_.astype(int)[0]
    return dominant.tolist()

data = []

base_path = 'images'
labels = ['warm', 'cool', 'neutral']

for label in labels:
    folder = os.path.join(base_path, label)
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                rgb = get_dominant_rgb(img)
                data.append([filename, *rgb, label])

# Save to CSV
df = pd.DataFrame(data, columns=['filename', 'R', 'G', 'B', 'skin_tone'])
df.to_csv('dataset.csv', index=False)
print("CSV created! ✅")

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

# Read the existing CSV
df = pd.read_csv('dataset.csv')

# Apply season classification
df['season'] = df.apply(lambda row: get_season(row['skin_tone'], row['R'], row['G'], row['B']), axis=1)

# Save it again
df.to_csv('dataset.csv', index=False)
print("Updated CSV with seasons! 🌸❄️🍂☀️")

def get_palette(season):
    palettes = {
        'Warm Spring': ['Peach', 'Coral', 'Warm Beige', 'Light Gold'],
        'Warm Autumn': ['Olive', 'Burnt Orange', 'Mustard', 'Terracotta'],
        'Cool Summer': ['Rose Pink', 'Lavender', 'Sky Blue', 'Dusty Lilac'],
        'Cool Winter': ['Jewel Tones', 'Fuchsia', 'Icy Blue', 'Charcoal'],
        'Soft Summer': ['Dusty Rose', 'Slate Blue', 'Mauve', 'Muted Lavender'],
        'Soft Autumn': ['Camel', 'Warm Taupe', 'Sage Green', 'Soft Rust']
    }
    return ', '.join(palettes.get(season, ['No Palette']))

# Add recommended palette column
df['recommended_palette'] = df['season'].apply(get_palette)

# Save final version
df.to_csv('dataset.csv', index=False)
print("Added recommended palettes! 🎨")
