# Напишите класс CoffeeMachine, который будет иметь следующие атрибуты и методы:
# water_level — уровень воды в кофейном автомате;
# coffee_level — уровень кофе в кофейном автомате;
# milk_level — уровень молока в кофейном автомате;
# sugar_level — уровень сахара в кофейном автомате;
# cups — количество доступных чашек для приготовления кофе;
# __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0) — конструктор класса, принимает значения и инициализирует соответствующие атрибуты;
# add_water(self, amount) — метод, который принимает значение amount (количество добавляемой воды) и увеличивает атрибут water_level на это значение;
# add_coffee(self, amount) — метод, который принимает значение amount (количество добавляемого кофе) и увеличивает атрибут coffee_level на это значение;
# add_milk(self, amount) — метод, который принимает значение amount (количество добавляемого молока) и увеличивает атрибут milk_level на это значение;
# add_sugar(self, amount) — метод, который принимает значение amount (количество добавляемого сахара) и увеличивает атрибут sugar_level на это значение;
# add_cups(self, number) — метод, который принимает значение number (количество добавляемых чашек) и увеличивает атрибут cups на это значение;
# check_resources(self) — метод, который проверяет наличие достаточных ресурсов (воды, кофе, молока, сахара и чашек) для приготовления кофе. Если все необходимые ингредиенты и чашки доступны в достаточном количестве, метод возвращает True, иначе возвращает False;
# make_coffee(self) — метод, который вызывает метод check_resources() для проверки ресурсов. Если ресурсы доступны, метод уменьшает уровень ингредиентов на соответствующие значения, уменьшает количество доступных чашек на 
#  и выводит сообщение «Кофе готов!». Если ресурсы недостаточны, метод выводит сообщение «Недостаточно ингредиентов!».

class CoffeMachine:
    'programm to make coffe using required level of water,coffe,milk,sugar and 1 cup'
    def __init__(self,water_level,coffee_level,milk_level,sugar_level = 0, cups = 0, required_water = 1,required_coffee = 1,required_milk = 1,required_sugar = 1):
        self.water_level = water_level 
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups
        self.required_water = required_water
        self.required_coffee = required_coffee
        self.required_milk = required_milk
        self.required_sugar = required_sugar
    def add_water(self,amount):
        self.water_level += amount
    def add_coffee(self,amount):
        self.coffee_level += amount
    def add_milk(self, amount):
        self.milk_level += amount
    def add_sugar(self,amount):
        self.sugar_level += amount
    def add_cups(self, amount):
        self.cups += amount
    def check_resources(self):
        if self.water_level >= self.required_water and self.coffee_level >= self.required_coffee and self.milk_level >= self.required_milk and self.sugar_level >= self.required_sugar and self.cups >= 1:
            return True
        return False
    def make_coffee(self):
        if self.check_resources:
            self.water_level -= self.required_water
            self.coffee_level -= self.required_coffee
            self.milk_level -= self.required_milk
            self.sugar_level -= self.required_sugar
            self.cups -= 1
            return 'Coffee is ready!'
        else:
            return 'Lack of ingredients'

# Напишите класс PhotoCamera, представляющий простую фотокамеру. Класс должен иметь следующие атрибуты и методы:
# brand — марка фотокамеры;
# model — модель фотокамеры;
# resolution — разрешение фотографий, где первое число представляет ширину, а второе — высоту;
# is_on — указывает, включена ли фотокамера;
# memory_capacity — обозначает емкость памяти фотокамеры для хранения фотографий;
# photos — хранит фотографии, сделанные с помощью фотокамеры;
# take_photo() — имитирует съемку фотографии. Метод должен выводить сообщение вида «Сделана фотография с разрешением [ширина]x[высота].»;
# get_camera_info() — возвращает строку с информацией о фотокамере в формате «Марка: [марка], Модель: [модель], Разрешение: [ширина]x[высота].»;
# turn_on() — включает фотокамеру. Метод должен установить значение атрибута is_on в True и вывести сообщение «Фотокамера включена.»;
# turn_off() — выключает фотокамеру. Метод должен установить значение атрибута is_on в False и вывести сообщение «Фотокамера выключена.»;
# is_camera_on() — возвращает логическое значение, указывающее, включена ли фотокамера;
# store_photo(photo) — сохраняет фотографию photo в памяти фотокамеры, если есть свободное место. Возвращает True, если фотография успешно сохранена, и False, если память полна;
# view_photos() — выводит информацию о всех фотографиях, сохраненных в памяти фотокамеры;
# clear_memory() — очищает память фотокамеры, удаляя все сохраненные фотографии.

class PhotoCamera():
    'programm to take photos, work with memmory, give info about a photocamera'
    def __init__(self,brand,model,resolution,is_on,memory_capacity,photos = []):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = photos

    def take_photo(self): 
        if not self.is_on:
            return 'Switch on your camera'
        return f"A photo with resolution {self.resolution[0]}x{self.resolution[1]} was taken"
    
    def get_camera_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Resolution: {self.resolution[0]}x{self.resolution[1]}"
    
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def is_camera_on(self):
        return self.is_on
    
    def store_photo(self):
        try:
            assert self.memory_capacity > len(self.photos)
            self.photos.append('photo')
            return True
        except AssertionError:
            return 'Lack of memory'
        
    def view_photos(self):
        return self.photos
    def clear_memory(self):
        self.photos = []

# Напишите класс Revolver со следующей функциональностью:
# максимальная вместимость барабана — 6 элементов;
# метод add_bullet(bullet) добавляет патрон в ближайший свободный слот барабана. Если добавление прошло успешно, возвращается True, иначе False;
# mетод add_bullets_from_list(list) добавляет патроны из списка в барабан. Если в списке недостаточно патронов, барабан заполняется настолько, насколько это возможно. При успешном добавлении любого количества патронов метод возвращает True. В противном случае — если список пустой, метод возвращает False;
# револьвер имеет указатель, который указывает на слот, из которого револьвер готов произвести выстрел;
# метод shoot() удаляет патрон из слота, на который указывает указатель, и передвигает указатель на следующий слот в барабане. Если слот пустой, возвращается None;
# метод unload(all_items=False) извлекает все патроны из барабана или только патрон, на который указывает указатель. Если all_items=True, возвращается список всех патронов. Если all_items=False, возвращается только патрон, на который указывает указатель. Если слот, на который указывает указатель, пустой, метод возвращает None;
# метод scroll() перемещает указатель на случайный слот в барабане;
# метод bullet_count() возвращает количество патронов в барабане.
# Проверьте результат: напишите код, который показывает, как работает класс Revolver.

import random

class Revolver:
    'drum of revolver is a list with len = max_bullet. 1 in this list means one bullet. 0 means empty place in the drum'
    max_bullet = 6
    drum_iterator = 0
    def __init__(self,count_of_bullets = 0): #настраиваем барабан, если при инициализации пуль дали больше или меньше, чем места в барабане
        self.drum = [0]*self.max_bullet
        if count_of_bullets >= self.max_bullet:
            self.drum = [1]*self.max_bullet
        else:
            for i in range(count_of_bullets):
                self.drum_iterator = i
                self.drum[i] = 1
                
        

    def add_bullet(self):
        if self.check_full_drum():
            return False
        min_dist_from_drum_iterator = self.max_bullet
        place_for_drum_iterator = None
        for i in range(self.max_bullet): #здесь мы находим ближайшее свободное место по принципу мусорок из егэ: сравниваем расстояния по часовой стрелке и против часовой у итератора и свободных ячеек, находим минимальное расстояние
            if self.drum[i] == 0:
                if abs(self.drum_iterator - i) < min_dist_from_drum_iterator or self.max_bullet - abs(self.drum_iterator - i) < min_dist_from_drum_iterator:
                    min_dist_from_drum_iterator = min(abs(self.drum_iterator - i), self.max_bullet - abs(self.drum_iterator - i))
                    place_for_drum_iterator = i
        self.drum_iterator = place_for_drum_iterator
        self.drum[self.drum_iterator] = 1
        return True
    
    def add_bullets_from_list(self,bullets):
        if self.check_full_drum() or bullets.count(1) == 0:
            return False
        elif bullets.count(1) >= self.drum.count(0): #если пуль дают больше,чем свободного места в барабане, то создаем массив из единичек
            self.drum = [1]*self.max_bullet
            return True
        else: 
            for j in range(bullets.count(1)): #повторяем действия из add_bullet столько раз, сколько единичек bullet
                self.add_bullet()
            return True
        
    def shoot(self):
        if self.drum[self.drum_iterator] == 1:
            shooted_bullet = self.drum[self.drum_iterator]
            self.drum[self.drum_iterator] = 0
            self.drum_iterator = (self.drum_iterator + 1) % self.max_bullet
            return f'{shooted_bullet} shot from a gun'
        else:
            self.drum_iterator = (self.drum_iterator + 1) % self.max_bullet
            return None
    
    def unload(self,all_items = False):
        if all_items:
            deleted_drum = self.drum
            self.drum = [0]*self.max_bullet
            return f'{deleted_drum} was unload'
        else:
            if self.drum[self.drum_iterator] == 1:
                deleted_bullet = self.drum[self.drum_iterator]
                self.drum[self.drum_iterator] = 0
                return f'{deleted_bullet} was unload'
            return None
        
    def check_full_drum(self):
        return all(self.drum[i] == 1 for i in range(self.max_bullet))
        
    def scroll(self):
        self.drum_iterator = random.randint(0,self.max_bullet-1)

    def bullet_count(self):
        return self.drum.count(1)
            
    def show_drum(self):
        return self.drum
    
Jhon = Revolver(2) #заряжаем два патрона
print(Jhon.show_drum(),Jhon.drum_iterator)
print(Jhon.add_bullet(),Jhon.show_drum(),Jhon.drum_iterator) #добавляем пули
print(Jhon.add_bullet(),Jhon.show_drum(),Jhon.drum_iterator)
print(Jhon.unload(True),Jhon.show_drum(),Jhon.drum_iterator) #удаляем все пули
print(Jhon.add_bullets_from_list([1,False,-10,1]),Jhon.show_drum(),Jhon.drum_iterator) #добавляем пули из списка 
print(Jhon.shoot(),Jhon.show_drum(),Jhon.drum_iterator) #стреляем
print(Jhon.shoot(),Jhon.show_drum(),Jhon.drum_iterator)
print(Jhon.scroll(),Jhon.show_drum(),Jhon.drum_iterator) #прокручиваем
print(Jhon.bullet_count(),Jhon.show_drum(),Jhon.drum_iterator) #количество пуль