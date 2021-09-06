heights = []
add = 0
count = 0
student_heights = input("enter a list of student heights ").split()
for n in range(0, len(student_heights)):
    heights.append(int(student_heights[n]))


# for i in heights:
#     add += i
#     count += 1       # in place of len function to count the number of elements in the list
# avg_heights = add / count
# print(add)
# print(count)
# print(round(avg_heights))


# maxim = 0
# for i in range(len(heights)-1):   to find the maximum out of a list
#     if heights[i] > heights[i+1]:
#         maxim = heights[i]
#         heights[i] = heights[i+1]
#         heights[i+1] = maxim
# print(maxim)


highest_score = 0
for score in heights:
    if score > highest_score:
        highest_score = score
print("the highest score in the class is {}".format(highest_score))




