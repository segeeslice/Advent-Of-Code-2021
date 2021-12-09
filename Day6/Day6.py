#!/usr/bin/env python3

'''
Requirements:
~none~

My solutions:
Part 1: 389726
Part 2: ?
'''
import pprint
import copy
pp = pprint.PrettyPrinter(indent = 2)

# Formatted weirdly, can't be a YAML...
FISH_TIMER_DATA_PATH = './Day6ExampleData.txt'

MAX_TIMER = 6
MIN_TIMER = 0
NEWBORN_TIMER = 8

# == General-use ==

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

# == Program-specific ==

def parse_fish_timer_data(fish_timer_text):
    return [int(i) for i in fish_timer_text.split(',')]

def process_fish_timers_one_day(fish_timer_data):
    new_fish_timer_data = []

    for f in fish_timer_data:
        new_f = f - 1
        if new_f < MIN_TIMER:
            new_fish_timer_data.append(NEWBORN_TIMER)
            new_f = MAX_TIMER
        new_fish_timer_data.append(new_f)

    return new_fish_timer_data

def process_fish_timers(fish_timer_data, days):
    result = fish_timer_data
    for i in range(0, days):
        result = process_fish_timers_one_day(result)
    return result

def sum_fish_func(curr_day, fish_generation, days_per_fish, start_offset):
    sum_val = (curr_day + days_per_fish - start_offset - (days_per_fish + 2) * fish_generation) / days_per_fish
    # print ('1 + ' + str(sum_val))

    return int(max(sum_val, 0))

def reverse_fish_timers(fish_timer_data):
    return [MAX_TIMER - x for x in fish_timer_data]

def process_fish_timers(fish_timer_data, days):
    result = len(fish_timer_data)
    print(fish_timer_data)

    reversed_fish_timer_data = reverse_fish_timers(fish_timer_data)

    for start_offset in fish_timer_data:
        fish_generation = 0
        while True:
            inner_result = sum_fish_func(days, fish_generation, MAX_TIMER+1, start_offset+1)
            result += inner_result
            print(fish_generation, inner_result)
            if inner_result <= 0:
                break
            else:
                fish_generation += 1
        print('')

    return result

# == Main ==

def main ():
    raw_fish_timer_text = read_file_text(FISH_TIMER_DATA_PATH)
    fish_timer_data = parse_fish_timer_data(raw_fish_timer_text)

    # result = process_fish_timers(fish_timer_data, 80)
    # num_fish = len(result)

    num_fish = process_fish_timers(fish_timer_data, 80)
    print("Part 1:")
    print("Number of Fish: " + str(num_fish))

if __name__ == '__main__':
    main()
