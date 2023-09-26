class ContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with ContextManager("employee.txt", "w") as f:
    f.write("Helloooo")

print(f.closed)

# Work
# Create a file
# Multiple lines
# Read all lines
# Copy context from one to another file