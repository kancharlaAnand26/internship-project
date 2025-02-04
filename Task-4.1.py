import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap


df = pd.read_csv(r"C:\Users\YAMINI K\OneDrive\Desktop\anand\compressed_data (1).csv")


df = df.rename(columns={
    "Accident Date": "Date",
    "Weather_Conditions": "Weather",
    "Road_Surface_Conditions": "Road_Condition",
    "Latitude": "Latitude",
    "Longitude": "Longitude",
    "Accident_Severity": "Severity"
})


df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)


df = df.dropna(subset=['Date', 'Weather', 'Road_Condition', 'Latitude', 'Longitude', 'Severity'])


df['Hour'] = df['Date'].dt.hour.fillna(0).astype(int)  # Default to 0 if time is missing


plt.figure(figsize=(10, 6))
sns.countplot(x=df['Hour'], hue=df['Hour'], palette='viridis', legend=False)
plt.title('Accidents by Time of Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.xticks(range(0, 24))
plt.show()


top_weather = df['Weather'].value_counts().nlargest(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_weather.index, y=top_weather.values, palette='magma')
plt.title('Top 10 Weather Conditions Leading to Accidents')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()


map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
accident_map = folium.Map(location=map_center, zoom_start=10)


heat_data = df[['Latitude', 'Longitude']].values.tolist()

HeatMap(heat_data, radius=10).add_to(accident_map)


output_map = "accident_hotspots.html"
accident_map.save(output_map)

print(f"Heatmap saved as '{output_map}' - Open this file in a web browser to view the map.")


