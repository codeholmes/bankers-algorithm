# Banker's algorithm implementation in Python

### The algorithm (`find_safe_sequence()` function) for finding the safe sequence:

1. Make a loop while the length of safe_seq_list is not equal to the no_of_job,
2. Inside the loop, make a for loop, so as to access keys (`job_name`) and values
   (`need_list`) over each iteration,
3. Make a `flag` (initialize it as `True` which means it resource needed is less than available CPU resources) for checking whether the resources is lesser or greater than available CPU resources.
4. Make another `for` loop, just to make sure the process (`job_name`) is not already in the safe_seq_list,
5. Check for the resources needed and available CPU available conditions if satisfy, pass it else make the `flag = False`
6. Outside `for` loop, check for `flag` status, if it is `True` , append the process (`job_name`) to the `safe_seq_list`.
   Update (`new_cpu_available`) the new CPU resources by adding the current process resources and available CPU resources.
   Also, delete the process (`job_name`) from the `res_need_dict_copy` dictionary, as the process is safe and has been added to the `safe_seq_list`.
7. Finally, outside `while` loop, print the safe sequence.
8. Run the above, recursively, till the `safe_seq_list` is equal to the `no_of_jobs`.

### Test case:

Run the program using: `python3 bankers.py`

CPU Resources:
Available: 2 1 0

Number of jobs: 5
Enter currentlly allocated resources for P0: 1 1 2
Enter currentlly allocated resources for P1: 2 1 2
Enter currentlly allocated resources for P2: 4 0 1
Enter currentlly allocated resources for P3: 0 2 0
Enter currentlly allocated resources for P4: 1 1 2

Current resources dict: {'P0': [1, 1, 2], 'P1': [2, 1, 2], 'P2': [4, 0, 1], 'P3': [0, 2, 0], 'P4': [1, 1, 2]}

Enter max resource for P0: 4 3 3
Enter max resource for P1: 3 2 2
Enter max resource for P2: 9 0 2
Enter max resource for P3: 7 5 3
Enter max resource for P4: 1 1 2

Resources needed dict: {'P0': [3, 2, 1], 'P1': [1, 1, 0], 'P2': [5, 0, 1], 'P3': [7, 3, 3], 'P4': [0, 0, 0]}

No safe sequence found!
New safe seq. added: ['P1']
No safe sequence found!
No safe sequence found!
New safe seq. added: ['P1', 'P4']
New safe seq. added: ['P1', 'P4', 'P0']
New safe seq. added: ['P1', 'P4', 'P0', 'P2']
New safe seq. added: ['P1', 'P4', 'P0', 'P2', 'P3']

Safe sequence: ['P1', 'P4', 'P0', 'P2', 'P3']
