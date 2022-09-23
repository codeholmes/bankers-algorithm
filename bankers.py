# Author: codeholmes

import numpy as np


class Bankers:
    def __init__(self) -> None:
        self.res_need_dict = {}
        self.cpu_available = []
        self.new_cpu_available = []
        self.safe_seq_list = []
        self.res_need_dict_copy = {}
        self.new_cpu_available = []

    # cpu resources assignment
    def assign_cpu_resources(self) -> None:
        print("CPU Resources:")
        # self.cpu_total = input("Total: ").split()
        self.cpu_available = [int(e) for e in input("Available: ").split()]
        self.new_cpu_available = self.cpu_available.copy()

    # add currently allocated resources
    def curr_allocated_resources(self) -> None:
        self.curr_res = []
        self.curr_res_dict = {}
        self.no_of_jobs = int(input("\nNumber of jobs: "))
        for i in range(self.no_of_jobs):
            self.add_curr_res = [
                int(e)
                for e in input(
                    "Enter currentlly allocated resources for P{job}: ".format(job=i)
                ).split()
            ]
            self.curr_res.append(self.add_curr_res)
            self.curr_res_dict.update({"P{job}".format(job=i): self.add_curr_res})

        # print("\nCurrent resources:", self.curr_res)
        print("\nCurrent resources dict:", self.curr_res_dict, "\n")

    # add maximum resources for each processes in the same sequence
    def max_resources(self) -> None:
        self.max_res = []
        self.max_res_dict = {}
        for i in range(self.no_of_jobs):
            self.add_max_res = [
                int(e)
                for e in input("Enter max resource for P{job}: ".format(job=i)).split()
            ]
            self.max_res.append(self.add_max_res)
            self.max_res_dict.update({"P{job}".format(job=i): self.add_max_res})

    # fn to calculate the resources needed by the each process
    def calculate_resource_need(self) -> None:
        self.curr_res_arr = np.array(self.curr_res)
        self.max_res_arr = np.array(self.max_res)
        self.res_need = [
            list(e) for e in np.subtract(self.max_res_arr, self.curr_res_arr)
        ]
        # print("\nResources needed", self.res_need)

        for i in range(len(self.res_need)):
            self.res_need_dict.update({"P{job}".format(job=i): self.res_need[i]})
        print("\nResources needed dict:", self.res_need_dict, "\n")

        self.res_need_dict_copy = self.res_need_dict.copy()

    # core algorithm to find the safe sequence
    def find_safe_sequence(self):
        while len(self.safe_seq_list) != self.no_of_jobs:
            for job_name, need_list in self.res_need_dict.items():
                self.flag = True
                if job_name not in self.safe_seq_list:
                    for i in range(len(need_list)):
                        if not (int(need_list[i]) <= int(self.new_cpu_available[i])):
                            #     pass
                            # else:
                            self.flag = False
                    if self.flag is True:
                        self.safe_seq_list.append(job_name)
                        self.new_cpu_available = list(
                            np.add(
                                np.array(self.new_cpu_available),
                                np.array(self.curr_res_dict[job_name]),
                            )
                        )
                        del self.res_need_dict_copy[job_name]
                        print("New safe seq. added:", self.safe_seq_list)
                    else:
                        print("No safe sequence found!")

        print("\nSafe sequence: ", self.safe_seq_list)

    # here using recursion
    # to run the above core fn
    # till the safe seq. list is equal to the no. of jobs.
    def check_for_sequence(self):
        while len(self.safe_seq_list) != self.no_of_jobs:
            self.find_safe_sequence()


bk = Bankers()
bk.assign_cpu_resources()
bk.curr_allocated_resources()
bk.max_resources()
bk.calculate_resource_need()
bk.check_for_sequence()
