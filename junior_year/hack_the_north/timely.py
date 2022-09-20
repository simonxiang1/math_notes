import math
import random

#dict of passenger <-> arrival hour
n = 2   #number of trains arriving per hour
k = 50  #capacity of each train
t = 30  #
d = 20

#dict mapping each hour of the day to estimated capacity (ML model). 
#this could also be a CSV. or it can be just a dict if we don't get the backend working
hours = {"zero": 20, "one": 45, "two": 100, "three": 154, "four": 675, "five": 1032, "six": 1201, "seven": 400, "eight": 201, "nine": 98, "ten": 303} 
num_to_letters = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

#THIS NEEDS TO BE WEIGHTED SO IT'S ONLY HALF RIGHT
# def wasted_time(n, k, t):
    # """n: number of trains arriving per hour
       # k: capacity of each train
        
       # Calculates the amount of time wasted. 
       # The goal is to minimize this value.
    # """

    # tot_wasted = 0

    # #minutes wasted is unserved people (hours[hour]-n*k) times 
    # #the amount of time it takes to make a single trip
    # for hour in hours:
        # tot_wasted += (hours[hour] - n * k) * t

    # return tot_wasted

def greed_train_assignment(d, n, k):
    """greed_train_assignment takes in some basic parameters and greedily
       decides how to allot all the extra trains. It works by sorting the
       dictionary of hours/capacities and sending a train to the highest 
       capacity timeslot iteratively.

       d: number of extra trains
       n: number of trains arriving per hour
       k: capacity of each train
    """
    
    while d > 0:
        #removes nk passengers from the most crowded train, updated for each d
        hours[list(dict(sorted(hours.items(), key=lambda \
                item: item[1], reverse = True)).keys())[0]] -= n * k
        #extra train is now full
        d -= 1
    return

def greed_passenger_assignment(h):
    """
       Takes in desired arrival time, returns departure train time.
       h: what hour the passenger wants to arrive at.
    """

    dep = h - 0.5 #departure time of desired train to arrive by h
    dep_hour = math.floor(dep) #departure hour
    dep_hour_people = hours[num_to_letters[dep_hour]] #crowd at departure hour

    #showing how many 30 minute intervals extra one would have to wait
    extra_wait_trains = []
    for i in range(0,10):
        extra_wait_trains.append((hours[num_to_letters[i]]  - n * k) // k)
    #no negative values
    for i in range(len(extra_wait_trains)):
        if extra_wait_trains[i] < 0:
            extra_wait_trains[i] = 0

    #print(extra_wait_trains)

    #case where hour works out based case)
    if dep_hour_people < n * k:
        #which half hour train to go on. case of 0n:30 train
        if h - dep_hour >= 1:
            return dep_hour + 0.5
        #case of 0n:00 train
        else:
            return dep_hour

    #have to loop backward through every hour starting from departure
    for i in range(1, math.floor(h)):
        #making you have to loop
        if (extra_wait_trains[dep_hour - 1]) >= (extra_wait_trains[dep_hour - 1 - i] + i):
            if hours[num_to_letters[dep_hour - i]] < (i+1) * n * k:

                #updates dict
                hours[num_to_letters[dep_hour]] -= 1
                hours[num_to_letters[dep_hour - i]] += 1
    
                #which half hour train to go on. case of 0n:30 train
                if h - dep_hour >= 1:
                    return dep_hour - i + 0.5
                #case of 0n:00 train
                else:
                    return dep_hour - i
        else:
            if h - dep_hour >= 1:
                return dep_hour + 0.5
            #case of 0n:00 train
            else:
                return dep_hour


def min_to_str(minutes):
    days = minutes // 1440
    hours = (minutes % 1440) // 60
    rem_min = minutes - days * 1440 - hours * 60

    formatted_string = str(days)+" days, "+str(hours)+" hours, and "+str(rem_min)+" minutes "
    return(formatted_string)




#making string for the buses.json file from input
gt = greed_passenger_assignment(4.3) 
if gt % 1 == 0:
    conv_time = str(int(gt))+":00PM\", \""+str(int(gt))+":30PM, \""+\
            str(int(gt+1))+":00PM\""
else:
    gt_m = gt - 0.5
    conv_time = str(int(gt_m))+":30PM\", \""+str(int(gt+1))+":00PM\", \""+str(int(gt+1))+":30PM\""

#writing to the .json file
busjs = open("buses.json", "w")
busjs.write("""{"buses": [
    {
        "num": 841,
        "times": [\"""")
busjs.write(conv_time)
busjs.write("""],
        "total": 50
    },
    {
        "num": 632,
        "times": ["7:30PM", "8:00PM", "8:30PM"],
        "total": 56
    },
    {
        "num": 344,
        "times": ["3:40PM", "4:10PM", "4:40PM"],
        "total": 48
    }
]}""")
busjs.close()

# print("Before,",min_to_str(wasted_time(n,k,t)),"were wasted.")

# for i in range(1000):
    # vari = random.uniform(0.5, 9.5)
    # print(vari)
    # greed_passenger_assignment(random.uniform(0.5,9.5))

# print("Now,",min_to_str(wasted_time(n,k,t)),"were wasted.")
