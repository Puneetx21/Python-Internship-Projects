import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from dotenv import load_dotenv
import os
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='matplotlib')

print("Starting Weather Dashboard...")

# -----------------------------
# Setup & API
# -----------------------------
load_dotenv()
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    print("ERROR: Set API_KEY in .env file")
    exit()

# Styling
plt.style.use("seaborn-v0_8-darkgrid")
sns.set_palette("mako")
plt.rcParams["axes.facecolor"] = "#0f172a"
plt.rcParams["figure.facecolor"] = "#020617"
plt.rcParams["savefig.facecolor"] = "#020617"
plt.rcParams["axes.labelcolor"] = "white"
plt.rcParams["xtick.color"] = "white"
plt.rcParams["ytick.color"] = "white"
plt.rcParams["text.color"] = "white"
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlepad"] = 10
plt.rcParams["font.size"] = 10

# -----------------------------
# Input
# -----------------------------
user_input = input("Enter locations (comma-separated): ")
locations = [loc.strip() for loc in user_input.split(',') if loc.strip()]

if not locations:
    print("No locations provided. Exiting.")
    exit()

print(f"Fetching data for: {locations}")

# -----------------------------
# Data collection
# -----------------------------
data_list = []
for loc_name in locations:
    # If user passes "lat,lon"
    if ',' in loc_name and len(loc_name.split(',')) == 2:
        lat, lon = [x.strip() for x in loc_name.split(',')]
        city_query = f"lat={lat}&lon={lon}"
        pretty_name = f"{lat},{lon}"
    else:
        # Geocode city → lat/lon
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={loc_name},IN&limit=1&appid={API_KEY}"
        geo_resp = requests.get(geo_url)

        if geo_resp.status_code == 200 and geo_resp.json():
            geo_data = geo_resp.json()[0]
            lat, lon = geo_data["lat"], geo_data["lon"]
            city_query = f"lat={lat}&lon={lon}"
            pretty_name = geo_data.get("name", loc_name)
        else:
            print(f" Cannot find {loc_name}")
            continue

    # Current weather
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?{city_query}&appid={API_KEY}&units=metric"
    weather_resp = requests.get(weather_url)

    if weather_resp.status_code == 200:
        w_data = weather_resp.json()
        main = w_data["main"]
        wind = w_data.get("wind", {})
        clouds = w_data.get("clouds", {}).get("all", np.nan)

        # AQI
        aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?{city_query}&appid={API_KEY}"
        aqi_resp = requests.get(aqi_url)
        aqi = aqi_resp.json()["list"][0]["main"]["aqi"] if aqi_resp.status_code == 200 else np.nan

        row = {
            "Location": pretty_name,
            "Temp (°C)": main.get("temp", np.nan),
            "Pressure (hPa)": main.get("pressure", np.nan),
            "Humidity (%)": main.get("humidity", np.nan),
            "Wind Speed (m/s)": wind.get("speed", np.nan),
            "Cloudiness (%)": clouds,
            "AQI (1-5)": aqi,
        }
        data_list.append(row)

        print(
            f"{pretty_name}: "
            f"{row['Temp (°C)']:.1f}°C, "
            f"Humidity: {row['Humidity (%)']:.0f}%, "
            f"Wind: {row['Wind Speed (m/s)']:.1f} m/s, "
            f"AQI: {aqi}"
        )
    else:
        print(f"{loc_name}: Weather API error (status {weather_resp.status_code})")

if not data_list:
    print("No data collected. Exiting.")
    exit()

df = pd.DataFrame(data_list)
print("\n Data ready:")
print(df)

# -----------------------------
# Single dashboard layout
# -----------------------------
fig = plt.figure(figsize=(14, 8))
fig.suptitle(
    f"City Weather Dashboard  •  {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    fontsize=18,
    fontweight="bold",
    color="white",
)

gs = fig.add_gridspec(
    3,
    1,
    height_ratios=[2.4, 0.8, 1.2],  # main chart, AQI strip, text table
    hspace=0.35,
)

ax_main = fig.add_subplot(gs[0, 0])
ax_aqi = fig.add_subplot(gs[1, 0])
ax_text = fig.add_subplot(gs[2, 0])

# -----------------------------
# 1) Main grouped bar chart
# -----------------------------
metrics = ["Temp (°C)", "Humidity (%)", "Wind Speed (m/s)"]
metric_colors = ["#f97316", "#22c55e", "#3b82f6"]  # orange, green, blue

x = np.arange(len(df))
width = 0.22
offsets = [-width, 0, width]

for metric, color, offset in zip(metrics, metric_colors, offsets):
    values = pd.to_numeric(df[metric], errors="coerce").fillna(0)
    bars = ax_main.bar(
        x + offset,
        values,
        width,
        label=metric,
        color=color,
        alpha=0.9,
        edgecolor="#0b1120",
        linewidth=1,
    )
    # Value labels
    for bar in bars:
        h = bar.get_height()
        ax_main.text(
            bar.get_x() + bar.get_width() / 2,
            h + (0.02 * max(values) if max(values) else 0.5),
            f"{h:.1f}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="white",
        )

ax_main.set_title("Core Weather Metrics by City", fontsize=14)
ax_main.set_xticks(x)
ax_main.set_xticklabels(df["Location"], rotation=15, ha="right")
ax_main.set_ylabel("Value")
ax_main.legend(
    loc="upper left",
    frameon=False,
    fontsize=9,
)
ax_main.grid(axis="y", alpha=0.3, linestyle="--", linewidth=0.5)

# -----------------------------
# 2) AQI horizontal bar strip
# -----------------------------
aqi_values = pd.to_numeric(df["AQI (1-5)"], errors="coerce").fillna(0)
# Color mapping: good (1) green -> poor (5) red
cmap = plt.get_cmap("RdYlGn_r")
norm = plt.Normalize(1, 5)
colors = [cmap(norm(v if v >= 1 else 3)) for v in aqi_values]

ax_aqi.bar(
    df["Location"],
    aqi_values,
    color=colors,
    edgecolor="#020617",
    linewidth=1.0,
)
for i, v in enumerate(aqi_values):
    ax_aqi.text(
        i,
        v + 0.05,
        f"{int(v)}" if v > 0 else "N/A",
        ha="center",
        va="bottom",
        fontsize=9,
        color="white",
    )

ax_aqi.set_ylim(0, max(aqi_values.max(), 5) + 0.8)
ax_aqi.set_ylabel("AQI (1-5)")
ax_aqi.set_title("Air Quality Index (Lower is Better)", fontsize=12)
ax_aqi.grid(axis="y", alpha=0.2, linestyle="--", linewidth=0.5)

# -----------------------------
# 3) Text “table” summary
# -----------------------------
ax_text.axis("off")
cell_text = []

for _, row in df.iterrows():
    line = (
        f"{row['Location']}:  "
        f"{row['Temp (°C)']:.1f}°C,  "
        f"Humidity {row['Humidity (%)']:.0f}%,  "
        f"Wind {row['Wind Speed (m/s)']:.1f} m/s,  "
        f"Clouds {row['Cloudiness (%)']:.0f}%,  "
        f"AQI {int(row['AQI (1-5)']) if row['AQI (1-5)'] == row['AQI (1-5)'] else 'N/A'}"
    )
    cell_text.append(line)

y_positions = np.linspace(0.9, 0.1, len(cell_text))
for y, line in zip(y_positions, cell_text):
    ax_text.text(
        0.01,
        y,
        line,
        fontsize=10,
        color="#e5e7eb",
        transform=ax_text.transAxes,
    )

ax_text.set_title("Quick City Summary", loc="left", fontsize=12, pad=5, color="white")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("weather_single_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()
