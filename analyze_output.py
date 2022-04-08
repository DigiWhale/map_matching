import pandas as pd
import geopandas as gpd
from shapely import wkt


df = pd.read_csv('output.csv', sep=';')
df['geometry'] = df['pgeom']
# df['geometry'] = df['pgeom'].map(wkt.loads)
for index, row in df.iterrows():
    print(row['geometry'].iloc[index])
print(df.geometry.head())
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
print(gdf.head())