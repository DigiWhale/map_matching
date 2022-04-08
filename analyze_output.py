import pandas as pd
import geopandas as gpd

df = pd.read_csv('output.csv', sep=';')
print(df.head())
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('pgeom')
print(gdf.head())