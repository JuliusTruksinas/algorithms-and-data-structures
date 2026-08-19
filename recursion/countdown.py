def countdown(n: int) -> None:
    if(n < 0):
        return

    print(n)
    countdown(n-1)

countdown(10)