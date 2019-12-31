"""Explore Queues and Stacks by checking for palindromes."""

class Solution:
    """Solution class creates, populates and emptys a stack and queue."""

    def __init__(self):
        """Initialise the queue and stack (as a double ended queue)."""
        self.my_q = list()
        self.my_stack = list()

    def push_character(self, char):
        """Append to the stack."""
        self.my_stack.append(char)

    def enqueue_character(self, char):
        """Append to the queue."""
        self.my_q.append(char)

    def pop_character(self):
        """Pop off the end of the stack."""
        return self.my_stack.pop()

    def dequeue_character(self):
        """Dequeue the first entry into the queue."""
        return self.my_q.pop(0)

if __name__ == "__main__":
    # read the string s
    S = input()
    #Create the Solution class object
    OBJ = Solution()

    L = len(S)
    # push/enqueue all the characters of string s to stack
    for i in range(L):
        OBJ.push_character(S[i])
        OBJ.enqueue_character(S[i])

    IS_PALINDROME = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(L // 2):
        if OBJ.pop_character() != OBJ.dequeue_character():
            IS_PALINDROME = False
            break
    #finally print whether string s is palindrome or not.
    if IS_PALINDROME:
        print("The word, " + S + ", is a palindrome.")
    else:
        print("The word, " + S + ", is not a palindrome.")
