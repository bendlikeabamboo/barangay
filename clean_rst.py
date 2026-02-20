import os
import re
import sys


def fix_rst_content(text):
    lines = text.splitlines()
    for i in range(1, len(lines)):
        # Regex matches lines consisting only of rst adornment characters
        # It ensures the line is at least 2 characters long to avoid accidental matches
        if re.match(r'^([=\-`:"\'~^_*+#])\1+$', lines[i]):
            # Align length to the line above (the heading text)
            lines[i] = lines[i][0] * len(lines[i - 1].rstrip())
    return "\n".join(lines)


def process_directory(target_dir):
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".rst"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    original_content = f.read()

                fixed_content = fix_rst_content(original_content)

                if original_content != fixed_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(fixed_content)
                    print(f"Fixed: {file_path}")


if __name__ == "__main__":
    # Use current directory if no path is provided
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"Scanning for .rst files in: {os.path.abspath(target)}")
    process_directory(target)
    print("Done!")
