from datetime import datetime

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            user_input = self.view.get_user_input()
            if user_input == 'c':
                title, description, status, priority, due_date = self.view.get_task_input()
                if due_date:
                    due_date = datetime.strptime(due_date, "%d/%m/%Y")  # Converte para datetime
                self.model.create_task(title, description, datetime.now(), status, priority, due_date)
            elif user_input == 'r':
                tasks = self.model.read_tasks()
                self.view.show_tasks(tasks)
            elif user_input == 'u':
                index = self.view.get_task_index()
                title, description, status, priority, due_date = self.view.get_task_input()
                if due_date:
                    due_date = datetime.strptime(due_date, "%d/%m/%Y")  # Converte para datetime
                self.model.update_task(index, title, description, status, priority, due_date)
            elif user_input == 'd':
                index = self.view.get_task_index()
                self.model.delete_task(index)
            elif user_input == 'q':
                break
