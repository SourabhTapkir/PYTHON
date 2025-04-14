#### List are Mutable #######


friend = ["Sourabh", "Tapkir", 11, 10.30, False, True, "Kothrud-Pune"]
print(friend) ## Displays Whole list
print(friend[0]) ## Display 0th index From the list

friend[0]= "Anil" ## Replacing 0th index  value sourabh To anil from the above list
print(friend) ## displaying the whole list (after Replacing)

friend.insert(7, "Single")## insert Function to insert the any of datatype in the list
print(friend)

print(friend[1:4])
print(20+20)