import subprocess

# List of scripts to run
scripts = ["KB-Correlation.py", "PDF-Parser.py", "Compare-CVE-Txt-Files.py"]

for script in scripts:
    try:
        # Run each script using subprocess
        result = subprocess.run(["python", script], check=True, capture_output=True, text=True)
        print(f"Output of {script}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script}:\n{e.stderr}")