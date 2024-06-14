#app to do list

class ToDoList:
    def __init__(self):
        self.todo = []
        self.done = []

    def add(self, task):
        self.todo.append(task)

    def mark_as_done(self, task):
        self.todo.remove(task)
        self.done.append(task)

    def remove(self, task):
        self.todo.remove(task)


my_list = ToDoList()

my_list.add("Buy milk")
my_list.add("Buy yoghurt")
my_list.add("Do laundry")

print(f"To do: {my_list.todo}")
print(f"Done: {my_list.done}")

my_list.remove("Do laundry")

print(f"To do: {my_list.todo}")
print(f"Done: {my_list.done}")

my_list.mark_as_done("Buy milk")

print(f"To do: {my_list.todo}")
print(f"Done: {my_list.done}")