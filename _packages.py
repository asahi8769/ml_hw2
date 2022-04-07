from subprocess import Popen, PIPE
import os

VENV_64_DIR = os.path.join(os.getcwd(), 'venv')
SCRIPTS_DIR = os.path.join(VENV_64_DIR, 'Scripts')


def subprocess_cmd(command):
    print(command)
    try :
        process = Popen(command, stdout=PIPE, shell=True, universal_newlines=True)
        proc_stdout = process.communicate()[0].strip()
    except Exception as e:
        process = Popen(command, stdout=PIPE, shell=True, universal_newlines=False)
        proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


def install(lib):
    return f'pip --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install {lib}'


def force_reinstall(lib):
    return f'pip --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install ' \
           f'"{lib}" --force-reinstall'


if __name__ == "__main__":
    subprocess_cmd(rf'cd {SCRIPTS_DIR} && python -m venv {SCRIPTS_DIR} && activate')
    subprocess_cmd(f'cd {SCRIPTS_DIR} && {install("pandas")}')
    subprocess_cmd(f'cd {SCRIPTS_DIR} && {install("numpy")}')
    subprocess_cmd(f'cd {SCRIPTS_DIR} & {install("xlrd")}')
    subprocess_cmd(f'cd {SCRIPTS_DIR} & {install("matplotlib")}')
    subprocess_cmd(f'cd {SCRIPTS_DIR} & {install("seaborn")}')
    subprocess_cmd(f'cd {SCRIPTS_DIR} & {install("sklearn")}')



