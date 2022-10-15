import random
class cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.eat = 5
        self.alive = True
        self.tiredness = 0
    def to_eat(self):
        print("Time to eat")
        self.eat += 2
        self.gladness += 1
        self.tiredness -= 1
    def on_the_walking(self):
        print("Time to walking")
        self.eat -= 1
        self.tiredness += 1
        self.gladness += 2
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.tiredness -= 1
    def to_play(self):
        print("Play time")
        self.gladness += 5
        self.tiredness += 1
        self.eat -= 0.5
    def is_alive(self):
        if self.eat < -0.5:
            print("Kitten died…")
            self.alive = False
        elif self.gladness <= 0:
            print("Kitten is sad…")
            self.alive = False
        elif self.tiredness > 10:
            print("Kitten died… It's overtired")
            self.alive = False
        elif self.eat < 50:
            print("The cat is good!!!")
            self.alive = True
        elif self.eat > 50:
            print("Kitten got very fat… Kitten died…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Eat = {round(self.eat, 2)}")
        print(f"Tiredness = {round(self.tiredness, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.on_the_walking()
        self.end_of_day()
        self.is_alive()

nick = cat(name="Barsik")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)