#coding:utf-8

t_1, i_1 = [1,2,5,3], 3
t_2, i_2 = [1,4,5,2,3], 3
t_3, i_3 = [1,4], 1
t_4, i_4 = [4,1], 1
t_5, i_5 = [2,3,4,5,6,7,1,8,11,9],6

#=======================================================================================================================

def inserer(T,i) :
    # YOUR CODE HERE
    x = [T[x] for x in range(len(T[:i+1]))]
    for y in range(len(x)):
        for j in range(len(x)):
            if x[y] > x[j]:
                z = x[y]
                x[y] = x[j]
                x[j] = z
    return x[::-1]+T[i+1:]

#=======================================================================================================================

def inserer(T,i) :#╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬
    # YOUR CODE HERE
    x = [T[x] for x in range(len(T[:i+1]))]
    for n in range(len(x)):
        for j in range(n+1,len(x)):
            z = x[j]
            if x[j] < x[n]:
                x[j] = x[n]
                x[n] = z
    return x+T[i+1:]

assert inserer([1,2,5,3],3) == [1, 2, 3, 5]
assert inserer([1,4,5,2,3],3) == [1, 2, 4, 5, 3]
assert inserer([1,4],1) == [1, 4]
assert inserer([4,1],1) == [1, 4]
assert inserer([2,3,4,5,6,7,1,8,11,9],6) == [1, 2, 3, 4, 5, 6, 7, 8, 11, 9]

#=======================================================================================================================

def tri_par_insertion(T):
    # YOUR CODE HERE
    for y in range(len(T)):
        for j in range(len(T)):
            if T[y] > T[j]:
                z = T[y]
                T[y] = T[j]
                T[j] = z
    return T[::-1]

#=======================================================================================================================
def tri_par_insertion(T):#╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬╚╔╩╦╠═╬
    # YOUR CODE HERE
    for n in range(len(T)):
        for j in range(n+1,len(T)):
            z = T[j]
            if T[j] < T[n]:
                T[j] = T[n]
                T[n] = z
    return T

assert tri_par_insertion([2,3,4,1]) == [1, 2, 3, 4]
assert tri_par_insertion([7,8,9,1,2,3,5,6,4]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert tri_par_insertion([1,2]) == [1, 2]
assert tri_par_insertion([2,1]) == [1, 2]
assert tri_par_insertion([i for i in range(20)]) == [i for i in range(20)]
assert tri_par_insertion([1,2,3,4,5,6,7,8]) == tri_par_insertion([3,2,1,8,7,5,6,4])


if __name__ == "__main__":
    b = inserer(t_5, i_5)
    print(tri_par_insertion(b))


#Music pause: 03 h: 26 min: 21 sec