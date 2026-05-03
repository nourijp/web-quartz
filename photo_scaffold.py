import os

base_dir = "/Users/hamed/Documents/2. Areas/Drive/Synology/Web/Services/Creative Services/Photography"
os.makedirs(base_dir, exist_ok=True)

files = ["Event Photography.md", "Portrait Photography.md", "Product Photography.md", "Street Photography.md"]

for f in files:
    filepath = os.path.join(base_dir, f)
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write(f"---\ntitle: {f.split('.')[0]}\ntags: [\"photography\"]\n---\n\n# {f.split('.')[0]}\n\nDetails coming soon...\n")
