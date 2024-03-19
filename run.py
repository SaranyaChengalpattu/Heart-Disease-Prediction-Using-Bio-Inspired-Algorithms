import subprocess

def run_script(script_name):
    print(f"Running {script_name}...")
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    # List of scripts to run
    scripts = [
        "Main.py",
        "BEE.py",
        "BAT.py",
        "ACO.py",
        "GA.py"
    ]

    # Run each script
    for script in scripts:
        run_script(script)

    print("All scripts executed.")
