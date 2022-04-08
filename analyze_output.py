import pandas as pd
import geopandas as gpd
from shapely import wkt


df = pd.read_csv('output.csv', sep=';')
print(df.head())
df['pgeom'] = df['pgeom'].apply(wkt.loads)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('pgeom')
print(gdf.head())