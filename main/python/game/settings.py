WIDTH = 900
HEIGHT = 800
FPS = 60
TITLESIZE = 64
GAME_FONT = 'main/python/resources/upheavtt.ttf'
FONT_COLOR = (255, 179, 0)


player_data = {
    'basic' : {'height' : 70,
               'width' : 70,
               'life' : 100, 
               'shooting_limiter' : 0.2,
               'missle_location' : -50, 
               'speed' : 8, 
               'image_path' : 'main/python/resources/player3.png'}
               }


missle_data = {
    'basic' : {'height' : 30,
               'width' : 15,
               'damage' : 10, 
               'speed' : 10,
               'image_path' : 'main/python/resources/missle_blue.png'},
    'basic_green' : {'height' : 30,
               'width' : 15,
               'damage' : 10, 
               'speed' : 8,
               'image_path' : 'main/python/resources/missle_green2.png'},

    'basic_orange' : {'height' : 30,
               'width' : 15,
               'damage' : 5, 
               'speed' : 8,
               'image_path' : 'main/python/resources/missle_orange.png'},

    'basic_yellow' : {'height' : 30,
            'width' : 15,
            'damage' : 20, 
            'speed' : 8,
            'image_path' : 'main/python/resources/missle_yellow.png'},

    'basic_white' : {'height' : 30,
            'width' : 9,
            'damage' : 12, 
            'speed' : 8,
            'image_path' : 'main/python/resources/missle_white.png'},

    'missle' : {'height' : 30,
            'width' : 15,
            'damage' : 40, 
            'speed' : 5,
            'image_path' : 'main/python/resources/missle_bomb.png'},


    'bomb' : {'height' : 16,
               'width' : 16,
               'damage' : 30, 
               'speed' : 6,
               'image_path' : 'main/python/resources/bomb.png'},
}

enemy_data = {
    'basic' : {'height' : 50,
               'width' : 50,
               'life' : 30, 
               'exp' : 0, 
               'shooting_limiter' : 1,
               'missle_type' : 'basic_green',
               'missle_location' : 10,  
               'speed' : 0.2, 
               'spawning_speed' : 3,
               'image_path' : 'main/python/resources/basic_enemy.png'},
            

    'fighter' : {'height' : 70,
               'width' : 70,
               'life' : 30, 
               'exp' : 10, 
               'shooting_limiter' : 1.5,
               'missle_type' : 'basic_green',
               'missle_location' : 50, 
               'speed' : 0.2, 
               'spawning_speed' : 2,
               'image_path' : 'main/python/resources/fighter.png'},
    'striker' : {'height' : 70,
               'width' : 70,
               'life' : 20, 
               'exp' : 10, 
               'shooting_limiter' : 0.8,
               'missle_type' : 'basic_orange',
               'missle_location' : 50,  
               'speed' : 0.3, 
               'spawning_speed' : 3,
               'image_path' : 'main/python/resources/striker.png'},
    'heavy' : {'height' : 80,
               'width' : 80,
               'life' : 50, 
               'exp' : 20, 
               'shooting_limiter' : 1.5,
               'missle_type' : 'basic_yellow', 
               'missle_location' : 50, 
               'speed' : 0.1, 
               'spawning_speed' : 1.25,
               'image_path' : 'main/python/resources/heavy.png'},

    'destroyer' : {'height' : 95,
               'width' : 95,
               'life' : 80, 
               'exp' : 50, 
               'shooting_limiter' : 0.6,
               'missle_type' : 'missle',
               'missle_location' : 65,  
               'speed' : 0.15, 
               'spawning_speed' : 0.75,
               'image_path' : 'main/python/resources/destroyer.png'},

    'helper' : {'height' : 60,
                'width' : 60,
                'life' : 30, 
                'exp' : 5, 
                'shooting_limiter' : 1,
                'missle_type' : 'basic_green',
                'missle_location' : 40,  
                'speed' : 0.3, 
                'spawning_speed' : 0.75,
                'image_path' : 'main/python/resources/helper.png'},


    'boss' : {'height' : 220,
                'width' : 220,
                'life' : 200, 
                'exp' : 100, 
                'shooting_limiter' : 1.3,
                'missle_type' : 'missle',
                'missle_location' : 75,  
                'speed' : 0.1, 
                'spawning_speed' : 2,
                'image_path' : 'main/python/resources/boss.png'},

    'reinforcement' : {'height' : 45,
               'width' : 45,
               'life' : 30, 
               'exp' : 0, 
               'shooting_limiter' : 0.6,
               'missle_type' : 'basic_white',
               'missle_location' : -40,  
               'speed' : 0.3, 
               'spawning_speed' : 0,
               'image_path' : 'main/python/resources/reinforcement.png'}

}
booster_data = {
    'xp' : {'height' : 20,
               'width' : 20,
               'image_path' : 'main/python/resources/xp.png',
               'speed' : 3 },
    'health' : {'height' : 30,
               'width' : 25,
               'image_path' : 'main/python/resources/shield.png',
               'speed' : 3},
    'bomb' : {'height' : 20,
               'width' : 20,
               'image_path' : 'main/python/resources/bomb_booster.png',
               'speed' : 3},
    'reinforcement' : {'height' : 20,
               'width' : 20,
               'image_path' : 'main/python/resources/reinforce.png',
               'speed' : 3}
}