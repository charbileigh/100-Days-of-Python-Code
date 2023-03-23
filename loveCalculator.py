# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

true_sum = 0

for i in "true":
    true_sum += name1.count(i) + name2.count(i)

count = 0
for j in "love":
    count += name1.count(j) + name2.count(j)


adding = str(true_sum) + str(count)
add = int(adding)


if (add < 10 or add > 90):
    print(f"Your score is {add}, you go together like coke and mentos.")
elif (add > 40 and add < 50):
    print(f"Your score is {add}, you are alright together.")
else:
    print(f"Your score is {add}.")



