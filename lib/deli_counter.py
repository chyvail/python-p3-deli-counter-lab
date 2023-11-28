# deli_counter.py

class DeliCounter:
    def __init__(self):
        self.line = []

    def take_a_number(self, name):
        self.line.append(name)
        return f"Welcome, {name}. You are number {len(self.line)} in line."

    def line(self):
        if not self.line:
            return "The line is currently empty."
        else:
            current_line = ", ".join(f"{index + 1}. {name}" for index, name in enumerate(self.line))
            return f"The current line: {current_line}"
