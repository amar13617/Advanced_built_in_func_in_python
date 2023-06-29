def start_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf', 'Jose', 'Rans', 'Anna','Nith']
#stat_r = filter(start_with_r,(friends))
stat_r = filter(lambda x: x.startswith('R'),(friends))
#print(next(stat_r))
#print(next(stat_r)) #for loop works in background
print(list(stat_r)) #['Rolf', 'Rans']