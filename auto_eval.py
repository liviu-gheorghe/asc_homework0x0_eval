import subprocess


tl_ids = list(map(int, input("Introdu numarul probelemor pe care doresti sa le testezi (ex 1 2 3 4 daca vrei sa le testezi pe toate):").split()))
tasks = [{'id':i, 'exec_file': 'cerinta{}'.format(i), 'tests_file': 'cerinta{}_teste.txt'.format(i)} for i in tl_ids]


for task in tasks:

    tests_file = open(task['tests_file'], 'r')
    lines = tests_file.readlines()
    lines = [{'input': lines[t].strip(), 'output': lines[t+1].strip()} for t in range(0,len(lines),3)]
    for line in lines:
        expected_output = line['output']
        taskProcess = subprocess.run(['./' + task['exec_file']], stdout=subprocess.PIPE, input = line['input'], encoding = 'ascii')
        process_output = taskProcess.stdout
        process_output = process_output.strip()
        if expected_output == process_output:
            print("Success")
        else:

            print("Test failed for problem no. {}, (input was {})".format(task['id'], line['input']))
            print("Expected output is {}, actual output is {}".format(expected_output, process_output))
