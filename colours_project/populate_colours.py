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

    cyan_colours = [
        {'name':'Cyan Lighten-5', 'hex_code':'#e0f7fa', 'additional_info':''},
        {'name':'Cyan Lighten-4', 'hex_code':'#b2ebf2', 'additional_info':''},
        {'name':'Cyan Lighten-3', 'hex_code':'#80deea', 'additional_info':''},
        {'name':'Cyan Lighten-2', 'hex_code':'#4dd0e1', 'additional_info':''},
        {'name':'Cyan Lighten-1', 'hex_code':'#26c6da', 'additional_info':''},
        {'name':'Cyan', 'hex_code':'#00bcd4', 'additional_info':''},
        {'name':'Cyan Darken-1', 'hex_code':'#00acc1', 'additional_info':''},
        {'name':'Cyan Darken-2', 'hex_code':'#0097a7', 'additional_info':''},
        {'name':'Cyan Darken-3', 'hex_code':'#00838f', 'additional_info':''},
        {'name':'Cyan Darken-4', 'hex_code':'#006064', 'additional_info':''},
        {'name':'Cyan Accent-1', 'hex_code':'#84ffff', 'additional_info':''},
        {'name':'Cyan Accent-2', 'hex_code':'#18ffff', 'additional_info':''},
        {'name':'Cyan Accent-3', 'hex_code':'#00e5ff', 'additional_info':''},
        {'name':'Cyan Accent-4', 'hex_code':'#00b8d4', 'additional_info':''}
    ]

    teal_colours = [
        {'name':'Teal Lighten-5', 'hex_code':'#e0f2f1', 'additional_info':''},
        {'name':'Teal Lighten-4', 'hex_code':'#b2dfdb', 'additional_info':''},
        {'name':'Teal Lighten-3', 'hex_code':'#80cbc4', 'additional_info':''},
        {'name':'Teal Lighten-2', 'hex_code':'#4db6ac', 'additional_info':''},
        {'name':'Teal Lighten-1', 'hex_code':'#26a69a', 'additional_info':''},
        {'name':'Teal', 'hex_code':'#009688', 'additional_info':''},
        {'name':'Teal Darken-1', 'hex_code':'#00897b', 'additional_info':''},
        {'name':'Teal Darken-2', 'hex_code':'#00796b', 'additional_info':''},
        {'name':'Teal Darken-3', 'hex_code':'#00695c', 'additional_info':''},
        {'name':'Teal Darken-4', 'hex_code':'#004d40', 'additional_info':''},
        {'name':'Teal Accent-1', 'hex_code':'#a7ffeb', 'additional_info':''},
        {'name':'Teal Accent-2', 'hex_code':'#64ffda', 'additional_info':''},
        {'name':'Teal Accent-3', 'hex_code':'#1de9b6', 'additional_info':''},
        {'name':'Teal Accent-4', 'hex_code':'#00bfa5', 'additional_info':''}
    ]

    green_colours = [
        {'name':'Green Lighten-5', 'hex_code':'#e8f5e9', 'additional_info':''},
        {'name':'Green Lighten-4', 'hex_code':'#c8e6c9', 'additional_info':''},
        {'name':'Green Lighten-3', 'hex_code':'#a5d6a7', 'additional_info':''},
        {'name':'Green Lighten-2', 'hex_code':'#81c784', 'additional_info':''},
        {'name':'Green Lighten-1', 'hex_code':'#66bb6a', 'additional_info':''},
        {'name':'Green', 'hex_code':'#4caf50', 'additional_info':''},
        {'name':'Green Darken-1', 'hex_code':'#43a047', 'additional_info':''},
        {'name':'Green Darken-2', 'hex_code':'#388e3c', 'additional_info':''},
        {'name':'Green Darken-3', 'hex_code':'#2e7d32', 'additional_info':''},
        {'name':'Green Darken-4', 'hex_code':'#1b5e20', 'additional_info':''},
        {'name':'Green Accent-1', 'hex_code':'#b9f6ca', 'additional_info':''},
        {'name':'Green Accent-2', 'hex_code':'#69f0ae', 'additional_info':''},
        {'name':'Green Accent-3', 'hex_code':'#00e676', 'additional_info':''},
        {'name':'Green Accent-4', 'hex_code':'#00c853', 'additional_info':''}
    ]

    light_green_colours = [
        {'name':'Light Green Lighten-5', 'hex_code':'#f1f8e9', 'additional_info':''},
        {'name':'Light Green Lighten-4', 'hex_code':'#dcedc8', 'additional_info':''},
        {'name':'Light Green Lighten-3', 'hex_code':'#c5e1a5', 'additional_info':''},
        {'name':'Light Green Lighten-2', 'hex_code':'#aed581', 'additional_info':''},
        {'name':'Light Green Lighten-1', 'hex_code':'#9ccc65', 'additional_info':''},
        {'name':'Light Green', 'hex_code':'#8bc34a', 'additional_info':''},
        {'name':'Light Green Darken-1', 'hex_code':'#7cb342', 'additional_info':''},
        {'name':'Light Green Darken-2', 'hex_code':'#689f38', 'additional_info':''},
        {'name':'Light Green Darken-3', 'hex_code':'#558b2f', 'additional_info':''},
        {'name':'Light Green Darken-4', 'hex_code':'#33691e', 'additional_info':''},
        {'name':'Light Green Accent-1', 'hex_code':'#ccff90', 'additional_info':''},
        {'name':'Light Green Accent-2', 'hex_code':'#b2ff59', 'additional_info':''},
        {'name':'Light Green Accent-3', 'hex_code':'#76ff03', 'additional_info':''},
        {'name':'Light Green Accent-4', 'hex_code':'#64dd17', 'additional_info':''}
    ]

    lime_colours = [
        {'name':'Lime Lighten-5', 'hex_code':'#f9fbe7', 'additional_info':''},
        {'name':'Lime Lighten-4', 'hex_code':'#f0f4c3', 'additional_info':''},
        {'name':'Lime Lighten-3', 'hex_code':'#e6ee9c', 'additional_info':''},
        {'name':'Lime Lighten-2', 'hex_code':'#dce775', 'additional_info':''},
        {'name':'Lime Lighten-1', 'hex_code':'#d4e157', 'additional_info':''},
        {'name':'Lime', 'hex_code':'#cddc39', 'additional_info':''},
        {'name':'Lime Darken-1', 'hex_code':'#c0ca33', 'additional_info':''},
        {'name':'Lime Darken-2', 'hex_code':'#afb42b', 'additional_info':''},
        {'name':'Lime Darken-3', 'hex_code':'#9e9d24', 'additional_info':''},
        {'name':'Lime Darken-4', 'hex_code':'#827717', 'additional_info':''},
        {'name':'Lime Accent-1', 'hex_code':'#f4ff81', 'additional_info':''},
        {'name':'Lime Accent-2', 'hex_code':'#eeff41', 'additional_info':''},
        {'name':'Lime Accent-3', 'hex_code':'#c6ff00', 'additional_info':''},
        {'name':'Lime Accent-4', 'hex_code':'#aeea00', 'additional_info':''}
    ]

    yellow_colours = [
        {'name':'Yellow Lighten-5', 'hex_code':'#fffde7', 'additional_info':''},
        {'name':'Yellow Lighten-4', 'hex_code':'#fff9c4', 'additional_info':''},
        {'name':'Yellow Lighten-3', 'hex_code':'#fff59d', 'additional_info':''},
        {'name':'Yellow Lighten-2', 'hex_code':'#fff176', 'additional_info':''},
        {'name':'Yellow Lighten-1', 'hex_code':'#ffee58', 'additional_info':''},
        {'name':'Yellow', 'hex_code':'#ffeb3b', 'additional_info':''},
        {'name':'Yellow Darken-1', 'hex_code':'#fdd835', 'additional_info':''},
        {'name':'Yellow Darken-2', 'hex_code':'#fbc02d', 'additional_info':''},
        {'name':'Yellow Darken-3', 'hex_code':'#f9a825', 'additional_info':''},
        {'name':'Yellow Darken-4', 'hex_code':'#f57f17', 'additional_info':''},
        {'name':'Yellow Accent-1', 'hex_code':'#ffff8d', 'additional_info':''},
        {'name':'Yellow Accent-2', 'hex_code':'#ffff00', 'additional_info':''},
        {'name':'Yellow Accent-3', 'hex_code':'#ffea00', 'additional_info':''},
        {'name':'Yellow Accent-4', 'hex_code':'#ffd600', 'additional_info':''}
    ]

    amber_colours = [
        {'name':'Amber Lighten-5', 'hex_code':'#fff8e1', 'additional_info':''},
        {'name':'Amber Lighten-4', 'hex_code':'#ffecb3', 'additional_info':''},
        {'name':'Amber Lighten-3', 'hex_code':'#ffe082', 'additional_info':''},
        {'name':'Amber Lighten-2', 'hex_code':'#ffd54f', 'additional_info':''},
        {'name':'Amber Lighten-1', 'hex_code':'#ffca28', 'additional_info':''},
        {'name':'Amber', 'hex_code':'#ffc107', 'additional_info':''},
        {'name':'Amber Darken-1', 'hex_code':'#ffb300', 'additional_info':''},
        {'name':'Amber Darken-2', 'hex_code':'#ffa000', 'additional_info':''},
        {'name':'Amber Darken-3', 'hex_code':'#ff8f00', 'additional_info':''},
        {'name':'Amber Darken-4', 'hex_code':'#ff6f00', 'additional_info':''},
        {'name':'Amber Accent-1', 'hex_code':'#ffe57f', 'additional_info':''},
        {'name':'Amber Accent-2', 'hex_code':'#ffd740', 'additional_info':''},
        {'name':'Amber Accent-3', 'hex_code':'#ffc400', 'additional_info':''},
        {'name':'Amber Accent-4', 'hex_code':'#ffab00', 'additional_info':''}
    ]

    orange_colours = [
        {'name':'Orange Lighten-5', 'hex_code':'#fff3e0', 'additional_info':''},
        {'name':'Orange Lighten-4', 'hex_code':'#ffe0b2', 'additional_info':''},
        {'name':'Orange Lighten-3', 'hex_code':'#ffcc80', 'additional_info':''},
        {'name':'Orange Lighten-2', 'hex_code':'#ffb74d', 'additional_info':''},
        {'name':'Orange Lighten-1', 'hex_code':'#ffa726', 'additional_info':''},
        {'name':'Orange', 'hex_code':'#ff9800', 'additional_info':''},
        {'name':'Orange Darken-1', 'hex_code':'#fb8c00', 'additional_info':''},
        {'name':'Orange Darken-2', 'hex_code':'#f57c00', 'additional_info':''},
        {'name':'Orange Darken-3', 'hex_code':'#ef6c00', 'additional_info':''},
        {'name':'Orange Darken-4', 'hex_code':'#e65100', 'additional_info':''},
        {'name':'Orange Accent-1', 'hex_code':'#ffd180', 'additional_info':''},
        {'name':'Orange Accent-2', 'hex_code':'#ffab40', 'additional_info':''},
        {'name':'Orange Accent-3', 'hex_code':'#ff9100', 'additional_info':''},
        {'name':'Orange Accent-4', 'hex_code':'#ff6d00', 'additional_info':''}
    ]

    deep_orange_colours = [
        {'name':'Deep Orange Lighten-5', 'hex_code':'#fbe9e7', 'additional_info':''},
        {'name':'Deep Orange Lighten-4', 'hex_code':'#ffccbc', 'additional_info':''},
        {'name':'Deep Orange Lighten-3', 'hex_code':'#ffab91', 'additional_info':''},
        {'name':'Deep Orange Lighten-2', 'hex_code':'#ff8a65', 'additional_info':''},
        {'name':'Deep Orange Lighten-1', 'hex_code':'#ff7043', 'additional_info':''},
        {'name':'Deep Orange', 'hex_code':'#ff5722', 'additional_info':''},
        {'name':'Deep Orange Darken-1', 'hex_code':'#f4511e', 'additional_info':''},
        {'name':'Deep Orange Darken-2', 'hex_code':'#e64a19', 'additional_info':''},
        {'name':'Deep Orange Darken-3', 'hex_code':'#d84315', 'additional_info':''},
        {'name':'Deep Orange Darken-4', 'hex_code':'#bf360c', 'additional_info':''},
        {'name':'Deep Orange Accent-1', 'hex_code':'#ff9e80', 'additional_info':''},
        {'name':'Deep Orange Accent-2', 'hex_code':'#ff6e40', 'additional_info':''},
        {'name':'Deep Orange Accent-3', 'hex_code':'#ff3d00', 'additional_info':''},
        {'name':'Deep Orange Accent-4', 'hex_code':'#dd2c00', 'additional_info':''}
    ]

    brown_colours = [
        {'name':'Brown Lighten-5', 'hex_code':'#efebe9', 'additional_info':''},
        {'name':'Brown Lighten-4', 'hex_code':'#d7ccc8', 'additional_info':''},
        {'name':'Brown Lighten-3', 'hex_code':'#bcaaa4', 'additional_info':''},
        {'name':'Brown Lighten-2', 'hex_code':'#a1887f', 'additional_info':''},
        {'name':'Brown Lighten-1', 'hex_code':'#8d6e63', 'additional_info':''},
        {'name':'Brown', 'hex_code':'#795548', 'additional_info':''},
        {'name':'Brown Darken-1', 'hex_code':'#6d4c41', 'additional_info':''},
        {'name':'Brown Darken-2', 'hex_code':'#5d4037', 'additional_info':''},
        {'name':'Brown Darken-3', 'hex_code':'#4e342e', 'additional_info':''},
        {'name':'Brown Darken-4', 'hex_code':'#3e2723', 'additional_info':''}
    ]

    grey_colours = [
        {'name':'Grey Lighten-5', 'hex_code':'#fafafa', 'additional_info':''},
        {'name':'Grey Lighten-4', 'hex_code':'#f5f5f5', 'additional_info':''},
        {'name':'Grey Lighten-3', 'hex_code':'#eeeeee', 'additional_info':''},
        {'name':'Grey Lighten-2', 'hex_code':'#e0e0e0', 'additional_info':''},
        {'name':'Grey Lighten-1', 'hex_code':'#bdbdbd', 'additional_info':''},
        {'name':'Grey', 'hex_code':'#9e9e9e', 'additional_info':''},
        {'name':'Grey Darken-1', 'hex_code':'#757575', 'additional_info':''},
        {'name':'Grey Darken-2', 'hex_code':'#616161', 'additional_info':''},
        {'name':'Grey Darken-3', 'hex_code':'#424242', 'additional_info':''},
        {'name':'Grey Darken-4', 'hex_code':'#212121', 'additional_info':''}
    ]

    blue_grey_colours = [
        {'name':'Blue Grey Lighten-5', 'hex_code':'#eceff1', 'additional_info':''},
        {'name':'Blue Grey Lighten-4', 'hex_code':'#cfd8dc', 'additional_info':''},
        {'name':'Blue Grey Lighten-3', 'hex_code':'#b0bec5', 'additional_info':''},
        {'name':'Blue Grey Lighten-2', 'hex_code':'#90a4ae', 'additional_info':''},
        {'name':'Blue Grey Lighten-1', 'hex_code':'#78909c', 'additional_info':''},
        {'name':'Blue Grey', 'hex_code':'#607d8b', 'additional_info':''},
        {'name':'Blue Grey Darken-1', 'hex_code':'#546e7a', 'additional_info':''},
        {'name':'Blue Grey Darken-2', 'hex_code':'#455a64', 'additional_info':''},
        {'name':'Blue Grey Darken-3', 'hex_code':'#37474f', 'additional_info':''},
        {'name':'Blue Grey Darken-4', 'hex_code':'#263238', 'additional_info':''}
    ]

    white_colours = [
        {'name':'White', 'hex_code':'#ffffff', 'additional_info':''}
    ]

    black_colours = [
        {'name':'Black', 'hex_code':'#000000', 'additional_info':''}
    ]

    palettes = {
        "Red": {"colours": red_colours},
        "Pink": {"colours": pink_colours},
        "Purple": {"colours": purple_colours},
        "Deep Purple": {"colours": deep_purple_colours},
        "Indigo": {"colours": indigo_colours},
        "Blue": {"colours": blue_colours},
        "Light Blue": {"colours": light_blue_colours},
        "Cyan": {"colours": cyan_colours},
        "Teal": {"colours": teal_colours},
        "Green": {"colours": green_colours},
        "Light Green": {"colours": light_green_colours},
        "Lime": {"colours": lime_colours},
        "Yellow": {"colours": yellow_colours},
        "Amber": {"colours": amber_colours},
        "Orange": {"colours": orange_colours},
        "Deep Orange": {"colours": deep_orange_colours},
        "Brown": {"colours": brown_colours},
        "Grey": {"colours": grey_colours},
        "Blue Grey": {"colours": blue_grey_colours},
        "White": {"colours": white_colours},
        "Black": {"colours": black_colours}
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
