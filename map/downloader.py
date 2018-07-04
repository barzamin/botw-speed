import click
import json
from pprint import pprint
import requests

API_BASE = 'https://www.zeldadungeon.net/wiki/api.php?\
format=json&action=parse&page=Zelda_Dungeon:Breath_of_the_Wild_Map/'


@click.command()
@click.argument('obj')
def cli(obj):
    r = requests.get(API_BASE + obj)

    raw = r.json()['parse']['properties'][0]['*']
    raw_json = '[' + raw[:-1] + ']'

    data = json.loads(raw_json)
    json.dump(data, click.get_text_stream('stdout'),
    		  indent=2)

if __name__ == '__main__':
    cli()
