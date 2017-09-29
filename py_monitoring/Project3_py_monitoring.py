import psutil
import time
import collections


def sum(arr):
    sum = 0
    for val in arr:
        sum = sum + val
        return sum


def avg(arr):
    return sum(arr) / len(arr)


def print_system_stats():
    """ Function to print System status """

    cpu_percent_arr1 = collections.deque(maxlen=60)
    cpu_percent_arr5 = collections.deque(maxlen=300)
    cpu_percent_arr30 = collections.deque(maxlen=30)

    disk_usage_arr1 = collections.deque(maxlen=60)
    disk_usage_arr5 = collections.deque(maxlen=300)
    disk_usage_arr30 = collections.deque(maxlen=30)

    memory_total_arr1 = collections.deque(maxlen=60)
    memory_total_arr5 = collections.deque(maxlen=300)
    memory_total_arr30 = collections.deque(maxlen=30)

    time_start = 0

    while True:
        # interval =1 in our case
        cpu_percent = (psutil.cpu_percent(interval=1, percpu=False))
        # Logical = true, so that it shows all cores
        cpu_core = (psutil.cpu_count(logical=True))
        disk_usage = psutil.disk_usage('/').used
        memory_total = psutil.virtual_memory().total

        cpu_percent_arr30.append(cpu_percent)
        cpu_percent_arr5.append(cpu_percent)
        cpu_percent_arr1.append(cpu_percent)

        disk_usage_arr30.append(disk_usage)
        disk_usage_arr1.append(disk_usage)
        disk_usage_arr5.append(disk_usage)

        memory_total_arr30.append(memory_total)
        memory_total_arr1.append(memory_total)
        memory_total_arr5.append(memory_total)
        if time_start % 5 == 0:
            print ("\n")
            print "cpu_percent:" + str(cpu_percent)
            print "cpu_core:" + str(cpu_core)
            print "disk_usage:" + str(disk_usage)
            print "memory_total_RAM usage: " + str(memory_total/(1024*1024*1024)) + "GB"
            print ("\n")

            if cpu_percent_arr30.__len__() == 30:
                print "Average CPU usage in latest 30 sec:" + str(avg(cpu_percent_arr30))
                print "Average disk usage in latest 30 sec:" + str(avg(disk_usage_arr30))
                print "Average RAM usage in latest 30 sec:" + str(avg(memory_total_arr30)/(1024*1024*1024)) + "GB"
                print("\n")

            if cpu_percent_arr1.__len__() == 60:
                print "Average CPU usage in latest 1 minute:" + str(avg(cpu_percent_arr1))
                print "Average disk usage in latest 1 minute:" + str(avg(disk_usage_arr1))
                print "Average RAM usage in latest 1 minute:" + str(avg(memory_total_arr1)/(1024*1024*1024)) + "GB"
                print("\n")

            if cpu_percent_arr5.__len__() == 300:
                print "Average CPU usage in latest 5 minutes:" + str(avg(cpu_percent_arr5))
                print "Average disk usage in latest 5 minutes:" + str(avg(disk_usage_arr5))
                print "Average RAM usage in latest 5 minutes:" + str(avg(memory_total_arr5)/(1024*1024*1024)) + "GB"
                print("\n")

        time.sleep(1)
        time_start = time_start + 1


if __name__ == "__main__":
    print_system_stats()