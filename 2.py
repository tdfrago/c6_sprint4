from time import sleep

def delay(seconds):
    print(f"Sleeping for {seconds} seconds(s)")
    sleep(seconds)

def main():
    n=5
    for i in range(0,n):
        print(i)
        delay(seconds=2)

if __name__ == "__main__":
    main()