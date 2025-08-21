import threading
import time
import multiprocessing
import asyncio

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def task(args):
    print(f"{YELLOW}Task started: {args}{RESET}")
    time.sleep(2)
    print(f"{GREEN}Task finished: {args}{RESET}")

async def threadingTasks():
    threads = []
    for i in range(3):
        thread = threading.Thread(target=task, args=(f"thread: {i}",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

async def multiprocessingTasks():
    with multiprocessing.Pool() as pool:
        args = [f"multiprocessing: {i}" for i in range(3)]
        results = pool.map(task, args)
        print(results)

async def main():
    print(f"--- Main thread started ---")
    await threadingTasks()
    print(f"--- Main thread finished ---")
    print(f"--- Main process started ---")
    await multiprocessingTasks()
    print(f"--- Main process finished ---")


if __name__ == "__main__":
   asyncio.run(main())

   