import os

base_dir = "/Users/hamed/Documents/2. Areas/Drive/Synology/Web"

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.md'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r') as file:
                lines = file.readlines()
            
            # Check if there is frontmatter
            if len(lines) > 0 and lines[0].strip() == "---":
                # Check if cover already exists
                has_cover = any(line.startswith("cover:") for line in lines)
                if not has_cover:
                    # insert cover: "" right before the second ---
                    try:
                        end_fm = lines[1:].index("---\n") + 1
                        lines.insert(end_fm, 'cover: ""\n')
                        with open(filepath, 'w') as file:
                            file.writelines(lines)
                    except ValueError:
                        pass
