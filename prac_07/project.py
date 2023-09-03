class Project:
    def __init__(self, name, start_date, priority, estimate, completion_percent):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion_percent = completion_percent

    def __lt__(self, other):
        # Implement comparison logic for sorting by priority
        return self.priority < other.priority

    def __str__(self):
        # Implement a string representation of the project
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion_percent}%"