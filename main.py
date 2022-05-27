import time
start_time = time.time()
time_sleep = 1
print(start_time)
while True:
    for i in range(61):
        print("time :", time.time())
        time_sleep = float(time_sleep) - float(0.1)
        print("sleep :",time_sleep)
        print("second :", i)
        time.sleep(time_sleep)
        if i == 60 :
            exit()
