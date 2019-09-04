import sys

def test():
    try:
        1 / 0
    except Exception:
        print(">>>>>>>>>")

    print("1111111111")
    print(sys.version)


if __name__ == "__main__":
    test()
