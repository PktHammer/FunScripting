# Anti-"mov" v0.2a -- In Progress
# Thanks to dustri.org @ https://dustri.org/b/defeating-the-recons-movfuscator-crackme.html
import subprocess
import string
import os.path


def mov_brute(target_file: str,
                charset: str = string.printable,
                exec: bool = False,
                sys_type: str = "linux",
                comm: str = "argv",
                comm_buf: list = None):
    # File check
    if not os.path.exists(target_file):
        print("Error: File Not Found")
        return

    # Variables
    flag = ''
    command = "perf stat -x : -e instructions:u " + target_file

    # Command Updates
    def print_flag_command():  # As is
        return target_file + " " + flag
    if comm == "communicate":
        while True:
            instructions_max = 0
            chr_max = ''
            if comm_buf is None:
                active_buf = []
            for i in string.printable:
                # Open Process
                target_process = subprocess.Popen(command,
                                                  stdout=subprocess.PIPE,
                                                  stdin=subprocess.PIPE,
                                                  stderr=subprocess.STDOUT,
                                                  shell=True)
                # Execute Buf
                for item in comm_buf:  # Apparently no binary fstrings :(
                    stdout, stderr = target_process.communicate(input=b'%s\n' % item)
                # Execute flagstring
                stdout, stderr = target_process.communicate(input=b'%s\n' % (flag + i))
                num_instructions = int(target_process.stdout.read().decode("utf-8").split(":")[0])
                if num_instructions > instructions_max:
                    instructions_max = num_instructions
                    chr_max = i
            flag += chr_max
            print(instructions_max)
            print(flag)

    if comm == "argv":
        def update_command():  # With added char
            return command + " " + flag + i + "1>/dev/null"
        # Brute force loop
        while True:
            ins_count = 0
            chr_max = ''
            for i in charset:
                if sys_type.lower() == "linux":
                    if i == "\'":
                        i = "\\\'"
                    else:
                        i = '\'' + i + '\''
                else:
                    print("Err: Unsupported OS")
                    return
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
                    chr_max = i
                    ins_count = instructions
            flag += chr_max
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
