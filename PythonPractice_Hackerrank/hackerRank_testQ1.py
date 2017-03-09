import sys
import os

def melon_count(boxes,melons):
    total_packed = 0
    boxes = [int(x) for x in boxes]
    melons = [int(x) for x in melons]

    melon_max = max(melons)
    box_max = max(boxes)

    #FIND STARTING POINT
    #pos_maxmelons contains position of all melons while arranged in descending order
    pos_maxmelons = []
    for size in sorted(melons,reverse=True):
        pos_maxmelons.append(melons.index(size))

    #length_betweenmelons holds the difference between the two positions
    length_betweenmelons = []
    for idx,pos in enumerate(pos_maxmelons):
        if pos_maxmelons.index(pos) == 0:
            length_betweenmelons.append(len(melons) - pos)
        else:
            length_betweenmelons.append(pos_maxmelons[idx-1] - pos)

    #start where the element has the max difference with itself and previous biggest

    #print(length_betweenmelons)
    maxDiff = 0
    startingPosition = len(melons)
    for idx,length in enumerate(sorted(length_betweenmelons,reverse=True)):
        #print("Length is {0}".format(length))
        if length >= maxDiff:
            #print("Yes it is greater")
            if startingPosition > pos_maxmelons[idx] and melons[pos_maxmelons[idx]] <= box_max:
                startingPosition = pos_maxmelons[idx]
                maxDiff = length
                print("New Starting Position {0}".format(startingPosition))
                print("New MaxDiff {0}".format(maxDiff))
        elif length < maxDiff:
            break

    print(startingPosition)
        #PLACE THE MELONS
    box_ordered = sorted(boxes)

    for melon_size in melons[startingPosition:]:
        packed = False
        for idx,box_size in enumerate(box_ordered):
            if melon_size<= box_size:
                box_ordered[idx] = -1
                packed = True
                total_packed += 1
                break

        if packed == False:
            break
    print(total_packed)



script,boxes,melons = sys.argv
boxes = boxes.split(' ')
melons = melons.split(' ')
melon_count(boxes,melons)
