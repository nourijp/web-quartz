import os

base_dir = "/Users/hamed/Documents/2. Areas/Drive/Synology/Web"

structure = {
    "Services": {
        "Creative Services": ["Photography.md", "Graphic Design.md", "Content Marketing.md", "Technical Writing.md"],
        "Printing Services": ["Photography Prints.md", "Stickers.md", "T-Shirts.md"],
        "Other Services": ["Custom Computer Building.md"]
    },
    "Products for Sale": ["3D Printed.md", "Used Items.md", "Other Products.md"],
    "Classes": ["Mindless Computing.md", "Building a Second Brain.md"],
    "Consulting": ["Consulting Services.md"],
    "Portfolio": ["Projects.md", "Media Appearances.md"]
}

for folder, contents in structure.items():
    if isinstance(contents, dict):
        for subfolder, files in contents.items():
            path = os.path.join(base_dir, folder, subfolder)
            os.makedirs(path, exist_ok=True)
            for f in files:
                filepath = os.path.join(path, f)
                if not os.path.exists(filepath):
                    with open(filepath, "w") as file:
                        tag = folder.lower().replace(" ", "-")
                        file.write(f"---\ntitle: {f.split('.')[0]}\ntags: [\"{tag}\"]\n---\n\n# {f.split('.')[0]}\n\nDetails coming soon...\n")
    else:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
        for f in contents:
            filepath = os.path.join(path, f)
            if not os.path.exists(filepath):
                with open(filepath, "w") as file:
                    tag = folder.lower().replace(" ", "-")
                    file.write(f"---\ntitle: {f.split('.')[0]}\ntags: [\"{tag}\"]\n---\n\n# {f.split('.')[0]}\n\nDetails coming soon...\n")
