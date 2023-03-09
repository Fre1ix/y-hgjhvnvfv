import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to studt")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Time to play")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.money <= 50:
            self.to.work()
        if self.progress <=0:
            self.to_study()
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <=0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed extern")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " Life"
        print(f"{day:=^50}")
        Live_cube = random.randint(1, 4)
        if Live_cube == 1:
            self.to_study()
        elif Live_cube == 2:
            self.to_sleep()
        elif Live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif Live_cube == 4:
            self.to_work()

nick = Student(name = "Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
