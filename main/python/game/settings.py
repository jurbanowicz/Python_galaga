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
               'speed' : 10,
               'cooldown' : 0.5, 
               'image_path' : 'main/python/resources/missle_green.png'}

}

enemy_data = {
    'basic' : {'height' : 60,
               'width' : 60,
               'life' : 30, 
               'exp' : 0, 
               'missle_type' : 'basic', 
               'speed' : 5, 
               'image_path' : 'main/python/resources/basic_enemy.png'}
}