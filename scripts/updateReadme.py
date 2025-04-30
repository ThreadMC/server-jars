import os
import re

README_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'README.md'))
VERSIONS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'versions'))

def version_key(s):
    return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', s)]

def build_tree(path, prefix=''):
    entries = sorted(os.listdir(path), key=version_key, reverse=True)
    tree_lines = []
    for idx, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = '└── ' if idx == len(entries) - 1 else '├── '
        if os.path.isdir(full_path):
            tree_lines.append(f"{prefix}{connector}{entry}")
            sub_prefix = prefix + ('    ' if idx == len(entries) - 1 else '│   ')
            sub_tree = build_tree(full_path, sub_prefix)
            tree_lines.extend(sub_tree)
        else:
            tree_lines.append(f"{prefix}{connector}{entry}")
    return tree_lines

def update_readme(structure_lines):
    with open(README_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '## Structure':
            start_idx = i
            break
    if start_idx is None:
        raise Exception("Could not find '## Structure' section in README.md")

    code_start = None
    for i in range(start_idx, len(lines)):
        if lines[i].strip().startswith('```'):
            code_start = i
            break
    if code_start is None:
        raise Exception("Could not find code block after '## Structure' in README.md")

    code_end = None
    for i in range(code_start + 1, len(lines)):
        if lines[i].strip().startswith('```'):
            code_end = i
            break
    if code_end is None:
        code_end = code_start + 1

    new_code_block = ['```\n'] + [line + '\n' for line in structure_lines] + ['```\n']
    new_lines = lines[:code_start] + new_code_block + lines[code_end+1:]

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    tree_lines = ['versions']
    tree_lines += build_tree(VERSIONS_PATH, prefix='')
    update_readme(tree_lines)

if __name__ == '__main__':
    main()
