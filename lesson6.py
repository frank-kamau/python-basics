#list
scores = [90, 65, 45, 32, 71, 87,48, 62]

#access a value
print(scores[0]) #first
print(scores[2]) #third

#add
scores.append(61)
print(scores)

#remove
scores.pop(3)
print(scores)

scores.sort(reverse=True)
print(scores)
print(len(scores))
