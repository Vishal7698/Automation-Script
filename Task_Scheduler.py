import schedule
import time
import datetime

def fun_miniute():
    print("curret time is")
    print(datetime.datetime.now())
    print("scheduler executer after minite")

def fun_hour():
    print("curret time is")
    print(datetime.datetime.now())
    print("scheduler executer after hours")

def fun_day():
    print("curret time is")
    print(datetime.datetime.now())
    print("scheduler executer after day")

def fun_Afternoon():
    print("curret time is")
    print(datetime.datetime.now())
    print("scheduler executer at specific time")

def main():
    print("python automation")

    print("python job scheduler")
    print(datetime.datetime.now())

    schedule.every(1).minute.do(fun_miniute)
    schedule.every().hour.do(fun_hour)
    schedule.every().day.at("01:30").do(fun_Afternoon)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()


