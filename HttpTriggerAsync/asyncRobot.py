import asyncio


class AsyncRobot:
    def __init__(self, name="SyncChoredRobot"):
      self.name = name

    async def doChores(self):
      tasks = [self.doLaundry(), self.doGroceries(), self.cook(), self.vacuum(), self.payBills()]
      await asyncio.wait(tasks)
  
    async def cook(self):
      print("Cooking task: preparing veggies")
      print("Cooking task: into the oven...")
      await asyncio.sleep(1)
      print("Cooking task: finished")
  
    async def doGroceries(self):
      print("Groceries task: buing healthy stuff...")
      await asyncio.sleep(3)
      print("Groceries task: finished")
  
    async def doLaundry(self):
      print("Laundry task: put washing maching...")
      await asyncio.sleep(2)
      print("Laundry task: finished")
  
    async def payBills(self):
      print("Paying bills task: $$$...")
      await asyncio.sleep(1)
      print("Paying bills task: finished")
  
    async def vacuum(self):
      print("Vacuum task: vacuuming the whole house...")
      await asyncio.sleep(2)
      print("Vacuum task: finished")
