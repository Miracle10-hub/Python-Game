# YouTube Views Analyzer - student style
def main():
    views = []
    while True:
        try:
            v = int(input('Enter daily views for a day (or -1 to stop): '))
            if v == -1:
                break
            if v < 0:
                print('Views must be 0 or more.')
                continue
            views.append(v)
        except ValueError:
            print('Enter an integer.')
    if not views:
        print('No views entered.')
        return
    print('Views:', views)
    print('Highest:', max(views))
    print('Lowest:', min(views))
    print('Average:', sum(views)/len(views))
if __name__ == '__main__':
    main()
