import os
import subprocess


for i in range(1, 25):
    day = str(i).zfill(2)
    os.chdir(day)
    try:
        assert os.path.exists("main.py"), f"File {day}/main.py does not exist"
        print(f"Day {day}:")
        subprocess.run(["python", "main.py"], check=True)
    except (AssertionError, subprocess.CalledProcessError) as e:
        print(f"Error on Day {day}: {e}")
    finally:
        os.chdir("..")
        print()
