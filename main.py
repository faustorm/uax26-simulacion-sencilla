import time
step_count = 0
def step(seconds = 3):
    global step_count
    time.sleep(3)
    step_count += 1
    print(f"Step: {step_count}, cada step toma {seconds} segs")

while step_count <= 1000:
    step()