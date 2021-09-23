'''
Match Maker
Little Mojo owns a match making company, which even to her surprise is an extreme hit. She says that her 
success rate cannot be matched (Yeah, wordplay!) in the entire match-making industry. She follows an 
extremely simple algorithm to determine if two people are matches for each other. Her algorithm is not at 
all complex, and makes no sense - not even to her. But she uses it anyway.

Let's say say that on a given day she decides to select n people - that is, n boys and n girls. She gets 
the list of n boys and n girls in a random order initially. Then, she arranges the list of girls in 
ascending order on the basis of their height and boys in descending order of their heights. A girl Ai can 
be matched to a boy on the same index only, that is, Bi and no one else. Likewise, a girl standing on Ak 
can be only matched to a boy on the same index Bk and no one else.

Now to determine if the pair would make an ideal pair, she checks if the modulo of their heights is 0, 
i.e., Ai % Bi == 0 or Bi % Ai == 0. Given the number of boys and girls, and their respective heights in 
non-sorted order, determine the number of ideal pairs Mojo can find.

Input
The first line contains number of test cases. Then, the next line contains an integer, n, saying the 
number of boys and girls. The next line contains the height of girls, followed by the height of boys.

Output
Print the number of ideal pairs corresponding to every test case.

Example
Input:

2

4

1 6 9 12

4 12 3 9

4

2 2 2 2

2 2 2 2

Output:

2

4
'''
for _ in range(int(input())):
    n=int(input())
    ga=[int(x) for x in input().split()]
    ba=[int(x) for x in input().split()]
    ga.sort()
    ba.sort(reverse=True)
    c=0
    for i in range(n):
        if ga[i] % ba[i] == 0 or ba[i] % ga[i] == 0:
            c+=1
    print(c)