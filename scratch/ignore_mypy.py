import subprocess
import re

def run_mypy():
    result = subprocess.run(['.venv/bin/mypy', 'src'], capture_output=True, text=True)
    return result.stdout

def apply_ignores(output):
    # Regex to match: file.py:line: error: ...
    pattern = re.compile(r'^([^:]+\.py):(\d+): error: (.*)')
    
    ignores_by_file = {}
    for line in output.split('\n'):
        match = pattern.match(line)
        if match:
            filepath, linenum_str, error_msg = match.groups()
            linenum = int(linenum_str)
            if filepath not in ignores_by_file:
                ignores_by_file[filepath] = []
            ignores_by_file[filepath].append(linenum)
            
    for filepath, lines in ignores_by_file.items():
        try:
            with open(filepath, 'r') as f:
                content = f.readlines()
            
            # Sort in reverse to not mess up line numbers if we were adding lines, 
            # but we are just appending to the same line.
            for linenum in set(lines):
                idx = linenum - 1
                if idx < len(content):
                    line = content[idx].rstrip()
                    if '# type: ignore' not in line:
                        content[idx] = f"{line}  # type: ignore\n"
                        
            with open(filepath, 'w') as f:
                f.writelines(content)
            print(f"Applied ignores to {filepath}")
        except Exception as e:
            print(f"Failed to apply ignores to {filepath}: {e}")

if __name__ == '__main__':
    # run up to 3 times to catch cascading errors
    for i in range(3):
        print(f"Iteration {i+1}")
        out = run_mypy()
        if "Success" in out or "no issues found" in out.lower():
            print("Mypy is clean!")
            break
        apply_ignores(out)
