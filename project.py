import arcade as ar 

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

        # текст меню
        ar.draw_text('Поздравляем! Вы выиграли!',SCREEN_WIDTH/2,SCREEN_HEIGHT/2,ar.color.BLACK,35, anchor_x="center")
        ar.draw_text('Нажмите ПРОБЕЛ для начала',SCREEN_WIDTH/2,125,ar.color.BLACK,18, anchor_x="center")
        ar.draw_text('Нажмите ESC для перехода в меню',SCREEN_WIDTH/2,100,ar.color.BLACK,18, anchor_x="center")
        ar.draw_text('Нажмите Q для выхода',SCREEN_WIDTH/2,75,ar.color.BLACK,18, anchor_x="center")
    
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

        texture = ar.load_texture('image/HackerB_1.png')
        self.textures.append(texture)
        texture = ar.load_texture('image/HackerB_1.png', mirrored=True)
        self.textures.append(texture)
        self.direction = RIGHT_FACING
        self.set_texture(self.direction)
    
    def update_animation(self):

        # условие смены направления изображения
        if self.change_x < 0 and self.direction == RIGHT_FACING:  # движение вправо
            self.direction = LEFT_FACING

        # условие смены направления изображения
        if self.change_x > 0 and self.direction == LEFT_FACING:  # движение влево
            self.direction = RIGHT_FACING
        
        self.set_texture(self.direction)

        if self.left < 20:
            self.left = 20
        elif self.right > SCREEN_WIDTH-20:
            self.right = SCREEN_WIDTH-20
 
        if self.bottom < 15:
            self.bottom =15            
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
        self.map_number = -1
        self.comback = False

        self.coin_sound = ar.Sound('sound\Sound_19349.mp3')
        
        
    def setup(self):
        ar.set_background_color(ar.color.BLUE_SAPPHIRE)
        self.view_left = 0
        self.view_bottom = 0

        self.coin = 0 

        self.back_list = ar.SpriteList()
        self.vxod_list = ar.SpriteList()
        self.stena_list = ar.SpriteList()
        self.coin_list = ar.SpriteList()
        self.enemy_list = ar.SpriteList()
        self.start = ar.SpriteList()
        self.finish = ar.SpriteList()
        self.all_wall_list = ar.SpriteList()
        self.player = Player()

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

        ar.draw_text(f'Количество монет: {self.coin}',100,-2,ar.color.PINK,20)

        ar.draw_text("Для перезагрузки игры нажмите пробел",SCREEN_WIDTH-10, 1,ar.color.PINK,20,anchor_x="right")
        
        
    def update(self,delta_time):
        self.physics_engine.update()
        self.player.update_animation()
        self.player.update()

        for coin in self.coin_list:
            if ar.check_for_collision(coin,self.player):
                self.coin += 1 
                coin.remove_from_sprite_lists()
                self.coin_sound.play(0.005)




        for vxod in self.vxod_list:
            if ar.check_for_collision(vxod, self.player) and self.map_number < 0:
                self.map_number *=-1
                self.setup()
                    
        for vxod in self.vxod_list:
            if ar.check_for_collision(vxod, self.player) and self.map_number > 0:        
                self.map_number *=-1
                self.comback=True
                self.setup()
        
        # for finish in self.finish:
        #     if ar.check_for_collision(finish, self.player):
        #         game_over = GameOver() # присвоение основного класса игры
        #         self.window.show_view(game_over) # переход на другое окно

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