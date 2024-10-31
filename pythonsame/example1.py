nested_list =[[2,3,4],[5,6,[7,8]],[9,11]]
nested_element =nested_list[1][2][1]
nested_list[2][1] =10

flattened_list =[element for sublist in nested_list for item in sublist for
element in (item if isinstance(item,list) else [item])]

print('Nested Element : ', nested_element)
print(" Modified Nested  List :", nested_list)
print("Flattened List : ", flattened_list)



