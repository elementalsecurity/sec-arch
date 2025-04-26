import os

# Define your repo base directory
BASE_DIR = './'  # Set to your local repo root

# Define the copyright block
COPYRIGHT_BLOCK = """---
© 2025 Elemental Security Solutions, LLC
Part of the Security Architecture Knowledge Base.
Licensed under the MIT License.
"""

# Folders to exclude
EXCLUDED_FOLDERS = ['.github', 'assets']

def should_exclude_file(file_path):
    lower_path = file_path.lower()
    return any(excluded in lower_path for excluded in EXCLUDED_FOLDERS)

def footer_already_present(content):
    return '© 2025 Elemental Security Solutions, LLC' in content

def remove_footer(content):
    # Remove the copyright block cleanly if present
    footer_lines = COPYRIGHT_BLOCK.strip().splitlines()
    for line in footer_lines:
        content = content.replace(line.strip(), '')
    return content.strip()

def process_markdown_files():
    updated_files = []
    removed_files = []
    skipped_files = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                lower_file = file.lower()
                
                if should_exclude_file(file_path):
                    continue

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                if 'readme' in lower_file:
                    if footer_already_present(content):
                        new_content = remove_footer(content)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content.strip() + '\n')
                        removed_files.append(file_path)
                        print(f'🗑️ Removed copyright from: {file_path}')
                    else:
                        skipped_files.append(file_path)
                        print(f'⏭️ Skipped (no footer to remove): {file_path}')
                else:
                    if not footer_already_present(content):
                        with open(file_path, 'a', encoding='utf-8') as f:
                            f.write('\n\n' + COPYRIGHT_BLOCK)
                        updated_files.append(file_path)
                        print(f'✔️ Added copyright to: {file_path}')
                    else:
                        skipped_files.append(file_path)
                        print(f'⏭️ Skipped (already has footer): {file_path}')

    # Summary Report
    print('\n--- Summary Report ---')
    print(f'Total Markdown files processed: {len(updated_files) + len(removed_files) + len(skipped_files)}')
    print(f'Files updated with copyright footer: {len(updated_files)}')
    print(f'Files with footer removed (README types): {len(removed_files)}')
    print(f'Files skipped (no changes needed): {len(skipped_files)}')

if __name__ == '__main__':
    process_markdown_files()
