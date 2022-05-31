import time
import threading


def main():
    for i in range(3):
        print("main:\t%d\n" % i)
        time.sleep(1)


def test():
    for i in range(3):
        print("test:\t%d\n" % i)
        time.sleep(0.5)


if __name__ == "__main__":
    # 启动子线程循环
    thread = threading.Thread(target=test)
    thread.start()

    # 启动主线程循环
    main()

    # 启动子线程循环 (被主线程阻塞)
    thread = threading.Thread(target=test)
    thread.start()