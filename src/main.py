from Controller.TaskController import TaskController
from Model.Task import TaskModel
from View.TaskView import TaskView

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
