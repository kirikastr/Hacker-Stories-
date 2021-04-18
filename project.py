import arcade as ar 
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Hacker Stories'

map_scale = 1
RIGHT_FACING = 1
LEFT_FACING = 0

# класс меню
class Menu(ar.View):
    #  метод показа 
    def on_show(self):
        ar.set_background_color(ar.color.YELLOW_ROSE)# фон меню

    # метод зарисовки 
    def on_draw(self):
        ar.start_render()

        texture = ar.load_texture('image\Game_menu.png')
        ar.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, texture)

        # текст меню
        ar.draw_text('Нажми на ENTER чтобы начать игру',SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 130,ar.color.BLACK,16,anchor_x="center")
        ar.draw_text('Нажми на Q чтобы выйти из игры',SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 90,ar.color.BLACK,18,anchor_x="center")
    
    def on_key_press(self,key,modification):
        # условие нажатия правой кнопкой мыши
        
        if key == ar.key.ENTER:
            mygame = Mygame() # присвоение основного класса игры
            mygame.setup() # установка начальных значений класса
            self.window.show_view(mygame) # переход на другое окно
        if key == ar.key.Q:
            self.window.close()
        
# класс меню
class GameOver(ar.View):
    #  метод показа 
    def on_show(self):
        ar.set_background_color(ar.color.GENERIC_VIRIDIAN)# фон меню

    # метод зарисовки 
    def on_draw(self):
        ar.start_render()

        texture = ar.load_texture('image\Win.png')
        ar.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, texture)

        # текст меню
        # ar.draw_text('Поздравляем! Вы выиграли!',SCREEN_WIDTH/2,SCREEN_HEIGHT/2,ar.color.BLACK,35, anchor_x="center")
        # ar.draw_text('Нажмите ПРОБЕЛ для начала',SCREEN_WIDTH/2,125,ar.color.BLACK,18, anchor_x="center")
        # ar.draw_text('Нажмите ESC для перехода в меню',SCREEN_WIDTH/2,100,ar.color.BLACK,18, anchor_x="center")
        # ar.draw_text('Нажмите Q для выхода',SCREEN_WIDTH/2,75,ar.color.BLACK,18, anchor_x="center")
    
    def on_key_press(self,key,modification):
        # условие нажатия правой кнопкой мыши
        if key == ar.key.SPACE:
            mygame = Mygame() # присвоение основного класса игры
            mygame.setup() # установка начальных значений класса
            self.window.show_view(mygame) # переход на другое окно
        if key == ar.key.ESCAPE:
            menu = Menu()
            self.window.show_view(menu)
        if key == ar.key.Q:
            self.window.close()

# class Task(ar.View):
#     def on_show(self):
#         ar.set_background_color(ar.color.BLUE_BELL)

#     def on_draw(self):
#         ar.start_render()

#     def on_key_press(self,key,modification):
#         if key == ar.key.ENTER:
#             mygame = Mygame()
#             mygame.setup()
#             self.window.show_view(mygame)





# class Enemy(ar.Sprite):
#     def __init__(self):
#         super ().__init__()

#         self.scale = 1

#         self.texture = ar.load_texture('image\Virus.png')

#         self.center_x = x 
#         self.center_y = y yield

#         ok = random.randrange(0,1)
#         self.change_x = speed_list[ok]

#         ladno = random.randrange(0,1)
#         self.change_y = speed_list[ladno]

#     def update(self):
#         self.center_x += self.change_x
#         self.center_y += self.change_y

#         # условие ходьбы только по оси Х
#         if self.change_x != 0 and random.randint(0,1) == 0:
#             self.change_y = 0 

#         # условие ходьбы только по оси У
#         if self.change_y != 0 and random.randint(0,1) == 1:
#             self.change_x = 0

#         # условие смены направления
#         if random.randint(0,50) == 0:
#             self.change_x = 0
#             self.change_y = 0 
#             if random.randint(0,1) == 1:
#                 ok = random.randint(0,1) # выбор скорости
#                 self.change_x = speed_list[ok]

#             else:
#                 ladno = random.randint(0,1) # выбор скорости
#                 self.change_y = speed_list[ladno]
        

class Player(ar.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = 1

        texture = ar.load_texture('image/HackerA_1.png')
        self.textures.append(texture)
        texture = ar.load_texture('image/HackerA_1.png', mirrored=True)
        self.textures.append(texture)
        self.direction = RIGHT_FACING
        self.set_texture(self.direction)
    
    def update_animation(self):

        # условие смены направления изображения
        if self.change_x < 0 and self.direction == RIGHT_FACING:  # движение вправо
            self.direction = LEFT_FACING

        # условие смены направления изображения
        if self.change_x > 0 and self.direction == LEFT_FACING:  # движение влевоz
            self.direction = RIGHT_FACING
        
        self.set_texture(self.direction)

        if self.left < 20:
            self.left = 20
        elif self.right > SCREEN_WIDTH-20:
            self.right = SCREEN_WIDTH-20
 
        if self.bottom < 15:
            self.bottom = 15            
        elif self.top > SCREEN_HEIGHT-15:
            self.top = SCREEN_HEIGHT-15

class Mygame(ar.View):
    def __init__(self):
        super().__init__()

        self.stena_list = None 
        self.vxod_list = None 
        self.back_list = None 
        self.player = None
        self.enemy_list = None 
        self.coin_list = None 
        self.collision_list = None 
        self.map_number = -1
        self.comback = False
        self.question = False 

        self.coin_sound = ar.Sound('sound\Sound_19349.mp3')
        self.damage_sound = ar.Sound('sound\damage by kirik.m4a')
        
        
    def setup(self):
        ar.set_background_color(ar.color.BLUE_SAPPHIRE)
        self.view_left = 0
        self.view_bottom = 0

        self.coin = 0 
        self.hp = 3 

        self.back_list = ar.SpriteList()
        self.vxod_list = ar.SpriteList()
        self.stena_list = ar.SpriteList()
        self.coin_list = ar.SpriteList()
        self.enemy_list = ar.SpriteList()
        self.start = ar.SpriteList()
        self.finish = ar.SpriteList()
        self.all_wall_list = ar.SpriteList()
        self.player = Player()
        self.collision_list = ar.SpriteList()
        self.question_list = ['Что отвечает за зарисовки картины?','Как инцеализируется библиотека?','Как называется команда открытие окна?']



        # coordinate_list = [[780,775],[780,785],[790,780]]

        # for coordinate in coordinate_list:
        #     enemy = Enemy(coordinate[0], coordinate[1])
        #     self.enemy_list.append(enemy)

        if self.map_number < 0 and self.comback == True:
            my_map = ar.tilemap.read_tmx('maps\map.tmx')          
            self.player.center_x = 760
            self.player.center_y = 750
        elif self.map_number < 0:
            my_map = ar.tilemap.read_tmx('maps\map.tmx')          
            self.player.center_x = 50
            self.player.center_y = 120
        elif self.map_number > 0:
            my_map = ar.tilemap.read_tmx("maps\map1.tmx")
            self.player.center_x = 50
            self.player.center_y = 425
        
            
        
        self.back_list = ar.tilemap.process_layer(my_map,'back',map_scale)
        self.vxod_list = ar.tilemap.process_layer(my_map,'vxod',map_scale)
        self.stena_list = ar.tilemap.process_layer(my_map,'stena',map_scale)
        self.start = ar.tilemap.process_layer(my_map,'start',map_scale)
        self.finish = ar.tilemap.process_layer(my_map,'finish',map_scale)
        self.enemy_list = ar.tilemap.process_layer(my_map,'enemy',map_scale)
        self.collision_list = ar.tilemap.process_layer(my_map,'enemy_block',map_scale)

        #enemy speed
        for enemy in self.enemy_list:
            enemy.change_x = random.randrange(-3,3,2)

        # self.enemy_list[0].change_x = 3

        for i in range(2):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 45
            coin.center_y = 200 + i * 64
            self.coin_list.append(coin)

        for i in range(2):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 200
            coin.center_y = 560 + i * 64
            self.coin_list.append(coin)

        for i in range(3):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 450
            coin.center_y = 520 + i * 64
            self.coin_list.append(coin)
        
        for i in range(1):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 400
            coin.center_y = 260 + i * 64
            self.coin_list.append(coin)

        for i in range(1):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 500
            coin.center_y = 60 + i * 64
            self.coin_list.append(coin)

        for i in range(1):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 540
            coin.center_y = 260 + i * 64
            self.coin_list.append(coin)            

        for i in range(2):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 560 + i * 64
            coin.center_y = 605 
            self.coin_list.append(coin)          

        for i in range(2):
            coin = ar.Sprite('image\Money.png',2)
            coin.center_x = 160 + i * 64
            coin.center_y = 320 
            self.coin_list.append(coin)        
        
        self.physics_engine = ar.PhysicsEngineSimple(self.player, self.stena_list)

    def on_draw(self):
        ar.start_render()
        self.back_list.draw()
        self.stena_list.draw()
        self.vxod_list.draw()
        self.coin_list.draw()
        self.start.draw()
        self.finish.draw()
        self.player.draw()
        self.enemy_list.draw()
        # self.collision_list.draw()

        ar.draw_text(f'Количество монет: {self.coin}',100,1,ar.color.RED,14)
        ar.draw_text(f'Жизни: {self.hp}',280,1,ar.color.RED,14)

        ar.draw_text("Для перезагрузки игры нажмите пробел",SCREEN_WIDTH-100, 1,ar.color.RED,14,anchor_x="right")

        if self.question == True:

            # self.ran = random.randint(0,2)
            ar.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 400,200, ar.color.LIGHT_SKY_BLUE)
            ar.draw_text(f"{self.question_list[self.ran]}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, ar.color.BLACK,20, anchor_x="center")
            ar.draw_text("Yes", SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-100, ar.color.BLACK,20, anchor_x="center")
            ar.draw_text("No", SCREEN_WIDTH/2+150, SCREEN_HEIGHT/2-100 , ar.color.BLACK,20, anchor_x="center")

        
        
    def update(self,delta_time):
        self.physics_engine.update()
        self.player.update_animation()
        self.player.update()
        self.enemy_list.update()

        #code dlya otskoka
        for enemy in self.enemy_list:

            if self.hp <=0:
                return



            # collisia
            if ar.check_for_collision_with_list(enemy, self.collision_list):
                #code vupolnenie
                enemy.change_x *= -1 

        for coin in self.coin_list:
            if ar.check_for_collision(coin,self.player):
                self.coin += 1 
                coin.remove_from_sprite_lists()
                self.coin_sound.play(0.05)

        # if ar.check_for_collision(enemy,self.player):
        #     self.hp -=1
        #     # self.player.center_x = 300
        #     # self.player.center_y = 300
        #     self.damage_sound.play(0.05)

        # for self.enemy_list in self.task:
        #     if ar.check_for_collision(self.enemy_list,self.player):







        for vxod in self.vxod_list:
            if ar.check_for_collision(vxod, self.player) and self.map_number < 0:
                self.map_number *=-1
                self.setup()
                    
        for vxod in self.vxod_list:
            if ar.check_for_collision(vxod, self.player) and self.map_number > 0:        
                self.map_number *=-1
                self.comback=True
                self.setup()
        
        for finish in self.finish:
            if ar.check_for_collision(finish, self.player):
                game_over = GameOver() # присвоение основного класса игры
                self.window.show_view(game_over) # переход на другое окно

        for enemy_list in self.enemy_list:
            if ar.check_for_collision(self.player, enemy_list):
                self.question = True 
                enemy_list.remove_from_sprite_lists()
                self.ran = random.randint(0,2)

        # for enemy in self.enemy_list:
        #     if ar.check_for_collision_with_list(enemy,self.wall_list):
        #         if enemy.change_x > 0: 
        #             enemy.change_x =  speed_list[0]  # -3
        #         elif enemy.change_x < 0:
        #             enemy.change_x = speed_list[1]  # 3

        #         if enemy.change_y > 0: 
        #             enemy.change_y = speed_list[0]
        #         elif enemy.change_y < 0:
        #             enemy.change_y = speed_list[1]
             


    
    def on_key_press(self,key,modifiers):
        if key == ar.key.A:
            self.player.change_x = -5
        if key == ar.key.D:
            self.player.change_x = 5 
        if key == ar.key.W:
            self.player.change_y = 5
        if key == ar.key.S:
            self.player.change_y = -5
        
        if key == ar.key.SPACE:
            self.map_number = -1
            self.comback = False
            self.setup()

        if key == ar.key.Y:
            self.question = False

        if key == ar.key.N:
            self.question = False

        # if key == ar.key.E:
        #     task = Task()
        #     self.window.show_view(task)            
            
        

    def on_key_release(self,key,modifiers):
        if key == ar.key.A:
            self.player.change_x = 0
        if key == ar.key.D:
            self.player.change_x = 0 
        if key == ar.key.W:
            self.player.change_y = 0
        if key == ar.key.S:
            self.player.change_y = 0

def main():
    window = ar.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = Menu()
    window.show_view(menu)
    ar.run()

main()