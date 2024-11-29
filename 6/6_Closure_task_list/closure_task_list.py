def create_task_list():
    """
    Creates task list using closure. Its create one list of tasks with two properties (description, is_complete) and some functions for manipulate it.

    :return: Dictionary with closure functions
    """

    tasks = []

    def add_task(description : str):
        """
        Add new uncompleted task
        :param description: the task text
        """
        if len(description.strip()) < 0:
            raise Exception("Task must contains one char at least.")

        tasks.append({"description" : description, "is_complete" : False})

    def get_uncompleted():
        """
        Select uncompleted tasks amd return it
        :return: list of descriptions in str
        """
        uncompleted = []
        for t in tasks:
            if not t["is_complete"]:
                uncompleted.append(t["description"])
        return uncompleted
    
    def mark_complete(description: str):
        """
        Marks a task as complete
        :param description: description of the task to mark as complete
        """
        for t in tasks:
            if t["description"] == description:
                t['is_complete'] = True
                return
        
        raise Exception("Such a task does not exist in this list")
        
    def get_completed():
        """
        Select completed tasks amd return it
        :return: list of descriptions in str
        """
        completed = []
        for t in tasks:
            if t["is_complete"]:
                completed.append(t["description"])
        return completed

    def get_all():
        """
        Select all tasks amd return it. [ ] before the task means it is not finished, [X] means it is finished
        :return: list of descriptions in str
        """
        all = []
        for t in tasks:
            if t["is_complete"]:
                all.append("[X]" + t["description"])
            else:
                all.append("[ ]" + t["description"])
        return all

    return {"add_task" : add_task, "get_uncompleted": get_uncompleted, "mark_complete": mark_complete, "get_completed": get_completed, "get_all": get_all}

peter_todo = create_task_list()
peter_todo["add_task"]("Vynest smeti")
peter_todo["mark_complete"]("Vynest smeti")
peter_todo["add_task"]("Uklidit si pokojicek")

print(peter_todo["get_all"]())
