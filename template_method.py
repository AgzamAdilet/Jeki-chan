from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments(): # Hook (Перехватчик) [cite: 71]
            self.add_condiments()

    def boil_water(self): print("Су қайнатылуда")
    def pour_in_cup(self): print("Шыныаяққа құйылуда")

    @abstractmethod
    def brew(self): pass
    @abstractmethod
    def add_condiments(self): pass

    def customer_wants_condiments(self): return True

class Tea(Beverage):
    def brew(self): print("Шай демделуде")
    def add_condiments(self): print("Лимон қосылды")

class Coffee(Beverage):
    def brew(self): print("Кофе дәндері пісірілуде")
    def add_condiments(self): print("Қант пен сүт қосылды")
    def customer_wants_condiments(self):
        ans = input("Қоспалар қосу керек пе? (и/ж): ") # Тұтынушы таңдауы [cite: 62]
        return ans.lower() == 'и'

tea = Tea()
tea.prepare_recipe()