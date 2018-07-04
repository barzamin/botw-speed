import click
import json
from pprint import pprint
import matplotlib.pyplot as plt

plt.xkcd()

with open('./landmarks.json') as f:
    landmarks = json.load(f)

with open('./regions.json') as f:
    regions = json.load(f)

landmark_pts = [l['geometry']['coordinates'] for l in landmarks]

plt.scatter(*zip(*landmark_pts))
for region in regions:
    pos = region['geometry']['coordinates']
    text = region['properties']['name']
    plt.text(*pos, text, ha='center')

plt.show()
