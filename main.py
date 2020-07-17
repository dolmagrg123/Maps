#map
#Iterated function run on every element within a sequence

new_list = list(range(5))
print(new_list)

new_list1 = ["apple", "banana", "cherry", "mango"]


def get_length(word):
  return len(word)

def extend_list(word):
  return word + 's'

#result=map(get_length, new_list1)
#print(type(result))
#print(list(result))

result=list(map(get_length,new_list1))
print (result)

result1 = list(map(extend_list, new_list1))
print(result1)