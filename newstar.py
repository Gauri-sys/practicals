
import heapq
import itertools

def h(s,g):
    p={g[i][j]:(i,j) for i in range(3) for j in range(3)}
    return sum(abs(i-p[s[i][j]][0])+abs(j-p[s[i][j]][1])
               for i in range(3) for j in range(3) if s[i][j])

def show(s):
    print("+---+---+---+")
    for r in s:
        print("|"+"".join(f" {x} |" if x else "   |" for x in r))
        print("+---+---+---+")

def moves(s):
    x,y=next((i,j) for i in range(3) for j in range(3) if s[i][j]==0)
    for dx,dy,m in [(-1,0,"DOWN"),(1,0,"UP"),(0,-1,"RIGHT"),(0,1,"LEFT")]:
        a,b=x+dx,y+dy
        if 0<=a<3 and 0<=b<3:
            n=[r[:] for r in s]
            t=n[a][b]
            n[x][y],n[a][b]=n[a][b],n[x][y]
            yield n,t,m

def key(s):
    return tuple(map(tuple,s))

def astar(start,goal):
    c=itertools.count()
    pq=[(h(start,goal),0,next(c),start,[(start,0,0,"Initial")])]
    best={}

    while pq:
        f,g,_,s,path=heapq.heappop(pq)
        k=key(s)
        if k in best and best[k]<=g: continue
        best[k]=g

        print("\n================ CURRENT STATE ================")
        print(f"g={g} h={h(s,goal)} f={f}")
        show(s)

        if s==goal:
            print("\n================ SOLUTION PATH ================")
            for i,(s,g,t,m) in enumerate(path):
                print(f"\nStep {i}: {m}" if i==0 else f"\nStep {i}: Tile {t} moved {m}")
                print(f"g={g} h={h(s,goal)} f={g+h(s,goal)}")
                show(s)
            print("\nGoal State Reached!")
            print("Total Moves =",len(path)-1)
            return

        ch=[]
        for n,t,m in moves(s):
            cg=g+1
            cf=cg+h(n,goal)
            ch.append((cf,cg,n,t,m))

        print("\n================ ALL POSSIBLE CHILDREN ================")
        for i,(cf,cg,n,t,m) in enumerate(ch,1):
            print(f"\nCHILD {i}: Tile {t} moved {m}")
            print(f"g={cg} h={h(n,goal)} f={cf}")
            show(n)

        if ch:
            b=min(ch,key=lambda x:(x[0],x[1]))
            child_no = ch.index(b) + 1
            
            print("\n================ BEST SELECTED ================")
            print(f"Selected: CHILD {child_no}")
            print(f"Tile {b[3]} moved {b[4]}")
            print(f"g={b[1]} h={h(b[2],goal)} f={b[0]}")
            show(b[2])

        for cf,cg,n,t,m in ch:
            if key(n) not in best or cg<best[key(n)]:
                heapq.heappush(pq,(cf,cg,next(c),n,
                                   path+[(n,cg,t,m)]))

    print("No Solution Found")

print("========== 8 PUZZLE USING A* SEARCH ==========")
print("\nEnter Initial State (0 = Blank)")
start=[list(map(int,input(f"Row {i+1}: ").split())) for i in range(3)]

print("\nEnter Goal State")
goal=[list(map(int,input(f"Row {i+1}: ").split())) for i in range(3)]

print("\nINITIAL STATE")
show(start)
print("\nGOAL STATE")
show(goal)
print("\nf(n) = g(n) + h(n)")
print("h(n) = Manhattan Distance")

astar(start,goal)
