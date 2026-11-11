def main():
    items = []
    for i in range(3):
        items.append(lambda: i)
    for f in items:
        print(f())


main()
