import pandas as pd
import geopandas as gpd
from shapely import wkt


df = pd.read_csv('output.csv', sep=';')
df = df[0: -10]
df['geometry'] = df['mgeom'].apply(wkt.loads)
# df['geometry'] = df['mgeom'].map(wkt.loads)
line_string = []
for index, row in df.iterrows():
    line_string.append(df['geometry'].iloc[index])
    print(df['geometry'].iloc[index])
print(df.geometry.head())
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
# print(gdf.head())
# gs_ls = gpd.GeoSeries(pd.Series(line_string).apply(wkt.loads))