N = int(input())
petrol = list(map(int, input().split()))
distance = list(map(int, input().split()))

def gasStation(petrol, distance):
    station = remain = 0

    for i in range(N): #loop through each station
        remain += petrol[i] - distance[i] #Check the remaining petrol

        if remain < 0: #in case run out of petrol
            remain = 0
            station = i + 1

    return station

print(gasStation(petrol, distance))