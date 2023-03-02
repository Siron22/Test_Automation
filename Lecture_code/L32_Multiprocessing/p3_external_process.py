import os
# os.system("sleep 2")
# code = os.system("ls -la")
# print(f"Q{code}Q")


import subprocess

# output = subprocess.run(['ls', '-la'])
# print(output)

# output = subprocess.run(['ls', '-la'], capture_output=True)
# #print(output)
# #print(output.stdout)
# print(output.stdout.decode())
# print(output.returncode)

# output = subprocess.run(['ls', '-la'], capture_output=True, text=True)
# #print(output)
# #print(output.stdout)
# print(output.stdout)
# print(output.returncode)

# with open("output.log", 'w') as f:
#     output = subprocess.run(['bash', 'script.sh'], stdout=f)
# print(output.stdout)

# output = subprocess.run(['python3', 'input_example.py'], capture_output=True, input=b'5')
# print(output)
# print(output.stdout)

import time
# output = subprocess.run(['bash', 'script.sh'], capture_output=True, text=True)
# for i in range(5):
#     print(f"In main: {i}")
#     time.sleep(0.6)


process = subprocess.Popen(['bash', 'script.sh'])
process.communicate(timeout=2)
for i in range(5):
    print(f"In main: {i}")
    time.sleep(0.6)

os.popen()
os.listdir(directory)
@pytes.fixture
def application():
    subprocess.Popen(['docker', 'run', 'image'])
    yield
    id = subprocess.run(['docker', 'ps'])
    subprocess.Popen(['docker', 'stop', id])