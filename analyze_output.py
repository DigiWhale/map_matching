import pandas as pd
import geopandas as gpd
from shapely import wkt


df = pd.read_csv('output.csv', sep=';')
df = df[0: -10]
df['geometry'] = df['mgeom']
# df['geometry'] = df['mgeom'].map(wkt.loads)
line_string = []
for index, row in df.iterrows():
  line = df['geometry'].iloc[index]
  if len(line) == 69:
    print(index)
    line_string.append(line.apply(wkt.loads))
    print(type(line))
    print(len(line))
# print(df.geometry.head())
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
# print(gdf.head())
# gs_ls = gpd.GeoSeries(pd.Series(line_string).apply(wkt.loads))