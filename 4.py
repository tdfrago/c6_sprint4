from time import sleep
import random

#r.seed(42)

def get_random_number():
    return random.randint(1,5)

def delay(seconds):
    seconds=get_random_number()
    print(f"Sleeping for {seconds} seconds(s)")
    sleep(seconds)

def main():
    n=5
    for i in range(0,n):
        print(i)
        delay(seconds=2)

if __name__ == "__main__":
    main()