import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Helper functions
# ------------------------------
def random_palette(k=5):
    """Return k random pastel-like colors."""
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    """Generate a wobbly closed shape (a blob)."""
    angles = np.linspace(0, 2*math.pi, points)
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🎨 Generative Abstract Poster")
st.subheader("Concepts: randomness, lists, loops, functions, matplotlib")

st.sidebar.header("Poster Controls")

# Controls
n_layers = st.sidebar.slider("Number of layers", 3, 15, 8)
palette_size = st.sidebar.slider("Palette size", 3, 10, 6)
background_color = st.sidebar.color_picker("Background color", "#fafaf8")
randomize = st.sidebar.button("🔀 Generate New Poster")

# ------------------------------
# Generate Poster
# ------------------------------
if randomize:
    random.seed()  # new random art each click

palette = random_palette(palette_size)

fig, ax = plt.subplots(figsize=(7, 10))
ax.axis("off")
ax.set_facecolor(background_color)

for i in range(n_layers):
    cx, cy = random.random(), random.random()
    rr = random.uniform(0.15, 0.45)
    x, y = blob(center=(cx, cy), r=rr, wobble=random.uniform(0.05, 0.25))
    color = random.choice(palette)
    alpha = random.uniform(0.25, 0.6)
    ax.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

# Typography
ax.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=ax.transAxes)
ax.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# ------------------------------
# Display
# ------------------------------
st.pyplot(fig)

st.caption("Each time you click 'Generate New Poster', a new random composition is created.")

