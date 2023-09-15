class TaskView:
    def show_tasks(self, tasks):
        for index, task in enumerate(tasks):
            formatted_due_date = task.formatted_due_date()
            print(f"{index + 1}. {task.title} - {task.status} - Prioridade: {task.priority} - Vencimento: {formatted_due_date}")

    def get_user_input(self):
        return input("Escolha uma ação (C - Criar, R - Ler, U - Atualizar, D - Deletar, Q - Sair): ").strip().lower()

    def get_task_input(self):
        title = input("Título da tarefa: ")
        description = input("Descrição da tarefa: ")
        status = input("Status da tarefa (concluída ou pendente): ")
        priority = input("Prioridade da tarefa (baixa, média, alta, etc.): ")
        due_date = input("Data de vencimento da tarefa (formato: YYYY-MM-DD): ")
        return title, description, status, priority, due_date

    def get_task_index(self):
        return int(input("Digite o número da tarefa: ")) - 1
