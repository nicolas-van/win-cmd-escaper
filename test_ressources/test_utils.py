import os.path
import tempfile
import os
import shutil
import subprocess
import locale

echo_py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "echo.py"))

def run_echoer_with_cmd_through_script(str):
    tmp_folder = tempfile.mkdtemp()
    try:
        # create the bat file
        output_file_path = os.path.join(tmp_folder, "output.txt")
        cmd_file_content = f"""
python "{echo_py_path}" --file "{output_file_path}" -- {str}
"""
        cmd_file_name = os.path.join(tmp_folder, "echofile.bat")
        with open(cmd_file_name, 'w', encoding="utf-8") as f:
            f.write(cmd_file_content)

        # perform the call
        subprocess.check_call([cmd_file_name], stdout=subprocess.DEVNULL)

        # get the results
        with open(output_file_path, 'r', encoding="utf-8", newline='') as f:
            output_content = f.read()

        return output_content
    finally:
        shutil.rmtree(tmp_folder)

def run_echoer_with_cmd_through_python_subprocess(str):
    tmp_folder = tempfile.mkdtemp()
    try:
        # create the bat file
        output_file_path = os.path.join(tmp_folder, "output.txt")
        cmd = f'python "{echo_py_path}" --file "{output_file_path}" -- {str}'

        # perform the call
        subprocess.check_call(cmd, shell=True, stdout=subprocess.DEVNULL)

        # get the results
        with open(output_file_path, 'r', encoding="utf-8", newline='') as f:
            output_content = f.read()

        return output_content
    finally:
        shutil.rmtree(tmp_folder)


def __run_echoer_with_powershell_through_script_common(str, executable):
    tmp_folder = tempfile.mkdtemp()
    try:
        # create the bat file
        output_file_path = os.path.join(tmp_folder, "output.txt")
        cmd_file_content = f"""
python "{echo_py_path}" --file "{output_file_path}" -- {str}
"""
        cmd_file_name = os.path.join(tmp_folder, "echofile.ps1")
        with open(cmd_file_name, 'w', encoding="utf-8-sig") as f:
            f.write(cmd_file_content)

        # perform the call
        subprocess.check_call([executable, cmd_file_name], stdout=subprocess.DEVNULL)

        # get the results
        with open(output_file_path, 'r', encoding="utf-8", newline='') as f:
            output_content = f.read()

        return output_content
    finally:
        shutil.rmtree(tmp_folder)


def run_echoer_with_powershell_through_script(str):
    return __run_echoer_with_powershell_through_script_common(str, 'powershell')


def run_echoer_with_pwsh_through_script(str):
    return __run_echoer_with_powershell_through_script_common(str, 'powershell')