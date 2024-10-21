# YOUR CODE HERE
n = int(input())
lst1 = []
lst2 = []
for i in range(n):
    user_input = int(input())
    lst1.append(user_input)
for i in range(n):
    user_input = int(input())
    lst2.append(user_input)
summarize = []
def summation(n):
    for i in range(n):
        summarize.append(lst1[i]+lst2[i])
    return summarize 
def find_min_max():
    min = summarize[0]
    max = summarize[0]
    for i in range (len(summarize)):
        if summarize[i] > max:
            max = summarize[i]
        elif summarize[i] < min:
            min = summarize[i]
    return min,max

print(summation(n))
print(find_min_max())
