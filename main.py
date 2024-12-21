import tkinter as tk
import json
from PIL import Image, ImageTk
import random
import pyglet
from pygame import mixer
from tkinter import messagebox, PhotoImage

#pyglet.font.add_file('league-spartan.bold.ttf')
pyglet.font.add_file(r'C:\Users\IDEAPAD\Desktop\ColorMatch\league-spartan.bold.ttf')
pyglet.font.add_file(r'C:\Users\IDEAPAD\Desktop\ColorMatch\GlacialIndifference-Regular.otf')
#pyglet.font.add_file('')

class Levels(tk.Frame):

    def check_level(self, levels):
        list_levels = [
            [ # Level 1
                ["#feeb85", "#feeb85", "#feeb85"],
                ["#eddf74", "#eddf74", "#eddf74"],
                ["#dbd467", "#dbd467", "#dbd467"],
                ["#cbc958", "#cbc958", "#cbc958"],
                ["#bbbe49", "#bbbe49", "#bbbe49"],
                ["#abb33c", "#abb33c", "#abb33c"],
                ["#9da72d", "#9da72d", "#9da72d"]
            ],
            [ # Level 2
                ["#f0bf61", "#c4b073", "#93a082", "#659390", "#3883a1"],
                ["#edb264", "#c49f70", "#98907b", "#6d7e86", "#436f94"],
                ["#f1a26a", "#c79071", "#9f7c76", "#746b7e", "#4e5b86"],
                ["#f1956e", "#ca8170", "#a46d73", "#7d5973", "#564677"],
                ["#f08670", "#cc7271", "#a95c6e", "#84466b", "#62306b"],
                ["#f07a76", "#ce626f", "#ae4967", "#8c3361", "#6b1a5c"],
                ["#f26c7b", "#d35270", "#b23763", "#942158", "#76084f"]
            ],
            [ # Level 3
                ["#f0d174", "#e5cf79", "#dbcd82", "#cfcc87", "#c5ca8f", "#bbc797", "#b1c7a0"],
                ["#ebba6d", "#e1b974", "#d4bb7b", "#c9bc85", "#bebb8e", "#b1bd97", "#a7bea0"],
                ["#e9a164", "#dca56d", "#cea877", "#c2ad82", "#b7ae8b", "#aab398", "#9db6a1"],
                ["#e48c5e", "#d99169", "#c89673", "#bb9c80", "#ada189", "#a1a697", "#95aca2"],
                ["#e07656", "#d37d62", "#c68370", "#b68c7c", "#a7938a", "#979c96", "#89a2a4"],
                ["#dd5e4f", "#cc685c", "#bd726c", "#af7c7b", "#9f8689", "#919096", "#829aa6"],
                ["#d94949", "#c75457", "#b76268", "#a86c78", "#987788", "#878497", "#7890a8"]
            ],
            [ #Level 4
                ["#e9e8d6", "#eacabf", "#eeaba3", "#ed8e8c", "#ed6f72", "#ef515d"],
                ["#ceddd6", "#cebfbc", "#cda5a4", "#cd888b", "#cf6b75", "#ce4e5b"],
                ["#b1d3d5", "#b1b8c0", "#b19da6", "#b0828c", "#b06675", "#ae4c59"],
                ["#97c8d7", "#94b0be", "#9495a7", "#927d8c", "#8f6374", "#8f4a5c"],
                ["#7ac0d7", "#78a8bf", "#758fa6", "#74768d", "#705e74", "#71475b"],
                ["#5db7d9", "#5a9fbf", "#5788a6", "#56718e", "#545b75", "#4e445c"],
                ["#41addb", "#3f96bf", "#3c82a6", "#366e8f", "#325774", "#30415b"],
                ["#28a3dc", "#238fbe", "#1e7aa9", "#17678c", "#125275", "#0d405d"],
            ],
            [
                #Level 5
                ["#d9eaf2", "#cce7ec", "#c1e5e5", "#b5e2df", "#a7dfda", "#9bdcd6", "#90dacf"],
                ["#e0dedf", "#d1dbdc", "#c2d6d7", "#b2d4d3", "#a4cfcd", "#95cbc9", "#87c9c5"],
                ["#e4d1cb", "#d2cdc7", "#c3c9c7", "#b1c5c6", "#9fc1c0", "#8dbdbd", "#7cb9ba"],
                ["#ecc4bb", "#d6bfb9", "#c4bbb6", "#afb7b7", "#9ab2b4", "#84aeb2", "#70a9b0"],
                ["#f2b7a9", "#dbb3aa", "#c2ada6", "#ada7a7", "#97a1a8", "#7da0a8", "#699ba6"],
                ["#f8aa96", "#dfa398", "#c59f9a", "#ac9a98", "#939499", "#778e9c", "#5d8a9d"],
                ["#ff9d84", "#e29687", "#c6918b", "#a98b8b", "#8e848d", "#6f7f8e", "#557a94"],
            ],
            [
                #Level 6
                ["#4b4aca", "#5545c9", "#633fc5", "#6c38bf", "#7a31be", "#852cba", "#8f28b7"],
                ["#685bb3", "#7151b2", "#794ab2", "#8340b1", "#8a36ae", "#932fac", "#9b26a9"],
                ["#826e9f", "#8a63a2", "#91589f", "#954ba0", "#9c3da1", "#a2319d", "#a8279e"],
                ["#a5818d", "#a6718d", "#a7628e", "#aa5590", "#ac4692", "#b03590", "#b52594"],
                ["#c29576", "#c1827b", "#c0707d", "#bf5b7d", "#c04b82", "#bd3983", "#c02688"],
                ["#dea762", "#da9164", "#d77c6a", "#d6646e", "#d05172", "#cd3b79", "#ca267c"],
                ["#fdbb4d", "#f6a051", "#f08858", "#e9705f", "#e35764", "#db3e69", "#d7256f"],
            ],
            [
                #Level 7
                ["#fae7a2", "#e5e4a2", "#d2e1a6", "#c0e1aa", "#ace1ab", "#99deaf", "#86ddb2"],
                ["#e2c790", "#d7c794", "#c9c997", "#bcc99b", "#aec99e", "#a1ca9e", "#94cba4"],
                ["#cea77e", "#c6aa82", "#c0ae86", "#b9b18b", "#b2b48f", "#acb894", "#a6ba97"],
                ["#ba886d", "#b78e72", "#b89376", "#b6987c", "#b79e80", "#b5a584", "#b6a989"],
                ["#a3695e", "#aa7062", "#b07867", "#b4806b", "#ba8772", "#c09177", "#c5997c"],
                ["#8f4a4d", "#99544f", "#a55e58", "#b3695e", "#bf7363", "#c97c68", "#d58770"],
                ["#7b2a3b", "#8c3440", "#9e4348", "#b14f4e", "#c05c52", "#d16a59", "#e57760"],
            ],
            [
                #Level 8
                ["#f4f3bd", "#f3dbab", "#f1c49a", "#f2ae89", "#ef987a", "#ec806b", "#ee6a5b"],
                ["#e1e4b7", "#ded0ab", "#dbbd9b", "#d8a98f", "#d39580", "#d08075", "#cd6c66"],
                ["#ced8b5", "#c8c7a8", "#c4b49b", "#bda193", "#b88f89", "#b27e80", "#ae6d75"],
                ["#becbaf", "#b5bda8", "#acad9f", "#a69d98", "#9d8d90", "#977d89", "#8e6e83"],
                ["#a9beab", "#9fb1a5", "#98a4a2", "#8d989e", "#808a99", "#767c94", "#6e6f8e"],
                ["#96b2a4", "#8aa7a3", "#809ba2", "#7491a3", "#6786a2", "#5a7b9e", "#4e709d"],
                ["#85a79f", "#779ca2", "#6795a3", "#588ba6", "#4c82a8", "#3c7aa9", "#2f71ab"]
            ]
        ]
        return list_levels[levels]

    def select_level(self, level):
        level_select = [
            [  # Level 1
                [{"movable": 0, "color": "#feeb85"}, {"movable": 0, "color": "#feeb85"}, {"movable": 0, "color": "#feeb85"}],
                [{"movable": 0, "color": "#eddf74"}, {"movable": 1, "color": "#dbd467"}, {"movable": 0, "color": "#eddf74"}],
                [{"movable": 0, "color": "#dbd467"}, {"movable": 1, "color": "#abb33c"}, {"movable": 0, "color": "#dbd467"}],
                [{"movable": 0, "color": "#cbc958"}, {"movable": 1, "color": "#eddf74"}, {"movable": 0, "color": "#cbc958"}],
                [{"movable": 0, "color": "#bbbe49"}, {"movable": 1, "color": "#bbbe49"}, {"movable": 0, "color": "#bbbe49"}],
                [{"movable": 0, "color": "#abb33c"}, {"movable": 1, "color": "#cbc958"}, {"movable": 0, "color": "#abb33c"}],
                [{"movable": 0, "color": "#9da72d"}, {"movable": 0, "color": "#9da72d"}, {"movable": 0, "color": "#9da72d"}]
            ], #level 2
            [
                 [{'movable': 0, 'color': '#f0bf61'}, {'movable': 1, 'color': '#edb264'}, {'movable': 1, 'color': '#f07a76'}, {'movable': 1, 'color': '#4e5b86'}, {'movable': 0, 'color': '#3883a1'}],
                 [{'movable': 1, 'color': '#62306b'}, {'movable': 0, 'color': '#c49f70'}, {'movable': 0, 'color': '#98907b'}, {'movable': 0, 'color': '#6d7e86'}, {'movable': 1, 'color': '#c4b073'}],
                 [{'movable': 1, 'color': '#564677'}, {'movable': 0, 'color': '#c79071'}, {'movable': 0, 'color': '#9f7c76'}, {'movable': 0, 'color': '#746b7e'}, {'movable': 1, 'color': '#436f94'}],
                 [{'movable': 1, 'color': '#d35270'}, {'movable': 0, 'color': '#ca8170'}, {'movable': 0, 'color': '#a46d73'}, {'movable': 0, 'color': '#7d5973'}, {'movable': 1, 'color': '#f1956e'}],
                 [{'movable': 1, 'color': '#93a082'}, {'movable': 0, 'color': '#cc7271'}, {'movable': 0, 'color': '#a95c6e'}, {'movable': 0, 'color': '#84466b'}, {'movable': 1, 'color': '#f08670'}],
                 [{'movable': 1, 'color': '#6b1a5c'}, {'movable': 0, 'color': '#ce626f'}, {'movable': 0, 'color': '#ae4967'}, {'movable': 0, 'color': '#8c3361'}, {'movable': 1, 'color': '#f1a26a'}],
                 [{'movable': 0, 'color': '#f26c7b'}, {'movable': 1, 'color': '#659390'}, {'movable': 1, 'color': '#942158'}, {'movable': 1, 'color': '#b23763'}, {'movable': 0, 'color': '#76084f'}]
            ],
            [ #Level 3
                 [{'movable': 0, 'color': '#f0d174'},{'movable': 0, 'color': '#e5cf79'},{'movable': 0, 'color': '#dbcd82'}, {'movable': 0, 'color': '#cfcc87'},{'movable': 0, 'color': '#c5ca8f'},{'movable': 0, 'color': '#bbc797'},{'movable': 0, 'color': '#b1c7a0'}],
                 [{'movable': 0, 'color': '#ebba6d'},{'movable': 1, 'color': '#d4bb7b'},{'movable': 1, 'color': '#979c96'},{'movable': 0, 'color': '#c9bc85'},{'movable': 1, 'color': '#919096'},{'movable': 1, 'color': '#b7ae8b'},{'movable': 0, 'color': '#a7bea0'}],
                 [{'movable': 0, 'color': '#e9a164'},{'movable': 1, 'color': '#9f8689'},{'movable': 1, 'color': '#a7938a'},{'movable': 0, 'color': '#c2ad82'},{'movable': 1, 'color': '#e1b974'},{'movable': 1, 'color': '#d37d62'},{'movable': 0, 'color': '#9db6a1'}],
                 [{'movable': 0, 'color': '#e48c5e'},{'movable': 0, 'color': '#d99169'},{'movable': 0, 'color': '#c89673'},{'movable': 0, 'color': '#bb9c80'},{'movable': 0, 'color': '#ada189'},{'movable': 0, 'color': '#a1a697'},{'movable': 0, 'color': '#95aca2'}],
                 [{'movable': 0, 'color': '#e07656'},{'movable': 1, 'color': '#aab398'},{'movable': 1, 'color': '#cc685c'},{'movable': 0, 'color': '#b68c7c'},{'movable': 1, 'color': '#b1bd97'},{'movable': 1, 'color': '#c68370'},{'movable': 0, 'color': '#89a2a4'}],
                 [{'movable': 0, 'color': '#dd5e4f'},{'movable': 1, 'color': '#cea877'},{'movable': 1, 'color': '#bd726c'},{'movable': 0, 'color': '#af7c7b'},{'movable': 1, 'color': '#dca56d'},{'movable': 1, 'color': '#bebb8e'},{'movable': 0, 'color': '#829aa6'}],
                 [{'movable': 0, 'color': '#d94949'},{'movable': 0, 'color': '#c75457'},{'movable': 0, 'color': '#b76268'},{'movable': 0, 'color': '#a86c78'},{'movable': 0, 'color': '#987788'},{'movable': 0, 'color': '#878497'},{'movable': 0, 'color': '#7890a8'}]
            ],
                [
                 [{'movable': 0, 'color': '#e9e8d6'}, {'movable': 1, 'color': '#125275'},
                  {'movable': 1, 'color': '#5db7d9'}, {'movable': 1, 'color': '#238fbe'},
                  {'movable': 1, 'color': '#17678c'}, {'movable': 0, 'color': '#ef515d'}],
                 [{'movable': 1, 'color': '#4e445c'}, {'movable': 0, 'color': '#cebfbc'},
                  {'movable': 0, 'color': '#cda5a4'}, {'movable': 0, 'color': '#cd888b'},
                  {'movable': 0, 'color': '#cf6b75'}, {'movable': 1, 'color': '#ed6f72'}],
                 [{'movable': 1, 'color': '#30415b'}, {'movable': 0, 'color': '#b1b8c0'},
                  {'movable': 0, 'color': '#b19da6'}, {'movable': 0, 'color': '#b0828c'},
                  {'movable': 0, 'color': '#b06675'}, {'movable': 1, 'color': '#41addb'}],
                 [{'movable': 1, 'color': '#8f4a5c'}, {'movable': 0, 'color': '#94b0be'},
                  {'movable': 0, 'color': '#9495a7'}, {'movable': 0, 'color': '#927d8c'},
                  {'movable': 0, 'color': '#8f6374'}, {'movable': 1, 'color': '#97c8d7'}],
                 [{'movable': 1, 'color': '#ae4c59'}, {'movable': 0, 'color': '#78a8bf'},
                  {'movable': 0, 'color': '#758fa6'}, {'movable': 0, 'color': '#74768d'},
                  {'movable': 0, 'color': '#705e74'}, {'movable': 1, 'color': '#ed8e8c'}],
                 [{'movable': 1, 'color': '#eacabf'}, {'movable': 0, 'color': '#5a9fbf'},
                  {'movable': 0, 'color': '#5788a6'}, {'movable': 0, 'color': '#56718e'},
                  {'movable': 0, 'color': '#545b75'}, {'movable': 1, 'color': '#7ac0d7'}],
                 [{'movable': 1, 'color': '#eeaba3'}, {'movable': 0, 'color': '#3f96bf'},
                  {'movable': 0, 'color': '#3c82a6'}, {'movable': 0, 'color': '#366e8f'},
                  {'movable': 0, 'color': '#325774'}, {'movable': 1, 'color': '#ceddd6'}],
                 [{'movable': 0, 'color': '#28a3dc'}, {'movable': 1, 'color': '#71475b'},
                  {'movable': 1, 'color': '#ce4e5b'}, {'movable': 1, 'color': '#1e7aa9'},
                  {'movable': 1, 'color': '#b1d3d5'}, {'movable': 0, 'color': '#0d405d'}]
            ],
            [[{'movable': 0, 'color': '#d9eaf2'}, {'movable': 1, 'color': '#a98b8b'}, {'movable': 1, 'color': '#cce7ec'}, {'movable': 1, 'color': '#ecc4bb'}, {'movable': 1, 'color': '#b5e2df'}, {'movable': 1, 'color': '#f2b7a9'}, {'movable': 0, 'color': '#90dacf'}], [{'movable': 1, 'color': '#70a9b0'}, {'movable': 0, 'color': '#d1dbdc'}, {'movable': 0, 'color': '#c2d6d7'}, {'movable': 0, 'color': '#b2d4d3'}, {'movable': 0, 'color': '#a4cfcd'}, {'movable': 0, 'color': '#95cbc9'}, {'movable': 1, 'color': '#699ba6'}], [{'movable': 1, 'color': '#a7dfda'}, {'movable': 0, 'color': '#d2cdc7'}, {'movable': 0, 'color': '#c3c9c7'}, {'movable': 0, 'color': '#b1c5c6'}, {'movable': 0, 'color': '#9fc1c0'}, {'movable': 0, 'color': '#8dbdbd'}, {'movable': 1, 'color': '#8e848d'}], [{'movable': 1, 'color': '#6f7f8e'}, {'movable': 0, 'color': '#d6bfb9'}, {'movable': 0, 'color': '#c4bbb6'}, {'movable': 0, 'color': '#afb7b7'}, {'movable': 0, 'color': '#9ab2b4'}, {'movable': 0, 'color': '#84aeb2'}, {'movable': 1, 'color': '#e29687'}], [{'movable': 1, 'color': '#c6918b'}, {'movable': 0, 'color': '#dbb3aa'}, {'movable': 0, 'color': '#c2ada6'}, {'movable': 0, 'color': '#ada7a7'}, {'movable': 0, 'color': '#97a1a8'}, {'movable': 0, 'color': '#7da0a8'}, {'movable': 1, 'color': '#e4d1cb'}], [{'movable': 1, 'color': '#87c9c5'}, {'movable': 0, 'color': '#dfa398'}, {'movable': 0, 'color': '#c59f9a'}, {'movable': 0, 'color': '#ac9a98'}, {'movable': 0, 'color': '#939499'}, {'movable': 0, 'color': '#778e9c'}, {'movable': 1, 'color': '#e0dedf'}], [{'movable': 0, 'color': '#ff9d84'}, {'movable': 1, 'color': '#9bdcd6'}, {'movable': 1, 'color': '#5d8a9d'}, {'movable': 1, 'color': '#f8aa96'}, {'movable': 1, 'color': '#c1e5e5'}, {'movable': 1, 'color': '#7cb9ba'}, {'movable': 0, 'color': '#557a94'}]
             ],
            [[{'movable': 0, 'color': '#4b4aca'}, {'movable': 0, 'color': '#5545c9'}, {'movable': 0, 'color': '#633fc5'}, {'movable': 0, 'color': '#6c38bf'}, {'movable': 0, 'color': '#7a31be'}, {'movable': 0, 'color': '#852cba'}, {'movable': 0, 'color': '#8f28b7'}], [{'movable': 0, 'color': '#685bb3'}, {'movable': 1, 'color': '#8a63a2'}, {'movable': 1, 'color': '#91589f'}, {'movable': 0, 'color': '#8340b1'}, {'movable': 1, 'color': '#9c3da1'}, {'movable': 1, 'color': '#a2319d'}, {'movable': 0, 'color': '#9b26a9'}], [{'movable': 0, 'color': '#826e9f'}, {'movable': 1, 'color': '#932fac'}, {'movable': 1, 'color': '#794ab2'}, {'movable': 0, 'color': '#954ba0'}, {'movable': 1, 'color': '#c04b82'}, {'movable': 1, 'color': '#d05172'}, {'movable': 0, 'color': '#a8279e'}], [{'movable': 0, 'color': '#a5818d'}, {'movable': 0, 'color': '#a6718d'}, {'movable': 0, 'color': '#a7628e'}, {'movable': 0, 'color': '#aa5590'}, {'movable': 0, 'color': '#ac4692'}, {'movable': 0, 'color': '#b03590'}, {'movable': 0, 'color': '#b52594'}], [{'movable': 0, 'color': '#c29576'}, {'movable': 1, 'color': '#bd3983'}, {'movable': 1, 'color': '#c1827b'}, {'movable': 0, 'color': '#bf5b7d'}, {'movable': 1, 'color': '#cd3b79'}, {'movable': 1, 'color': '#d77c6a'}, {'movable': 0, 'color': '#c02688'}], [{'movable': 0, 'color': '#dea762'}, {'movable': 1, 'color': '#c0707d'}, {'movable': 1, 'color': '#da9164'}, {'movable': 0, 'color': '#d6646e'}, {'movable': 1, 'color': '#8a36ae'}, {'movable': 1, 'color': '#7151b2'}, {'movable': 0, 'color': '#ca267c'}], [{'movable': 0, 'color': '#fdbb4d'}, {'movable': 0, 'color': '#f6a051'}, {'movable': 0, 'color': '#f08858'}, {'movable': 0, 'color': '#e9705f'}, {'movable': 0, 'color': '#e35764'}, {'movable': 0, 'color': '#db3e69'}, {'movable': 0, 'color': '#d7256f'}]
             ],
            [
              [{'movable': 0, 'color': '#fae7a2'}, {'movable': 1, 'color': '#a3695e'},
              {'movable': 1, 'color': '#99deaf'}, {'movable': 1, 'color': '#d2e1a6'},
              {'movable': 1, 'color': '#e5e4a2'}, {'movable': 1, 'color': '#c0e1aa'},
              {'movable': 0, 'color': '#86ddb2'}],
             [{'movable': 1, 'color': '#c5997c'}, {'movable': 0, 'color': '#d7c794'},
              {'movable': 0, 'color': '#c9c997'}, {'movable': 0, 'color': '#bcc99b'},
              {'movable': 0, 'color': '#aec99e'}, {'movable': 0, 'color': '#a1ca9e'},
              {'movable': 1, 'color': '#c05c52'}],
             [{'movable': 1, 'color': '#b14f4e'}, {'movable': 0, 'color': '#c6aa82'},
              {'movable': 0, 'color': '#c0ae86'}, {'movable': 0, 'color': '#b9b18b'},
              {'movable': 0, 'color': '#b2b48f'}, {'movable': 0, 'color': '#acb894'},
              {'movable': 1, 'color': '#8c3440'}],
             [{'movable': 1, 'color': '#9e4348'}, {'movable': 0, 'color': '#b78e72'},
              {'movable': 0, 'color': '#b89376'}, {'movable': 0, 'color': '#b6987c'},
              {'movable': 0, 'color': '#b79e80'}, {'movable': 0, 'color': '#b5a584'},
              {'movable': 1, 'color': '#b6a989'}],
             [{'movable': 1, 'color': '#8f4a4d'}, {'movable': 0, 'color': '#aa7062'},
              {'movable': 0, 'color': '#b07867'}, {'movable': 0, 'color': '#b4806b'},
              {'movable': 0, 'color': '#ba8772'}, {'movable': 0, 'color': '#c09177'},
              {'movable': 1, 'color': '#ace1ab'}],
             [{'movable': 1, 'color': '#a6ba97'}, {'movable': 0, 'color': '#99544f'},
              {'movable': 0, 'color': '#a55e58'}, {'movable': 0, 'color': '#b3695e'},
              {'movable': 0, 'color': '#bf7363'}, {'movable': 0, 'color': '#c97c68'},
              {'movable': 1, 'color': '#94cba4'}],
             [{'movable': 0, 'color': '#7b2a3b'}, {'movable': 1, 'color': '#cea77e'},
              {'movable': 1, 'color': '#e2c790'}, {'movable': 1, 'color': '#d16a59'},
              {'movable': 1, 'color': '#d58770'}, {'movable': 1, 'color': '#ba886d'},
              {'movable': 0, 'color': '#e57760'}]
             ],
            [[{'movable': 0, 'color': '#f4f3bd'}, {'movable': 0, 'color': '#f3dbab'},
              {'movable': 0, 'color': '#f1c49a'}, {'movable': 0, 'color': '#f2ae89'},
              {'movable': 0, 'color': '#ef987a'}, {'movable': 0, 'color': '#ec806b'},
              {'movable': 0, 'color': '#ee6a5b'}],
             [{'movable': 0, 'color': '#e1e4b7'}, {'movable': 1, 'color': '#b27e80'},
              {'movable': 1, 'color': '#5a7b9e'}, {'movable': 0, 'color': '#d8a98f'},
              {'movable': 1, 'color': '#767c94'}, {'movable': 1, 'color': '#ded0ab'},
              {'movable': 0, 'color': '#cd6c66'}],
             [{'movable': 0, 'color': '#ced8b5'}, {'movable': 1, 'color': '#8aa7a3'},
              {'movable': 1, 'color': '#d08075'}, {'movable': 0, 'color': '#bda193'},
              {'movable': 1, 'color': '#c4b49b'}, {'movable': 1, 'color': '#98a4a2'},
              {'movable': 0, 'color': '#ae6d75'}],
             [{'movable': 0, 'color': '#becbaf'}, {'movable': 0, 'color': '#b5bda8'},
              {'movable': 0, 'color': '#acad9f'}, {'movable': 0, 'color': '#a69d98'},
              {'movable': 0, 'color': '#9d8d90'}, {'movable': 0, 'color': '#977d89'},
              {'movable': 0, 'color': '#8e6e83'}],
             [{'movable': 0, 'color': '#a9beab'}, {'movable': 1, 'color': '#809ba2'},
              {'movable': 1, 'color': '#808a99'}, {'movable': 0, 'color': '#8d989e'},
              {'movable': 1, 'color': '#b88f89'}, {'movable': 1, 'color': '#dbbd9b'},
              {'movable': 0, 'color': '#6e6f8e'}],
             [{'movable': 0, 'color': '#96b2a4'}, {'movable': 1, 'color': '#c8c7a8'},
              {'movable': 1, 'color': '#6786a2'}, {'movable': 0, 'color': '#7491a3'},
              {'movable': 1, 'color': '#d39580'}, {'movable': 1, 'color': '#9fb1a5'},
              {'movable': 0, 'color': '#4e709d'}],
             [{'movable': 0, 'color': '#85a79f'}, {'movable': 0, 'color': '#779ca2'},
              {'movable': 0, 'color': '#6795a3'}, {'movable': 0, 'color': '#588ba6'},
              {'movable': 0, 'color': '#4c82a8'}, {'movable': 0, 'color': '#3c7aa9'},
              {'movable': 0, 'color': '#2f71ab'}]]
        ]
        return level_select[level]

class GameFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#fff6ea")
        self.levels = Levels()  # Initialize Levels
        self.moves_count = 0
        self.buttons = {}
        self.selected_level = 1
        self.highlighted = False
        self.hint_frame = None
        self.clicked = False
        self.current_state = []

        # Upper panel
        self.upper_panel = tk.Frame(self, bg="#fff6ea", width=680, height=100)
        self.upper_panel.pack(side="top", pady=5)

        #Game Board
        self.board_panel = tk.Frame(self, bg="#fff6ea", width=500, height=530)
        self.board_panel.pack(anchor="center", side="bottom", pady=30)
        self.create_grid(self.board_panel)

        # Labels and Buttons
        self.hint_clicked_image = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\hint_bg.png').subsample(20, 20)
        self.hint_image = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\hint_no_bg.png').subsample(20, 20)
        self.back = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\back.png').subsample(5, 5)
        self.hint_text = tk.Label(self.upper_panel, text="Hints", font=('Glacial Indifference', 18), bg="#fff6ea", fg="#6d8b85")
        self.hint_text.place(relx=0.685, rely=0.15)
        self.hint_button = tk.Button(self.upper_panel, image=self.hint_image, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=self.hint_clicked)
        self.hint_button.place(relx=0.68, rely=0.41)
        self.moves_text = tk.Label(self.upper_panel, text="Moves", font=('Glacial Indifference', 18), bg="#fff6ea", fg="#6d8b85")
        self.moves_text.place(relx=0.465, rely=0.15)
        self.moves = tk.Label(self.upper_panel, text=str(self.moves_count), font=('League Spartan', 33), bg="#fff6ea", fg="#6d8b85")
        self.moves.place(relx=0.49, rely=0.5)
        self.level_text = tk.Label(self.upper_panel, text="Level", font=('Glacial Indifference', 18), bg="#fff6ea", fg="#6d8b85")
        self.level_text.place(relx=0.25, rely=0.15)
        self.level_label = tk.Label(self.upper_panel, text=str(self.selected_level), font=('League Spartan', 33), bg="#fff6ea", fg="#6d8b85")
        self.level_label.place(relx=0.275, rely=0.5)
        self.back_button = tk.Button(self.upper_panel, image=self.back, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=self.return_to_select)
        self.back_button.place(relx=0.06, rely=0.45)

        # Binds hover effects
        self.hint_button.bind('<Enter>', lambda e: self.on_hover(self.hint_button))
        self.hint_button.bind('<Leave>', lambda e: self.on_leave(self.hint_button))
        self.back_button.bind('<Enter>', lambda e: self.on_hover(self.back_button))
        self.back_button.bind('<Leave>', lambda e: self.on_leave(self.back_button))

    def hint_clicked(self):
        # Recreates the hint_frame if it doesn't exist or has been destroyed
        if not hasattr(self, 'hint_frame') or self.hint_frame is None or not self.board_panel.winfo_exists():
            self.hint_frame = tk.Frame(self.board_panel, bg="#d2e0fb", height=50, width=50)

            # Creates buttons for the hint options
            self.incorrect = tk.Button(self.hint_frame, bg="#8eaccd", text="Show Incorrectly Placed Tile",
                                       font=('Glacial Indifference', 10), fg="#FFFFFF", width=50, height=5,
                                       command=self.identify_misplaced_tile)
            self.view_complete_button = tk.Button(self.hint_frame, bg="#8eaccd", text="View Complete Puzzle",
                                           font=('Glacial Indifference', 10), fg="#FFFFFF", width=50, height=5,
                                            command=lambda :self.view_complete(self.selected_level))
            self.auto_complete = tk.Button(self.hint_frame, bg="#8eaccd", text="Auto Complete Puzzle",
                                           font=('Glacial Indifference', 10), fg="#FFFFFF", width=50, height=5,
                                           command = self.solve_puzzle)

            # Packs the buttons inside the frame
            self.incorrect.pack(padx=8, pady=5)
            self.view_complete_button.pack(padx=8, pady=5)
            self.auto_complete.pack(padx=8, pady=5)

        # Toggles visibility of the hint frame
        if not self.clicked:
            self.not_clicked()
        else:
            self.clicked_hint()

    def not_clicked(self):
        self.hint_frame.place(relx=0.13, rely=0.21)  # Shows the frame
        self.clicked = True
        self.hint_button.config(image=self.hint_clicked_image)

    def clicked_hint(self):
        if self.hint_frame is not None and self.hint_frame.winfo_exists():
            self.hint_frame.place_forget()  # Hides the frame

        self.hint_button.config(image=self.hint_image)
        self.clicked = False

    def reset_hint_frame(self):
        """Resets or destroys the hint frame when switching levels."""
        if hasattr(self, 'hint_frame') and self.hint_frame is not None:
            self.hint_frame.destroy()
            self.hint_frame = None
        self.clicked = False  # Resets the clicked state

    def save_grid_state(self, filename=r'C:\Users\IDEAPAD\Desktop\ColorMatch\grid_state.json'):
        """
        Saves the current configuration of the puzzle grid to a JSON file.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.current_state, file, indent=4)
            print(f"Grid state saved to {filename}!")
        except Exception as e:
            print(f"Error saving grid state: {e}")

    def load_grid_state(self, filename="grid_state.json"):
        """
        Load a previously saved configuration of the puzzle grid from a JSON file.
        """
        try:
            with open(filename, "r") as file:
                self.current_state = json.load(file)

            # Restore the grid state
            self.level_data = self.current_state
            self.create_grid(self.board_panel)  # Recreate the grid visually
            print(f"Grid state loaded from {filename}!")

        except FileNotFoundError:
            print(f"File {filename} not found! Unable to load grid state.")
        except Exception as e:
            print(f"An error occurred while loading the grid state: {e}")

    def view_complete(self, level):

        self.save_grid_state()
        max_size = (480,480)
        # Hide the hint frame if it exists
        if hasattr(self, 'hint_frame') and self.hint_frame is not None:
            self.hint_frame.place_forget()
            self.hint_frame.pack_forget()

        # Create a new hint frame
        self.hint_frame = tk.Frame(self.board_panel, bg="#d2e0fb", height=500, width=500, relief="raised", bd = 0)
        self.hint_frame.pack(anchor="center", side="bottom", pady=0)

        if level == 1:
            # Keep a reference to the PhotoImage
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level1.png')
        elif level == 2:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level2.png')
        elif level == 3:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level3.png')
        elif level == 4:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level4.png')
        elif level == 5:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level5.png')
        elif level == 6:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level6.png')
        elif level == 7:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level7.png')
        elif level == 8:
            self.level = Image.open(r'C:\Users\IDEAPAD\Desktop\ColorMatch\CorrectPuzzle\Level8.png')

        self.level.thumbnail(max_size)
        self.level_image = ImageTk.PhotoImage(self.level)
        self.level_img = tk.Label(self.hint_frame, image=self.level_image)
        self.level_img.pack(anchor="center")
        self.hint_back = (tk.Button(self.hint_frame, height=10, width=20, font=('Glacial Indifference', 15), bd=1,
                                    text='Click here to go back', command=self.exit_complete_puzzle).pack(side='bottom', pady=2))

        #self.clicked = False
        #self.hint_button.config(image=self.hint_image)
        #self.reset_hint_frame()

    def exit_complete_puzzle(self):
        """Close the view_complete and reset the hint frame."""
        if hasattr(self, 'hint_frame') and self.hint_frame.winfo_exists():
            self.hint_frame.pack_forget()
        self.clicked = False
        self.hint_button.config(image=self.hint_image)
        self.hint_frame = None

    def reset_level(self):
        """Resets the game board and hint frame when changing levels."""
        # Clear the board panel
        for widget in self.board_panel.winfo_children():
            widget.destroy()

        # Reset the hint frame
        self.reset_hint_frame()

        # Reload level data
        self.level_data = self.levels.select_level(self.selected_level - 1)
        self.correct_grid = self.levels.check_level(self.selected_level - 1)
        self.create_grid(self.board_panel)

    def create_grid(self, board_panel):
        # Fixed dimensions
        width = 500
        height = 530

        # Clear any existing widgets
        for widget in board_panel.winfo_children():
            widget.destroy()

        # Get the level data
        self.level_data = self.levels.select_level(self.selected_level - 1)
        self.correct_grid = self.levels.check_level(self.selected_level - 1)
        self.rows = len(self.level_data)
        self.cols = len(self.level_data[0]) if self.rows > 0 else 0
        self.current_state = self.level_data

        # for calculating tile size dynamically
        cell_width = width // self.cols if self.cols > 0 else 0
        cell_height = height // self.rows if self.rows > 0 else 0

        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.level_data[row][col]
                if cell["movable"] == 1:  # Movable
                    btn = tk.Button(
                        board_panel,
                        bd=0,
                        bg=cell["color"],
                        relief="raised",
                        command=lambda r=row, c=col: self.click_tile(r, c, btn)
                    )
                else:  # for immovable tile
                    btn = tk.Button(
                        board_panel,
                        text="X",
                        font = ("Glacial Indifference", 10),
                        fg = "blue",
                        bg=cell["color"],
                        bd=0,
                        state="disabled"
                    )
                    btn.bind("<Button-1>", lambda event: self.show_error())
                self.buttons[(row, col)] = btn
                btn.place(x=col * cell_width, y=row * cell_height, width=cell_width, height=cell_height)

    def return_to_select(self):
        self.pack_forget()  # Hide game frame
        color_match.select_level.pack(fill="both", expand=True)  # Show level selection screen
        self.reset_puzzle()
        self.clicked = False
        self.hint_button.config(image=self.hint_image)

    def show_error(self):
        messagebox.showerror("Invalid Move", "The tile is immovable")
        del self.selected_tile

    def toggle_grid_buttons(self, state):
        """Enable or disable grid buttons based on the state."""
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.level_data[row][col]
                btn = self.buttons.get((row, col))
                if cell["movable"] == 1:  # Only toggle movable buttons
                    btn.config(state=state)

    def click_tile(self, row, col, button):
        if not hasattr(self, "selected_tile"):  # Check if selected_tile exists
            self.selected_tile = (row, col)  # Save the position
        else:
            # Second tile clicked, perform the swap
            selected_row, selected_col = self.selected_tile
            self.swap_tiles((selected_row, selected_col), (row, col))

            # Reset the first tile's appearance
            self.buttons[(selected_row, selected_col)].config(relief="raised")
            self.moves_count += 1
            self.moves.config(text=str(self.moves_count))
            self.validate_grid(self.selected_level)
            # Reset selection only if it exists
            if hasattr(self, "selected_tile"):
                del self.selected_tile  # Reset selection

            if self.highlighted:
                self.reset_highlights()

    """def swap_tiles(self, pos1, pos2):
        # Get button references
        btn1 = self.buttons.get(pos1)
        btn2 = self.buttons.get(pos2)

        if btn1 == btn2:
            messagebox.showerror("Invalid Move", "Can't swap with the same tile")
        else:
            # Swap their colors
            color1 = btn1["bg"]
            color2 = btn2["bg"]

            btn1.config(bg=color2)
            btn2.config(bg=color1)

            self.moves_count += 1
            self.moves.config(text=str(self.moves_count))
            self.validate_grid(self.selected_level)

        if self.highlighted:
            self.reset_highlights()
            self.save_grid_state()"""

    def swap_tiles(self, pos1, pos2):
        """
        Swap two tiles and update the game state.
        """
        row1, col1 = pos1
        row2, col2 = pos2

        # Get button references
        btn1 = self.buttons[(row1, col1)]
        btn2 = self.buttons[(row2, col2)]

        # Swap colors
        color1 = btn1["bg"]
        color2 = btn2["bg"]
        btn1.config(bg=color2)
        btn2.config(bg=color1)

        # Update grid data
        self.level_data[row1][col1]["color"], self.level_data[row2][col2]["color"] = (
            color2,
            color1,
        )
        self.current_state = self.level_data  # Update the current state
        self.save_grid_state("grid_state_live.json")  # Optional live saving
        print(f"Swapped ({row1}, {col1}) with ({row2}, {col2})")

    def solve_puzzle(self):
        #Solves the puzzle step-by-step starting from the current configuration.
        self.clicked_hint()
        correct_grid = self.levels.check_level(self.selected_level - 1)
        locked_tiles = set()  # Keeps track of tiles that are correctly placed

        def find_misplaced_tiles():
            #Identifies all misplaced movable tiles.
            misplaced = []
            for row in range(self.rows):
                for col in range(self.cols):
                    if (
                            self.level_data[row][col]["movable"] == 1
                            and self.level_data[row][col]["color"] != correct_grid[row][col]
                            and (row, col) not in locked_tiles
                    ):
                        misplaced.append((row, col))
            return misplaced

        def find_correct_position(tile_position):
            #Finds the correct position for the given tile.
            row, col = tile_position
            correct_color = correct_grid[row][col]
            for r in range(self.rows):
                for c in range(self.cols):
                    if (
                            self.level_data[r][c]["movable"] == 1
                            and self.level_data[r][c]["color"] == correct_color
                            and (r, c) not in locked_tiles
                    ):
                        return r, c
            return None

        def perform_swap():
            #Performs a swap for the next misplaced tile.
            #Validates grid to check if it's already solved
            if self.validate_grid(self.selected_level - 1):
                return

            misplaced_tiles = find_misplaced_tiles()
            if not misplaced_tiles:
                # If all tiles are correctly placed; stop solving
                return

            # Picks the first misplaced tile and find its correct position
            tile_to_correct = misplaced_tiles[0]
            correct_position = find_correct_position(tile_to_correct)

            if correct_position:
                # Performs the swap and updates the move count
                self.swap_tiles(tile_to_correct, correct_position)
                self.moves_count+=1
                self.moves.config(text=str(self.moves_count))

                # Updates locked tiles
                row1, col1 = tile_to_correct
                row2, col2 = correct_position
                if self.level_data[row1][col1]["color"] == correct_grid[row1][col1]:
                    locked_tiles.add((row1, col1))
                    self.buttons[(row1, col1)].config(state="disabled")
                if self.level_data[row2][col2]["color"] == correct_grid[row2][col2]:
                    locked_tiles.add((row2, col2))
                    self.buttons[(row2, col2)].config(state="disabled")

            # Continues solving after a short delay
            self.after(300, perform_swap)

        # Start solving
        perform_swap()

    def reset_puzzle(self):
        """ Reset the puzzle back to its original state after completing a level """
        self.moves_count = 0
        self.moves.config(text=str(self.moves_count))  # Reset the moves counter

        # Reset the selected tile (if any)
        if hasattr(self, 'selected_tile'):
            del self.selected_tile

        # Recreate the grid with the same level configuration
        self.create_grid(self.board_panel)

        # Optionally reset the level display (if you want to change the level number)
        if hasattr(self, "hint_frame") and self.hint_frame is not None:
            self.hint_frame.destroy()
            self.hint_frame = None

        self.clicked = False

    def validate_grid(self, level):
        # Get the correct grid configuration
        correct_grid = self.levels.check_level(self.selected_level - 1)

        # Get the current grid colors
        current_grid = []
        for row in range(len(correct_grid)):
            current_row = []
            for col in range(len(correct_grid[0])):
                # Retrieve the button at the position (row, col)
                btn = self.buttons[(row, col)]
                current_row.append(btn["bg"])  # Get the current button's background color
            current_grid.append(current_row)

        # Compare current grid with the correct grid
        if current_grid == correct_grid:
            self.show_success_message()
            self.reset_puzzle()
            self.return_to_select()
            return True
        else:
            return False

    def highlight_tile(self, row, col):
        """Highlight a misplaced tile by changing its color."""
        button = self.buttons.get((row,col))
        print((row,col))
        button.config(bd = 1)
        self.hint_frame.place_forget()
        self.highlighted = True

    def identify_misplaced_tile(self):
        """Identify and randomly highlight a misplaced tile."""
        misplaced_tiles = []  # List to store positions of all misplaced tiles

        # Loop through the grid and find all misplaced tiles
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.level_data[row][col]
                if cell["color"] != self.correct_grid[row][col]:
                    button = (row, col)
                    misplaced_tiles.append(button)

        # If there are any misplaced tiles, pick one randomly and highlight it
        if misplaced_tiles:
            random_tile = random.choice(misplaced_tiles)
            row, col = random_tile
            self.highlight_tile(row, col)
            self.clicked = True
            self.hint_clicked()

        self.toggle_grid_buttons("normal")

    def reset_highlights(self):
        """Reset the highlight color of all buttons."""
        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[(row,col)].config(bd = 0)  # Default button color

    def show_success_message(self):
        import tkinter.messagebox as messagebox
        messagebox.showinfo("Level Complete", "Congratulations! You've completed the level.")

    def on_hover(self, button):
        button.config(cursor="hand2")

    def on_leave(self, button):
        button.config(cursor="")

class SelectLevel(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#fff6ea")

        # Upper panel with the "Select Level" title
        self.upper_panel = tk.Frame(self, bg="#fff6ea", width=600, height=100)
        self.upper_panel.pack(padx=10, pady=30)

        self.select = tk.Label(self.upper_panel, text="Select", font=('League Spartan', 50), bg="#fff6ea", fg="#6d8b85")
        self.select.pack(side="left", padx=5)

        self.a = tk.Label(self.upper_panel, text="a", font=('League Spartan', 50), bg="#fff6ea", fg="#1b7985")
        self.a.pack(side="left", padx=5)

        self.level = tk.Label(self.upper_panel, text="Level", font=('League Spartan', 50), bg="#fff6ea", fg="#1d617a")
        self.level.pack(side="left", padx=5)

        # Center panel for level selection buttons
        self.center_panel = tk.Frame(self, bg="#fff6ea", width=480, height=480)
        self.center_panel.pack(padx=0, pady=20)

        # Level buttons
        self.one = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\one.png').subsample(3, 3)
        self.two = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\two.png').subsample(3, 3)
        self.three = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\three.png').subsample(3, 3)
        self.four = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\four.png').subsample(int(2.8), int(2.8))
        self.five = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\five.png').subsample(3, 3)
        self.six = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\six.png').subsample(3, 3)
        self.seven = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\seven.png').subsample(3, 3)
        self.eight = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\eight.png').subsample(3, 3)
        self.back = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\back.png').subsample(3, 3)

        # Button bindings to select a level
        self.one_button = tk.Button(self.center_panel, image=self.one, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=1: self.go_to_level(level))
        self.one_button.grid(row=0, column=0)
        self.two_button = tk.Button(self.center_panel, image=self.two, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=2: self.go_to_level(level))
        self.two_button.grid(row=1, column=0)
        self.three_button = tk.Button(self.center_panel, image=self.three, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=3: self.go_to_level(level))
        self.three_button.grid(row=2, column=0)
        self.four_button = tk.Button(self.center_panel, image=self.four, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=4: self.go_to_level(level))
        self.four_button.grid(row=3, column=0)
        self.five_button = tk.Button(self.center_panel, image=self.five, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=5: self.go_to_level(level))
        self.five_button.grid(row=0, column=1)
        self.six_button = tk.Button(self.center_panel, image=self.six, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=6: self.go_to_level(level))
        self.six_button.grid(row=1, column=1)
        self.seven_button = tk.Button(self.center_panel, image=self.seven, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=7: self.go_to_level(level))
        self.seven_button.grid(row=2, column=1)
        self.eight_button = tk.Button(self.center_panel, image=self.eight, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=lambda level=8: self.go_to_level(level))
        self.eight_button.grid(row=3, column=1)

        # Lower panel with the back button
        self.lower_panel = tk.Frame(self, bg="red", width=100, height=80)
        self.lower_panel.pack(side="right", padx=20)
        self.back_button = tk.Button(self.lower_panel, image=self.back, bg="#fff6ea", bd=0, activebackground="#fff6ea", command=self.return_to_menu)
        self.back_button.pack(side="right")

        # Bind hover effects
        self.one_button.bind('<Enter>', lambda e: self.on_hover(self.one_button))
        self.one_button.bind('<Leave>', lambda e: self.on_leave(self.one_button))
        self.two_button.bind('<Enter>', lambda e: self.on_hover(self.two_button))
        self.two_button.bind('<Leave>', lambda e: self.on_leave(self.two_button))
        self.three_button.bind('<Enter>', lambda e: self.on_hover(self.three_button))
        self.three_button.bind('<Leave>', lambda e: self.on_leave(self.three_button))
        self.four_button.bind('<Enter>', lambda e: self.on_hover(self.four_button))
        self.four_button.bind('<Leave>', lambda e: self.on_leave(self.four_button))
        self.five_button.bind('<Enter>', lambda e: self.on_hover(self.five_button))
        self.five_button.bind('<Leave>', lambda e: self.on_leave(self.five_button))
        self.six_button.bind('<Enter>', lambda e: self.on_hover(self.six_button))
        self.six_button.bind('<Leave>', lambda e: self.on_leave(self.six_button))
        self.seven_button.bind('<Enter>', lambda e: self.on_hover(self.seven_button))
        self.seven_button.bind('<Leave>', lambda e: self.on_leave(self.seven_button))
        self.eight_button.bind('<Enter>', lambda e: self.on_hover(self.eight_button))
        self.eight_button.bind('<Leave>', lambda e: self.on_leave(self.eight_button))
        self.back_button.bind('<Enter>', lambda e: self.on_hover(self.back_button))
        self.back_button.bind('<Leave>', lambda e: self.on_leave(self.back_button))

    def return_to_menu(self):
        self.pack_forget()  # Hide game frame
        color_match.main_menu.pack(fill="both", expand=True)  # Show main menu

    def go_to_level(self, level):
        self.pack_forget()
        color_match.levels.selected_level = level
        print(f"Selected Level: {color_match.levels.selected_level}")
        color_match.levels.create_grid(color_match.levels.board_panel)  # Update game grid for the selected level
        color_match.levels.reset_level()
        color_match.levels.pack(fill="both", expand=True)  # Show game frame
        color_match.levels.level_label.config(text=str(level))

    def on_hover(self, button):
        button.config(cursor="hand2")

    def on_leave(self, button):
        button.config(cursor="")

class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#fff6ea")
        self.master = master

        # for the bg music
        self.sound_on = True
        mixer.init()
        self.play_sound()

        # for the upper text
        text_panel1 = tk.Frame(self, bg="red", width=600, height=100)
        text_panel1.pack(padx=0, pady=20)

        color_label = tk.Label(text_panel1, text="Color", font=('League Spartan', 70), bg="#fff6ea", fg="#8eaccd")
        color_label.pack(side="left", padx=0)
        match_label = tk.Label(text_panel1, text="Match", font=('League Spartan', 70), bg="#fff6ea", fg="#6aabd2")
        match_label.pack(side="left", padx=0)

        # for the lower text
        text_panel2 = tk.Frame(self, bg="#fff6ea", width=600, height=100)
        text_panel2.pack()

        hue_label = tk.Label(text_panel2, text="Hue", font=('League Spartan', 70), bg="#fff6ea", fg="#91b2eb")
        hue_label.pack(side="left", padx=20)
        puzzle_label = tk.Label(text_panel2, text="Puzzle", font=('League Spartan', 70), bg="#fff6ea", fg="#273755")
        puzzle_label.pack(side="left", padx=0)

        # for the buttons
        button_panel1 = tk.Frame(self, bg="#fff6ea", width=460, height=460)
        button_panel1.pack(pady=5)

        button_panel2 = tk.Frame(self, bg="#fff6ea", width=50, height=50)
        button_panel2.pack(side="right")

        self.play_image = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\play.png').subsample(2, 2)
        self.exit_image = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\exit.png').subsample(2, 2)
        self.sound_image = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\sound.png').subsample(5, 5)
        self.sound_off_image = tk.PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Buttons\sound_off.png').subsample(5, 5)

        self.play_button = tk.Button(
            button_panel1,
            image=self.play_image,
            bg="#fff6ea",
            bd=0,
            activebackground="#fff6ea",
            command=self.play_clicked
        )
        self.play_button.pack()

        self.exit_button = tk.Button(
            button_panel1,
            image=self.exit_image,
            bg="#fff6ea",
            bd=0,
            activebackground="#fff6ea",
            command=self.exit_clicked
        )
        self.exit_button.pack()

        self.sound_button = tk.Button(
            button_panel2,
            image=self.sound_image,
            bg="#fff6ea",
            bd=0,
            activebackground="#fff6ea",
            command=self.toggle_sound
        )
        self.sound_button.pack(side="right")

        # Bind hover effects
        self.play_button.bind('<Enter>', lambda e: self.on_hover(self.play_button))
        self.play_button.bind('<Leave>', lambda e: self.on_leave(self.play_button))
        self.exit_button.bind('<Enter>', lambda e: self.on_hover(self.exit_button))
        self.exit_button.bind('<Leave>', lambda e: self.on_leave(self.exit_button))
        self.sound_button.bind('<Enter>', lambda e: self.on_hover(self.sound_button))
        self.sound_button.bind('<Leave>', lambda e: self.on_leave(self.sound_button))

    def play_sound(self):
        if self.sound_on:
            try:
                mixer.music.load(r'C:\Users\IDEAPAD\Desktop\ColorMatch\Music\bg_music.mp3')
                mixer.music.set_volume(0.5)
                mixer.music.play(-1)
            except Exception as e:
                print(f"Error playing music: {e}")

    def play_clicked(self):
        """Switch to game frame"""
        self.pack_forget()  # Hide main menu
        color_match.select_level.pack(fill="both", expand=True)  # Show game frame

        if not mixer.music.get_busy() and self.sound_on:
            self.play_sound()

    def exit_clicked(self):
        self.master.quit()

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        try:
            if self.sound_on:
                self.sound_button.config(image=self.sound_image)
                mixer.music.unpause()
                if not mixer.music.get_busy():
                    self.play_sound()
            else:
                self.sound_button.config(image=self.sound_off_image)
                mixer.music.pause()
        except Exception as e:
            print(f"Error toggling sound: {e}")

    def on_hover(self, button):
        button.config(cursor="hand2")

    def on_leave(self, button):
        button.config(cursor="")

class ColorMatch(tk.Tk):
    def __init__(self):
        super().__init__()

        window_height = 700
        window_width = 700
        screen_height = self.winfo_screenheight() - 100
        screen_width = self.winfo_screenwidth()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.title("ColorMatch Hue Puzzle")
        img = PhotoImage(file=r'C:\Users\IDEAPAD\Desktop\ColorMatch\Logo.png')
        self.iconphoto(False, img)

        # Create frames
        self.main_menu = MainMenu(self)
        self.select_level = SelectLevel(self)
        self.levels = GameFrame(self)
        self.puzzle = Levels(self)

        # Show main menu initially
        self.main_menu.pack(fill="both", expand=True)

if __name__ == "__main__":
    color_match = ColorMatch()
    color_match.mainloop()