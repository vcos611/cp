'''You are given two positive integers N and K, where K≤N. Find a
sequence A1,A2,…,AN such that:

for each valid i, Ai is either i or −i
there are exactly K values of i such that 1≤i≤N and A1+A2+…+Ai>0

If there are multiple solutions, you may print any one of them. It can
be proved that at least one solution always exists.

Input
The first line of the input contains a single integer T denoting the
number of test cases. The description of T test cases follows. The first
and only line of each test case contains two space-separated integers N
and K.

Output
For each test case, print a single line containing N space-separated
integers A1,A2,…,AN.

Constraints
1≤T≤1,000
1≤K≤N≤1,000
Subtasks
Subtask #1 (10 points): N≤10
Subtask #2 (90 points): original constraints

Example Input
1
3 3
Example Output
1 2 3'''

t = int(input())
n,k = [],[]
for y in range(t):
    n1,k1 = list(map(int,input().split()))
    n.append(n1)
    k.append(k1)

for y in range(0,t):
    pos1,pos2 = list(range(0,n[y],2)),list(range(1,n[y],2))
    pos2.reverse()
    pos = (pos1 + pos2)[0:k[y]]
    ans = list(range(-1,-n[y]-1,-1))
    for x in pos:
        ans[x] *= -1
    z=''
    for i in ans:
        z = z + str(i) + ' '
    print(z[:-1])      
