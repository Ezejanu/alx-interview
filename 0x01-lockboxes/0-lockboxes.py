#!/usr/bin/python3
'''a method that determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''a method that determines if all the boxes can be opened'''

    if not boxes:
        return False

    opened_boxes = set()
    '''Set to keep track of opened boxes'''

    def dfs(box):
        '''a recursive function to perform depth-first search(DFS)
        apprroach to open boxes'''

        opened_boxes.add(box)

        for key in boxes[box]:
            ''' If the key corresponds to an unopened box and is within
            valid range, recursively open that box'''
            if key not in opened_boxes and 0 <= key < len(boxes):
                dfs(key)

    dfs(0)
    '''start DFS from the first box (boxes[0])'''

    return len(opened_boxes) == len(boxes)
