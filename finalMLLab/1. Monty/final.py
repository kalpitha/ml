import argparse, random      
def simulate(num_doors, switch, steps):

    winning_door = random.randint(0, num_doors-1)
    if steps:
        print('Prize is behind door {}'.format(winning_door+1))

    choice = random.randint(0, num_doors-1)
    if steps:
        print('Contestant chooses door {}'.format(choice+1))

    closed_doors = list(range(num_doors))
    while len(closed_doors) > 2:
        door_to_remove = random.choice(closed_doors)
        if door_to_remove == winning_door or door_to_remove == choice:
            continue
        assert(winning_door >=0 and winning_door <= num_doors-1 ),"winning door illegal"
        assert(choice >=0 and choice <= num_doors -1 ),"winning door illegal"
        closed_doors.remove(door_to_remove)
        if steps:
            print('Host opens door {}'.format(door_to_remove+1))
            
    if switch:
        if steps:
            print('Contestant switches from door {} '.format(choice+1))
        available_doors = list(closed_doors) # Make a copy of the list.
        available_doors.remove(choice)
        choice = available_doors.pop()

        if steps:
            print('to {}'.format(choice+1))

    assert(len(closed_doors)==2),"no of doors to choose from is not 2"
    won = (choice == winning_door)
    if steps:
        if won:
            print('Contestant WON')
        else:
            print('Contestant LOST')
    return won

def main():

    parser = argparse.ArgumentParser(description='simulate the Monty Hall problem')

    parser.add_argument('--doors', default=2, type=int, metavar='int',help='number of doors offered to the contestant')

    parser.add_argument('--trials', default=100, type=int, metavar='int',help='number of trials to perform')

    parser.add_argument('--steps', default=True, action='store_true',help='display the results of each trial')

    args = parser.parse_args()

    print('Simulating {} trials...'.format(args.trials))

    winning_non_switchers = 0

    winning_switchers = 0

    for i in range(args.trials):
        won = simulate(args.doors, switch=False, steps=args.steps)
        if won:
            winning_non_switchers += 1
        won = simulate(args.doors, switch=True, steps=args.steps)
        if won:
            winning_switchers += 1

    print('    Switching won {0:5} times out of {1} ({2}% of the time)'.format(

            winning_switchers, args.trials,

            (winning_switchers / args.trials * 100 ) ))

    print('Not switching won {0:5} times out of {1} ({2}% of the time)'.format(

            winning_non_switchers, args.trials,

            (winning_non_switchers / args.trials * 100 ) ))


if __name__ == '__main__':

    main()
