# The list of each EAS's with it's lowest latency obtained either with video compression or without,
# it's available resources (RAM and Computing Power), and a boolean notifying if latency was obtained 
# with compression or without

EAS_list = [[EAS_ID, latency, available_resources, video_type]]

# The detailed resources needs for each steps of the tasks schedule:
# tasks that can be executed in parallel belong to a unique step
# (which is a sublist)

Task_schedule = [[[task1, needs]],
                 [[task2A, needs], [task2B, needs]],
                 [[task3, needs]],
                 [[task4A, needs], [task4B, needs], [task4C, needs]],
                 [[task5A, needs], [task5B, needs]],
                 [[task6, needs]]]

# initiate a list that contains the destination EAS for each task
# (within each test)
Task_destination = []

# Multiply available resources by 0.8 for all EAS (security considerations)
for eas_info in EAS_list:
    eas_info[2] = eas_info[2]*0.8

# Get a sorted list of EAS by the lowest latency
EAS_list_sorted = EAS_list.sort(ascending, key = on latency)

def allocation_pseudo_algorithms(EAS_list_sorted, Task_Schedule, Task_destination):
    for step in Task_schedule:
        if (len(step) == 1): # if there is only 1 task to execute at this step
            Copy_EAS_sorted = EAS_list_sorted.copy()
            eas = 0
            while (step[1] > Copy_EAS_sorted[eas][2]): # while task needs > EAS's available resources
                eas += 1 # check if the EAS with next lowest latency got enough resources
            destination = Copy_EAS_sorted[eas][0]
            video_type = Copy_EAS_sorted[eas][3]
            Task_destination.append([step[0], destination, video_type])

        else: # if there is at least 2 tasks that can be executed in parallel
            for task in step:
                eas = 0
                while (task[1] > Copy_EAS_sorted[eas][2]):
                    eas += 1
                destination = Copy_EAS_sorted[eas][0]
                video_type = Copy_EAS_sorted[eas][3]
                Task_destination.append([task[0], destination, video_type])
    # the copy of EAS list has to be updated because the execution of the current 
    # studied task consumes resources
                Copy_EAS_sorted[eas][2] = Copy_EAS_sorted[eas][2] - task[1]
    return destination





