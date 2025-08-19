import queue
import threading
import time


def worker(queue):
    while not queue.empty():
        task = queue.get()
        print(f"{threading.current_thread().name} processing: {task}")
        time.sleep(1)  # process simulation
        queue.task_done()


# Queue tasks
tasks = queue.Queue()


# Creat 5 threads
for i in range(5):
    tasks.put(f"Task {i+1}")


# Creating 2 threads to process queues
for _ in range(2):
    t = threading.Thread(target=worker, args=(tasks,))
    t.start()


tasks.join()  # Wait for all tasks to be processed
print("All the tasks are done")
