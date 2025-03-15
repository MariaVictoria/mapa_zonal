import os
import folium

# Coordenadas de la zona
latitud = -32.5
longitud = -64.5

# Crear el mapa
m = folium.Map(location=[latitud, longitud], zoom_start=12)

# Agregar marcadores
folium.Marker([-32.5333, -64.5167], popup='Río 3°').add_to(m)
folium.Marker([-32.55, -64.5], popup='Santa Rosa de Calamuchita').add_to(m)
folium.Marker([-32.58, -64.4833], popup='Villa Gral. Belgrano').add_to(m)
folium.Marker([-32.6, -64.4667], popup='San Agustín').add_to(m)
folium.Marker([-32.6167, -64.45], popup='Embalse Alma Fuerte').add_to(m)

# Agregar polígono para delimitar la zona
#folium.Polygon([[-32.5, -64.5], [-32.6, -64.5], [-32.6, -64.4], [-32.5, -64.4], [-32.5, -64.5]],
               #color='blue', fill_color='blue', fill_opacity=0.2).add_to(m)

# Guardar el mapa en la misma carpeta que el script
script_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_path, 'zona_25_zonq_25.html')
m.save(output_path)