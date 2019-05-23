import os

class Style:

    styles = []
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def is_valid_style(style_string):
        return any([x for x in Style.styles if x.name == style_string])

    def data_path():
        return os.path.abspath(r'home-data\styles.txt')

with open(r'home-data\styles.txt', 'r') as stylesfile:
    styles = stylesfile.read().split('\n')
    for sty in styles:
        Style.styles.append(Style(sty))