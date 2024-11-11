"""
Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""
 
class RandomizedSet:

    def __init__(self):
        #Orginally used a set add() and remove() have average O(1) problems arose with rand() set -> dicitonary
        self.internalDic = {}
        #Most list methods are O(n) so not ideal however we can use modulo and len to get random values at O(1)
        self.internalList = []

    
    def insert(self, val: int) -> bool:
        #the in method for dictionaries in python is O(n)
        if val in self.internalDic:
            return False
        else:
            #list method append and len are O(1)
            self.internalList.append(val)
            # offset for list starts at 0 not 1
            elementPosition = len(self.internalList) - 1
            self.internalDic[val] = elementPosition
            #print(f"current Dic = {self.internalDic} current List = {self.internalList}")
            return True

    def remove(self, val: int) -> bool:
        if val in self.internalDic:
            #Dicitonary lookup options are based on Hash-Tables so on average O(1) but can be O(n)
            removalElementPosition = self.internalDic.get(val)
            #list.pop() has O(1)
            finalElementPosition = len(self.internalList) - 1
            movedListValue = self.internalList[finalElementPosition]
            self.internalList[removalElementPosition] = movedListValue
            #removes duplicate of kept value at the end O(1)
            self.internalList.pop()
            #Also O(1)            
            self.internalDic.update({movedListValue: removalElementPosition})
            #Ran into issues when update was after deletion, would delete then recreate.
            del self.internalDic[val]
            #print(f"current Dic = {self.internalDic} current List = {self.internalList}")
            return True
        else:
            return False

    def getRandom(self) -> int:
        """Python random function is not secure and I assume is O(1) 
        randint uses randrange which uses _randBelow from the C library and is O(n), that took TOO long to find out
        random.random() seems to be the only O(1) easily verfied "random" code
        """

        #I tried to make this a clear as possible, if you find a more elegant AND O(1) solution let me know!
        #Generate value 0.0 <-> 1.0
        randomElement = random.random()
        #grab value somewhere in our list length, since it is percentage based in theory everything is approximately equally likely
        randomElement = (randomElement * len(self.internalList))
        randomElement = int(randomElement)
        #take that random value and look at direct location in list for O(1) which we cannot do with our dictionary
        #print(f"current Dic = {self.internalDic} current List = {self.internalList}")
        return self.internalList[randomElement]