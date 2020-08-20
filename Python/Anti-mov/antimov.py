# Anti-"mov" v0.1
import subprocess
import string
import os.path

def mov_argv_brute(target_file:str, charset: list = string.printable, exec: bool = False, sys_type: str = "linux"):
    # File check
    if not os.path.exists(target_file):
        print("Error: File Not Found")
        return

    # Variables
    flag = ''
    command = "perf stat -x : -e instructions:u " + target_file

    # Command Updates
    def update_command(): # With added char
        return command + " " + flag + i + "1>/dev/null"

    def print_flag_command(): # As is
        return target_file + " " + flag

    # Brute force loop
    while True:
        ins_count = 0
        count_chr = ''
        for i in charset:
            if sys_type.lower() == "linux":
                if i == "\'":
                    i = "\\\'"
                else:
                    i = '\'' + i + '\''
            else:
                i = '\'' + i + '\''
            cmd_updated = update_command()
            target_process = subprocess.Popen(cmd_updated,
                                              stdout=subprocess.PIPE,
                                              stdin=subprocess.PIPE,
                                              stderr=subprocess.STDOUT,
                                              shell=True)

            # Filter out the instruction count
            result = target_process.stdout.read().decode("utf-8")
            result = result.split(":")

            # Pull count and set char if greater
            instructions = int(result[0])
            if instructions > ins_count:
                count_chr = i
                ins_count = instructions
        flag += count_chr
        print(ins_count)
        print(flag)
        # Optional Run Check if exec == true
        if exec:
            exec_process = subprocess.Popen(print_flag_command(),
                                              stdout=subprocess.PIPE,
                                              stdin=subprocess.PIPE,
                                              stderr=subprocess.STDOUT,
                                              shell=True)
            print(exec_process.stdout.read().decode("utf-8"))
