class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        plus = operations.count("X++") + operations.count("++X")
        x += plus
        x -= len(operations) - plus
        # for operation in operations:
        #     if operation == "++X" or operation == "X++":
        #         x += 1
        #     elif operation == "--X" or operation == "X--":
        #         x -= 1
        return x