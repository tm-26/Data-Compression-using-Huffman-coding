import heapq
import sys
from os import path

if __name__ == "__main__":
    # Handling input
    fileLocation = ""
    if len(sys.argv) == 2:
        fileLocation = sys.argv[1]
    else:
        print("Enter the path to an ASCII text file to show it's coding table:", end=" ")
        fileLocation = input().strip()
    # Variable Declaration
    characters = {}
    # Validate file
    if path.exists(fileLocation):
        file = open(fileLocation, "r")
        for char in file.read():
            # Validate input
            if not (char.isdigit() or char.isalpha()):
                print("An error has occurred: Entered file contains an illegal character (" + char + ")")
                exit()
            # Create dictionary, with characters as keys and count as values
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        # Create heap
        heap = [[value, [key, '']] for key, value in characters.items()]
        heapq.heapify(heap)
        # While heap has more then then 1 node
        while len(heap) > 1:
            # Get the two nodes with the lowest count
            min1 = heapq.heappop(heap)
            min2 = heapq.heappop(heap)
            for node in min1[1:]:
                node[1] = '0' + node[1]
            for node in min2[1:]:
                node[1] = '1' + node[1]
            # Push new node with count = min1[count] + min2[count]
            heapq.heappush(heap, [min1[0] + min2[0]] + min1[1:] + min2[1:])
        # Sort the heap by ASCII values
        heap = sorted(heapq.heappop(heap)[1:])
        characters = {key: value for key, value in sorted(characters.items(), key=lambda i: i[1], reverse=True)}

        print(characters)
        print("Coding table")
        for node in heap:
            print(node[0] + ": " + node[1])

    else:
        print("An error has occurred: Entered file does not exist")
