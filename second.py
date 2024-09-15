class time():
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min
    def calculate_min(self):
        second_min=self.min*60
        print("The second for given minutes",second_min)
    def calculate_hr(self):
        second_hr=self.hr*3600
        print("the second for given hr",second_hr)
obj=time(1,56)
obj.calculate_min()
obj.calculate_hr()

