import pandas as pd
import geopandas as gpd
from shapely import wkt
import traceback

def wkt_loads(x):
    try:
        return wkt.loads(x)
    except Exception:
        return None


df = pd.read_csv('output.csv', sep=';')
# df = df[0: -10]
# df['geometry'] = df['mgeom']
# try:
df['geometry'] = df['mgeom'].apply(wkt_loads)
# except:
#   print('Error:', traceback.format_exc())
# line_string = []
# for index, row in df.iterrows():
#   line = df['geometry'].iloc[index]
#   print(line)
#   # if len(line) == 69:
  #   print(index)
  #   line_string.append(df['geometry'][index].apply(wkt.loads))
  #   print(type(line))
  #   print(len(line))
# print(df.geometry.head())
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
# print(gdf.head())
# gs_ls = gpd.GeoSeries(pd.Series(line_string).apply(wkt.loads))