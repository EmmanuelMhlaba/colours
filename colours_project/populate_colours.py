import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colours_project.settings')

import django

django.setup()

from colours.models import Palette, Colour

def populate():
    red_colours = [
        {'name':'Red Lighten-5', 'hex_code':'#ffebee', 'additional_info':''},
        {'name':'Red Lighten-4', 'hex_code':'#ffcdd2', 'additional_info':''},
        {'name':'Red Lighten-3', 'hex_code':'#ef9a9a', 'additional_info':''},
        {'name':'Red Lighten-2', 'hex_code':'#e57373', 'additional_info':''},
        {'name':'Red Lighten-1', 'hex_code':'#ef5350', 'additional_info':''},
        {'name':'Red', 'hex_code':'#44336', 'additional_info':''},
        {'name':'Red Darken-1', 'hex_code':'#e53935', 'additional_info':''},
        {'name':'Red Darken-2', 'hex_code':'#d32f2f', 'additional_info':''},
        {'name':'Red Darken-3', 'hex_code':'#c62828', 'additional_info':''},
        {'name':'Red Darken-4', 'hex_code':'#b71c1c', 'additional_info':''},
        {'name':'Red Accent-1', 'hex_code':'#ff8a80', 'additional_info':''},
        {'name':'Red Accent-2', 'hex_code':'#ff5252', 'additional_info':''},
        {'name':'Red Accent-3', 'hex_code':'#ff1744', 'additional_info':''},
        {'name':'Red Accent-4', 'hex_code':'#d50000', 'additional_info':''}
    ]

    pink_colours = [
        {'name':'Pink Lighten-5', 'hex_code':'#fce4ec', 'additional_info':''},
        {'name':'Pink Lighten-4', 'hex_code':'#f8bbd0', 'additional_info':''},
        {'name':'Pink Lighten-3', 'hex_code':'#f48fb1', 'additional_info':''},
        {'name':'Pink Lighten-2', 'hex_code':'#f06292', 'additional_info':''},
        {'name':'Pink Lighten-1', 'hex_code':'#ec407a', 'additional_info':''},
        {'name':'Pink', 'hex_code':'#e91e63', 'additional_info':''},
        {'name':'Pink Darken-1', 'hex_code':'#d81b60', 'additional_info':''},
        {'name':'Pink Darken-2', 'hex_code':'#c2185b', 'additional_info':''},
        {'name':'Pink Darken-3', 'hex_code':'#ad1457', 'additional_info':''},
        {'name':'Pink Darken-4', 'hex_code':'#880e4f', 'additional_info':''},
        {'name':'Pink Accent-1', 'hex_code':'#ff80ab', 'additional_info':''},
        {'name':'Pink Accent-2', 'hex_code':'#ff4081', 'additional_info':''},
        {'name':'Pink Accent-3', 'hex_code':'#f50057', 'additional_info':''},
        {'name':'Pink Accent-4', 'hex_code':'#c51162', 'additional_info':''}
    ]

    purple_colours = [
        {'name':'Purple Lighten-5', 'hex_code':'#f3e5f5', 'additional_info':''},
        {'name':'Purple Lighten-4', 'hex_code':'#e1bee7', 'additional_info':''},
        {'name':'Purple Lighten-3', 'hex_code':'#ce93d8', 'additional_info':''},
        {'name':'Purple Lighten-2', 'hex_code':'#ba68c8', 'additional_info':''},
        {'name':'Purple Lighten-1', 'hex_code':'#ab47bc', 'additional_info':''},
        {'name':'Purple', 'hex_code':'#9c27b0', 'additional_info':''},
        {'name':'Purple Darken-1', 'hex_code':'#8e24aa', 'additional_info':''},
        {'name':'Purple Darken-2', 'hex_code':'#7b1fa2', 'additional_info':''},
        {'name':'Purple Darken-3', 'hex_code':'#6a1b9a', 'additional_info':''},
        {'name':'Purple Darken-4', 'hex_code':'#4a148c', 'additional_info':''},
        {'name':'Purple Accent-1', 'hex_code':'#ea80fc', 'additional_info':''},
        {'name':'Purple Accent-2', 'hex_code':'#e040fb', 'additional_info':''},
        {'name':'Purple Accent-3', 'hex_code':'#d500f9', 'additional_info':''},
        {'name':'Purple Accent-4', 'hex_code':'#aa00ff', 'additional_info':''}
    ]

    deep_purple_colours = [
        {'name':'Deep Purple Lighten-5', 'hex_code':'#ede7f6', 'additional_info':''},
        {'name':'Deep Purple Lighten-4', 'hex_code':'#d1c4e9', 'additional_info':''},
        {'name':'Deep Purple Lighten-3', 'hex_code':'#b39ddb', 'additional_info':''},
        {'name':'Deep Purple Lighten-2', 'hex_code':'#9575cd', 'additional_info':''},
        {'name':'Deep Purple Lighten-1', 'hex_code':'#7e57c2', 'additional_info':''},
        {'name':'Deep Purple', 'hex_code':'#673ab7', 'additional_info':''},
        {'name':'Deep Purple Darken-1', 'hex_code':'#5e35b1', 'additional_info':''},
        {'name':'Deep Purple Darken-2', 'hex_code':'#512da8', 'additional_info':''},
        {'name':'Deep Purple Darken-3', 'hex_code':'#4527a0', 'additional_info':''},
        {'name':'Deep Purple Darken-4', 'hex_code':'#311b92', 'additional_info':''},
        {'name':'Deep Purple Accent-1', 'hex_code':'#b388ff', 'additional_info':''},
        {'name':'Deep Purple Accent-2', 'hex_code':'#7c4dff', 'additional_info':''},
        {'name':'Deep Purple Accent-3', 'hex_code':'#651fff', 'additional_info':''},
        {'name':'Deep Purple Accent-4', 'hex_code':'#6200ea', 'additional_info':''}
    ]

    indigo_colours = [
        {'name':'Indigo Lighten-5', 'hex_code':'#e8eaf6', 'additional_info':''},
        {'name':'Indigo Lighten-4', 'hex_code':'#c5cae9', 'additional_info':''},
        {'name':'Indigo Lighten-3', 'hex_code':'#9fa8da', 'additional_info':''},
        {'name':'Indigo Lighten-2', 'hex_code':'#7986cb', 'additional_info':''},
        {'name':'Indigo Lighten-1', 'hex_code':'#5c6bc0', 'additional_info':''},
        {'name':'Indigo', 'hex_code':'#3f51b5', 'additional_info':''},
        {'name':'Indigo Darken-1', 'hex_code':'#3949ab', 'additional_info':''},
        {'name':'Indigo Darken-2', 'hex_code':'#303f9f', 'additional_info':''},
        {'name':'Indigo Darken-3', 'hex_code':'#283593', 'additional_info':''},
        {'name':'Indigo Darken-4', 'hex_code':'#1a237e', 'additional_info':''},
        {'name':'Indigo Accent-1', 'hex_code':'#8c9eff', 'additional_info':''},
        {'name':'Indigo Accent-2', 'hex_code':'#536dfe', 'additional_info':''},
        {'name':'Indigo Accent-3', 'hex_code':'#3d5afe', 'additional_info':''},
        {'name':'Indigo Accent-4', 'hex_code':'#304ffe', 'additional_info':''}
    ]

    blue_colours = [
        {'name':'Blue Lighten-5', 'hex_code':'#e3f2fd', 'additional_info':''},
        {'name':'Blue Lighten-4', 'hex_code':'#bbdefb', 'additional_info':''},
        {'name':'Blue Lighten-3', 'hex_code':'#90caf9', 'additional_info':''},
        {'name':'Blue Lighten-2', 'hex_code':'#64b5f6', 'additional_info':''},
        {'name':'Blue Lighten-1', 'hex_code':'#42a5f5', 'additional_info':''},
        {'name':'Blue', 'hex_code':'#2196f3', 'additional_info':''},
        {'name':'Blue Darken-1', 'hex_code':'#1e88e5', 'additional_info':''},
        {'name':'Blue Darken-2', 'hex_code':'#1976d2', 'additional_info':''},
        {'name':'Blue Darken-3', 'hex_code':'#1565c0', 'additional_info':''},
        {'name':'Blue Darken-4', 'hex_code':'#0d47a1', 'additional_info':''},
        {'name':'Blue Accent-1', 'hex_code':'#82b1ff', 'additional_info':''},
        {'name':'Blue Accent-2', 'hex_code':'#448aff', 'additional_info':''},
        {'name':'Blue Accent-3', 'hex_code':'#2979ff', 'additional_info':''},
        {'name':'Blue Accent-4', 'hex_code':'#2962ff', 'additional_info':''}
    ]

    light_blue_colours = [
        {'name':'Light Blue Lighten-5', 'hex_code':'#e1f5fe', 'additional_info':''},
        {'name':'Light Blue Lighten-4', 'hex_code':'#b3e5fc', 'additional_info':''},
        {'name':'Light Blue Lighten-3', 'hex_code':'#81d4fa', 'additional_info':''},
        {'name':'Light Blue Lighten-2', 'hex_code':'#4fc3f7', 'additional_info':''},
        {'name':'Light Blue Lighten-1', 'hex_code':'#29b6f6', 'additional_info':''},
        {'name':'Light Blue', 'hex_code':'#03a9f4', 'additional_info':''},
        {'name':'Light Blue Darken-1', 'hex_code':'#039be5', 'additional_info':''},
        {'name':'Light Blue Darken-2', 'hex_code':'#0288d1', 'additional_info':''},
        {'name':'Light Blue Darken-3', 'hex_code':'#0277bd', 'additional_info':''},
        {'name':'Light Blue Darken-4', 'hex_code':'#01579b', 'additional_info':''},
        {'name':'Light Blue Accent-1', 'hex_code':'#80d8ff', 'additional_info':''},
        {'name':'Light Blue Accent-2', 'hex_code':'#40c4ff', 'additional_info':''},
        {'name':'Light Blue Accent-3', 'hex_code':'#00b0ff', 'additional_info':''},
        {'name':'Light Blue Accent-4', 'hex_code':'#0091ea', 'additional_info':''}
    ]

    palettes = {
        "Red": {"colours": red_colours},
        "Pink": {"colours": pink_colours},
        "Purple": {"colours": purple_colours},
        "Deep Purple": {"colours": deep_purple_colours},
        "Indigo": {"colours": indigo_colours},
        "Blue": {"colours": blue_colours},
        "Light Blue": {"colours": light_blue_colours}
    }

    for pal, pal_data in palettes.items():
        p = add_palette(pal)
        for c in pal_data["colours"]:
            add_colour(p, c["name"], c["hex_code"], c["additional_info"])
    
    for p in Palette.objects.all():
        for c in Colour.objects.filter(palette=p):
            print("- {0} - {1}".format(str(p), str(c)))

def add_colour(palette, name, hex_code, additional_info):
    c = Colour.objects.get_or_create(
        palette=palette,
        name=name,
        hex_code=hex_code,
        additional_info=additional_info
    )[0]
    c.save()
    return c

def add_palette(name):
    p = Palette.objects.get_or_create(name=name)[0]
    p.save()
    return p

if __name__ == "__main__":
    print("Starting Colours population script...")
    populate()
