import os
import os.path
import shutil
import subprocess
import venv

# create setup.py -> create virtualenv -> install pip-tools
def main():
    venv.create(".venv", clear=True, symlinks=True, with_pip=True)
    subprocess.run([".venv/bin/pip", "install", "pip-tools", "--quiet"])
    #
    shutil.rmtree("requirements", ignore_errors=True)
    os.mkdir("requirements", mode=0o755)
    #
    with open("requirements/base.in", "w") as file:
        file.write("\n")
    process = subprocess.run(
        [".venv/bin/pip-compile", "-q", "-o", "requirements/base.txt", "requirements/base.in"]
    )
    process.check_returncode()
    #
    with open("requirements/dev.in", "w") as file:
        file.write("-c base.txt\n")
    process = subprocess.run(
        [".venv/bin/pip-compile", "-q", "-o", "requirements/dev.txt", "requirements/dev.in"]
    )
    process.check_returncode()
    #
    print("\U0001F389 The Python project is successfully initialized. \U0001F389")

if __name__ == "__main__":
    main()
