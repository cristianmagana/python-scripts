# Can iterator over list, tuple, string the same

x = ["one","two","three","four","five"]

for i in x:
    print(x)

# iterate over dict

d = {'xyz': 123, 'abc': 345}
for i in d :
    print("%s  %d" %(i, d[i]))


# While loops
 
iterable_value = "TEST-THIS"
iterable_obj = iter(iterable_value)
 
while True:
    try:
 
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
 
        # exception will happen when iteration will over
        break
