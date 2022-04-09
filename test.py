import pandas as pd
import geopandas as gpd
from shapely import wkt, ops, geometry
import folium
from shapely.geometry import Point, Polygon

def wkt_loads(x):
    try:
        return wkt.loads(x)
    except Exception:
        return None
      
def create_polygon(coords, polygon_name):
  ''' Create a polygon from coordinates '''
  polygon = Polygon(coords)
  gdf = gpd.GeoDataFrame(crs = {'init' :'epsg:4326'})
  gdf.loc[0,'name'] = polygon_name
  gdf.loc[0, 'geometry'] = polygon
  return gdf


df = pd.read_csv('output.csv', sep=';')
pdf = df
# df = df[0: -10]
# df['geometry'] = df['mgeom']
# try:
df['geometry'] = df['mgeom'].apply(wkt_loads)
# df['points'] = df['pgeom'].apply(wkt_loads)
# except:
#   print('Error:', traceback.format_exc())
line_string = []
drop = []
for index, row in df.iterrows():
  if df['geometry'].iloc[index] != None:
    # print(df['geometry'].iloc[index], type(df['geometry'].iloc[index]))
    line_string.append(df['geometry'].iloc[index])
  else:
    drop.append(index)
# for index, row in df.iterrows():
#   print(df['points'].iloc[index], type(df['points'].iloc[index]))
    # df=df.drop(df.index[index])
multi_line = geometry.MultiLineString(line_string)
print(multi_line)
# for index in drop:
#   df=df.drop(df.index[index])
df = df.drop(df.index[drop])
# df['geometry'] = line_string
#   print(line)
#   # if len(line) == 69:
  #   print(index)
  #   line_string.append(df['geometry'][index].apply(wkt.loads))
  #   print(type(line))
  #   print(len(line))
# print(df.geometry.head())
# shapefile = create_polygon(coordinates, “Amesterdam”)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs).set_geometry('geometry')
# print(gdf['geometry'])
gdf.to_file('output.shp', driver='ESRI Shapefile')
map = gdf.explore()
map.add_child(multi_line.plot(color='red', alpha=0.5))
html_string = map.get_root().render()
#write html to file
output_file = open("map.html","w+")
output_file.write(html_string)
output_file.close()
# print(gdf.head())
# gs_ls = gpd.GeoSeries(pd.Series(line_string).apply(wkt.loads))