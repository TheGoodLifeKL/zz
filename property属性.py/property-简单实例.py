class Pager():
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10


    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items + 1
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(1)
num_start = p.start
num_end = p.end
print(num_start)
print(num_end)