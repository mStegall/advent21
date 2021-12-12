with open('./data.txt') as f:
    lines = f.readlines()

routes = {}

for line in lines:
    [a,b] = line.strip().split('-')

    if not a in routes:
        routes[a] = []

    if not b in routes:
        routes[b] = []

    routes[a].append(b)
    routes[b].append(a)

def findRoutes(node, path,doubled):
    r = []
    
    for nextNode in routes[node]:
        newPath = path.copy()
        newPath.append(nextNode)
        if nextNode == 'end':
            r.append(newPath)
        elif nextNode.isupper():
            r.extend(findRoutes(nextNode, newPath, doubled))
        elif nextNode.islower() and nextNode not in path:
            r.extend(findRoutes(nextNode, newPath, doubled))
        elif nextNode.islower() and nextNode not in ['end','start'] and nextNode in path and not doubled:
            r.extend(findRoutes(nextNode, newPath, True))
    
    return r

def listRoutes():
    return findRoutes("start", ['start'], False)

print(len(listRoutes()))