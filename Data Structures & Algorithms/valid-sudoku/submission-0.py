class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # make a map for rows and we set the key from row 1-9 and save the entire row and values we keep in them     

        res = defaultdict(list)
        rows = defaultdict(list)
        cols = defaultdict(list)
        index = 0
        # save every row to hashmap with key 1-9
        for strs in board:
            rows[index] = strs
            index += 1
        # save every col to map with key 1-9
        columnNumber = 0
        index = 0
        while columnNumber <= 8:
            for strs in board:
                cols[columnNumber].append(strs[index])
            columnNumber += 1
            index += 1
        
        # we can now check a whole column and a row for numbers
        # now to see whats in the boxes 
        boxes = defaultdict(list)
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                box_index = (row // 3) * 3 + (col // 3)
                boxes[box_index].append(val)
        
        # go through row col and boxes to make sure no numbers come more than once ignore '.'
        # row = [1 2 . . 3 . . . .]
        # col = [1 4 . 5 . 7 . . .]
        # box = [1 2 . 4 . . . 9 1]

        # check rows
        seen = set()
        for row in rows.values():
            for num in row:
                if num == '.':
                    pass
                elif num not in seen:
                    seen.add(num)
                elif num in seen:
                    return False
            seen.clear()

        # check cols
        seen.clear()
        for col in cols.values():
            for num in col:
                 if num == '.':
                    pass
                 elif num not in seen:
                    seen.add(num)
                 elif num in seen:
                    return False
            seen.clear()

        # check boxes
        seen.clear()
        for box in boxes.values():
            for num in box:
                 if num == '.':
                    pass
                 elif num not in seen:
                    seen.add(num)
                 elif num in seen:
                    return False
            seen.clear()
        return True

             