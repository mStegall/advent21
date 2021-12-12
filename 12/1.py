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

def findRoutes(node, path):
    r = []
    
    for nextNode in routes[node]:
        newPath = path.copy()
        newPath.append(nextNode)
        if nextNode == 'end':
            r.append(newPath)
        elif nextNode.isupper():
            r.extend(findRoutes(nextNode, newPath))
        elif nextNode.islower() and nextNode not in path:
            r.extend(findRoutes(nextNode, newPath))
    
    return r

def listRoutes():
    return findRoutes("start", ['start'])

print(len(listRoutes()))