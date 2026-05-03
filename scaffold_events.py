import os

base_dir = "/Users/hamed/Documents/2. Areas/Drive/Synology/Web/Events"
os.makedirs(base_dir, exist_ok=True)

with open(os.path.join(base_dir, "Example Tech Festival.md"), "w") as file:
    file.write("---\ntitle: Example Tech Festival\ntags: [\"events\"]\ncover: \"\"\n---\n\n# Example Tech Festival\n\nI will be speaking at this event!\n")

with open(os.path.join(base_dir, "Local Photography Walk.md"), "w") as file:
    file.write("---\ntitle: Local Photography Walk\ntags: [\"events\"]\ncover: \"\"\n---\n\n# Local Photography Walk\n\nHosting a camera walk through the city.\n")
