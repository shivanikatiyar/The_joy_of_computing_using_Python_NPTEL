#We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#Input-->abracadabra
# 5 k
#Sample Output---> abrackdabra

def mutate_string(string, position, character):
    list1=list(string)    #  convert string to list
    list1[position]=character
    return''.join(list1)    # Uses ''.join(list_name) function ---->convert list to string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
