import os
import re


def remove_self_closing_slashes(directory):
    # Regex pattern to find self-closing tags
    pattern = re.compile(r'<(\w+)([^>]*)\s*/>')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace self-closing tags with open tags
                new_content = pattern.sub(r'<\1\2>', content)

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"Processed {file_path}")


# Replace 'your_directory_path' with the path to your HTML files
directory_path = 'C:\\Users\hp compac\\alx-frontend\\0x00-html_advanced'
remove_self_closing_slashes(directory_path)
