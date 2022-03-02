import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--value',
        type=int, 
    )
    args = parser.parse_args()
    time.sleep(args.value)
    print(f"I finish {args.value}")
