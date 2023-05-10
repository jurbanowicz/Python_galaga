WIDTH = 900
HEIGHT = 800
FPS = 60
TITLESIZE = 64


missle_data = {
    'basic' : {'height' : 40,
               'width' : 20,
               'damage' : 10, 
               'speed' : 10,
               'cooldown' : 0.5, 
               'image_path' : 'main/python/resources/missle_red.png'},
    'basic_green' : {'height' : 40,
               'width' : 20,
               'damage' : 10, 
               'speed' : 8,
               'cooldown' : 0.5, 
               'image_path' : 'main/python/resources/missle_green.png'},
    'bomb' : {'height' : 16,
               'width' : 16,
               'damage' : 30, 
               'speed' : 6,
               'cooldown' : 0.5, 
               'image_path' : 'main/python/resources/bomb.png'},
}

enemy_data = {
    'basic' : {'height' : 50,
               'width' : 50,
               'life' : 30, 
               'exp' : 0, 
               'missle_type' : 'basic_green', 
               'speed' : 0.2, 
               'image_path' : 'main/python/resources/basic_enemy2.png'}
}
booster_data = {
    'shield' : {},
    'health' : {},
    'bomb' : {},
    'freezer' : {}
}