# 1
class HeavenBody:
    'Родительский клас HeavenBody'
    def __init__(self,name,age,temperature,radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius
        self.attrs = [self.name,self.age,self.temperature,self.radius]
        self.descriptions = ['Название',"Возраст","Температура","Радиус"]
        self.units_of_measure = ['', ' (млн. лет)', ' (С)', ' (км)']
    def display(self):
        for i in range(len(self.attrs)):
            print(f'{self.descriptions[i]}: {self.attrs[i]}{self.units_of_measure[i]}')
        print()
    
class Planet(HeavenBody):
    'Дочерний класс Planet'
    def __init__(self, name, age, temperature, radius,orbital_speed):
        super().__init__(name, age, temperature, radius)
        self.orbital_speed = orbital_speed
        self.attrs.append(self.orbital_speed)
        self.descriptions.append('Орбитальная скорость')
        self.units_of_measure.append(' (км/с)')


class Star(HeavenBody):
    'Дочерний класс Star'
    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation
        self.attrs.append(self.constellation)
        self.descriptions.append('Созвездие')
        self.units_of_measure.append('')
    
planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
planet1.display()

print(Star.__doc__, end='\n')
star1.display()

# 2
import random
import datetime
class Pastry:
    def __init__(self,name,price,manufacuire_date,term):
        self.name = name
        self.price = price
        self.manufacture_date = manufacuire_date
        self.term = term
        self.attrs = [self.name, self.price, self.manufacture_date]
        self.descriptions = ['Название', 'Цена', 'Дата изготовления']
        self.units_of_measure = ['',' (руб.)','']
    def display(self):
        for i in range(len(self.attrs)):
            print(f'{self.descriptions[i]}: {self.attrs[i]}{self.units_of_measure[i]}')
    def valid_unit(self):
        delta = datetime.date.today() - self.manufacture_date 
        delta_days = str(delta).split(' ')[0]
        return int(delta_days)

class Cake(Pastry):
    def __init__(self, name, price, manufacuire_date, term, filling):
        super().__init__(name, price, manufacuire_date, term)
        self.filling = filling
        self.attrs.append(self.filling)
        self.descriptions.append('Начинка')
        self.units_of_measure.append('')
    def order(self):
        delta_days = super().valid_unit()
        super().display()
        if self.term > delta_days:
            print(f'Срок годности истекает через {self.term - delta_days} дня')
            print(f'Оформлен заказ {random.randint(10000,99999)} - Торт с начинкой {self.filling}')
        print()
    

class BentoCake(Pastry):
    def __init__(self, name, price, manufacuire_date, term,celebration):
        super().__init__(name, price, manufacuire_date, term)
        self.celebration = celebration
        self.attrs.append(self.celebration)
        self.descriptions.append('Праздник')
        self.units_of_measure.append('')
    def order(self):
        delta_days = super().valid_unit()
        super().display()
        if self.term > delta_days:
            print(f'Срок годности истекает через {self.term - delta_days} дня')
            print(f'Оформлен заказ {random.randint(10000,99999)} - Бенто торт на {self.celebration}')
        print() 
cake1 = Cake('Торт', 1300, datetime.date(2023, 8, 10), 3, 'вишня')
bento1 = BentoCake('Бенто торт', 1000, datetime.date(2023, 8, 10), 4, 'день рождения')

cake1.order()
bento1.order()

# 3
import random
class BankAccount:
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self.balance = balance
        self.interest_rate = interest_rate
    
    @property
    def holder(self):
        print('are you sure you want to get information about a holder?')
        if input().lower() == 'yes':
            return self.__holder
    @holder.setter 
    def holder(self, holder):
        print('are you sure you want to set information about a holder?')
        if input().lower() == 'yes':
            self.__holder = holder
    
    def __str__(self):
        print(f'Владелец: {self.__holder}')
        print(f'Баланс: \${self.balance:,}')
        print(f'Процентная ставка: {self.interest_rate}')

class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.accountID = random.randint(10000000000000,100000000000000)
        self.actions = []
    def deposit(self,amount):
        self.balance += amount
        self.actions.append(f'Аккаунт {self.accountID} - внесение наличных на счет: \${amount:,.2f}')
    def withdraw(self,amount):
        self.balance -= amount
        self.actions.append(f'Аккаунт {self.accountID} - снятие наличных: \${amount:,.2f}')
    def add_interest(self):
        percentage = self.balance*self.interest_rate
        self.balance += percentage
        self.actions.append(f'Аккаунт {self.accountID} - начислены проценты по вкладу: \${percentage:,.2f}')
    def history(self):
        for i in range(len(self.actions)):
            print(self.actions[i])
    
account = BankOperation('Warren Buffett', 113000000000, 0.08)

account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.add_interest()
account.history()

# 5
import random 
from abc import ABC, abstractmethod
class Investments(ABC):
    'Parent class'
    # листы attrs и description созданы для display(), чтобы не принтить руками
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry
        self.attrs = [self.ticker, self.price, self.currency, self.industry]
        self.description = ['Тикер','Цена','Валюта','Сектор']
    def display(self):
        for i in range(len(self.attrs)):
            print(f'{self.description[i]}: {self.attrs[i]}')

    def buying_securities(func):
        def inner_func(self):
            if self.echelon == 3:
                print('Это высокорискованная сделка')
            else:
                func(self)
            print()
        return inner_func
    
    @abstractmethod
    def buying(self):
        pass

class Shares(Investments):
    'Daughter class'
    def __init__(self, ticker, price, currency, industry,dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit
    
    @Investments.buying_securities
    def buying(self):
        if self.profit > 5:
            count_of_shares = random.randint(1,100)
            print(f'Количество (лот 10): {count_of_shares}')
            print(f'Совершена покупка на сумму: {count_of_shares*self.price}. Поздравляю, Вы стали совладельцем компании!')
        else:
            print('Не могу совершить покупку. Годовая доходность бумаги не больше 5%!')

class Bonds(Investments):
    'Daughter class'
    def __init__(self, ticker, price, currency, industry,coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    @Investments.buying_securities
    def buying(self):
        if self.price <= self.nominal:
            count_of_bounds = random.randint(1,100)
            print(f'Количество (лот 10): {count_of_bounds}')
            print(f'Совершена покупка на сумму: {count_of_bounds*self.price}. Поздравляю, Вы стали кредитором компании!')
        else:
            print('Не могу совершить покупку. Стоимость облигации меньше её номинальной стоимости!')

i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
i1.display()
i1.buying()
i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 1, 1000)
i2.display()
i2.buying()
i3 = Shares('Шампунь Жумайсынба', 10, 'Тенге', 'Косметика', False, 3, -1000)
i3.display()
i3.buying()