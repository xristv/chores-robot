import time

class SyncRobot:
    def __init__(self, name="SyncChoredRobot"):
      self.name = name
  
    def doChores(self):
        self.doLaundry()
        self.doGroceries()
        self.cook()
        self.vacuum()
        self.payBills
  
    def cook(self):
      print("Cooking task: preparing veggies")
      print("Cooking task: into the oven...")
      time.sleep(1)
      print("Cooking task: finished")
  
    def doGroceries(self):
      print("Groceries task: buing healthy stuff...")
      time.sleep(3)
      print("Groceries task: finished")
  
    def doLaundry(self):
      print("Laundry task: put washing maching...")
      time.sleep(2)
      print("Laundry task: finished")
  
    def payBills(self):
      print("Paying bills task: $$$...")
      time.sleep(1)
      print("Paying bills task: finished")
  
    def vacuum(self):
      print("Vacuum task: vacuuming the whole house...")
      time.sleep(2)
      print("Vacuum task: finished")
