# def swap(arr,i,j):
#     if i>=j:
#         return
#     arr[i],arr[j]=arr[j],arr[i]

#     swap(arr,i+1,j-1)

arr=[1,2,3,4,5]
j=len(arr)-1
i=0
# print(j)
# swap(arr,i,j)
print(len(arr))


# second------------------2
# def swap(arr,i):
#     j=len(arr)
#     if i>=j/2:
#         return
#     arr[i],arr[j-i-1]=arr[j-i-1],arr[i]

#     swap(arr,i+1)

# arr=[1,2,3,4,5]
# j=len(arr)
# i=0
# # print(j)
# swap(arr,i)
# print(arr)

# Given String palindrom or not-----------------------------


# def palindrom(s,i):
#     j=len(s)
#     if i>=j/2:
#         return True
#     if s[i]!=s[j-i-1]:
#         return False
#     palindrom(s,i+1)




# s="bhargav"
# i=0

# palindrom(s,i)
# if True:
#     print("palindrom")
# else:
#     print("Not palindrom")

# problem : count digit in array--------------------------------------
# def count(ar):
#     # z=len(ar)
#     k={}

#     for i in ar:
#         if i in k:
#             k[i]+=1
#         else:
#             k[i]=1
#     for o,p in k.items():
#         print(o,":",p)



# ar=[1,1,2,2,3,3,3,4,4,4,5,5,5]
# count(ar)

# problem -----------------------rearangement array

# def re(ar):
#     l=int((len(ar)-1)/2)
#     k=int(l+1)
#     j=sorted(ar)
#     x=j[:k]
#     # print(x)
#     p=j[k:]
#     v=sorted(p,reverse=True)
#     # print(v)
#     m=x+v
#     print(m)

# ar=[7,8,1,6,5,7,9]
# re(ar)

# problem---------------------sum of array of eliment
# def su(ar):
#     sum=0
#     for i in range(len(ar)):
#         sum+=ar[i]
#     return sum

# ar=[7,8,1,6,5,7,9]
# print(su(ar))



# problrm ------------------rotate array by k element

# def ro(ar,k):
#     j=ar[:k]
#     i=ar[k:]
#     z=i+j
#     print(z)

# ar=[7,8,1,6,5,7,9]
# k=2
# ro(ar,k)

# import numbers


# problem----------------avrage of all array numbers
# def av(ar):
#     i=0
#     sum=0
#     j=len(ar)-1
#     if i==j:
#         return
#     sum+=ar[i]
#     i+=1
#     av(ar)

# ar=[1,2,1,1,5,1]
# av(ar)



# problem ------------------median in find arry
# def me(ar):
#     ar=sorted(ar)
#     l=len(ar)
#     j=int(l/2)-1
#     if l%2==0:
#         return (ar[j]+ar[j+1])/2
#     else:
#         return ar[j]


# ar=[4, 7, 1, 2, 5, 6]
# print(me(ar))


# problrm ----------------------removed dublicate sorted array
# def du(ar):
#     # ar=list(set(ar))
#     # return ar
#     j=[]
#     for i in ar:
#         print(i)
#         if i in j:
#             pass
#         else:
#             j.append(i)
#             # print(j)
#     print(j)

# ar=[1,2,2,3,3,4,4,5,5,6,6]
# du(ar)


# problem --------------Find all Symmetric Pairs in the array of pairs
# def sy(ar):
#     for i in range(len(ar)):
#         # for j in range(len(ar)):
#         #     a=ar[(i)]
#         #     if i!=j and a==ar[i]:
#         #         return a
#         #     else:
#         #         pass



# ar=[[1,2],[2,1],[3,4],[4,5],[5,4]]
# print(sy(ar))
# problem ------------Maximum Product Subarray in an Array

# def au(ar):
#     p=[]
#     for i in range(len(ar)):
#         ar.pop(ar[i])
#         print(ar)
#         ar.insert(i,ar[i])
#         print(ar)
#         # for i in ar:
#         #     i*=i
#         #     p.append(i)
#         # ar.insert(i)

# ar=[1,2,3,4,5,0]
# au(ar)

# problem-------Replace elements by its rank in the array
# def el(ar):
#     j=sorted(ar)
    
#     l=[]
#     for i in ar:
#         for k in range(len(j)):
#             if i==j[k]:
#                 l.append(k+1)
#             else:
#                 pass
#     return l  


# ar=[20,15,26,2,98,6]
# print(el(ar))

# problem ----------Sort Elements of an Array by Frequency
# def fr(ar):
#     co=[]
#     # for i in range(len(ar)):
#     #     count=0
#     #     for j in range(len(ar)):
#     #         if ar[i]==ar[j] and i!=j:
#     #             count+=1
#     #         else:
#     #             pass
#     #     co.append(count)
#     # return co
            




# ar=[1,2,3,2,4,3,1,2]
# print(fr(ar))
    
# problem-----------Rotate array by K elements
# def ro(ar,k):
#     # for i in range(k):
#     #     j=ar.pop(0)
#     #     ar.append(j)
#     # return ar
#     # second solution
#     j=ar[:k]
#     k=ar[k:]
#     i=k+j
#     return i

# ar=[1,2,3,4,5,6,7]
# k=4
# print(ro(ar,k))

# problem--------------indek return
# def ro(ar,k):
#     j=ar.index(k)
#     print(j)

# ar=[1,2,3,4,5,6,7]
# k=4
# ro(ar,k)

# problrm--------Check if array is subset of another array

# def su(ar1,ar2):
#     k=[]
#     for i in range(len(ar1)):
#         for j in range(len(ar2)):
#             if ar1[i]==ar2[j] :
#                 k.append(ar1[i])
#     ar1=sorted(ar1)
#     ar2=sorted(ar2)
#     k=sorted(k)
#     if k==ar1:
#         print("subset")
#     elif k==ar2:
#         print("subset")
#     else:
#         print("not subset")

# ar1=[1,3,4,5,2]
# ar2=[2,4,3,1,7,5,15]
# su(ar1,ar2)

# ------------------------------------------------------------------------------
# problem of number
# ==================================================================

# problem ---------Find all Palindrome Numbers in a given range

# def pl(x,y):
#     p=[]
#     for i in range(x,y):
        
#         i=str(i)
#         j=i[::-1]
#         if i==j:
#             p.append(i)
#         else:
#             pass
#     for o in p:
#         print(o))

# x=10
# y=50
# pl(x,y)

# problem-----------Check if a number is Armstrong Number or not
# def am(a):
#     a=str(a)
#     b=len(a)
#     p=0
#     for i in a:
#         i=int(i)
#         p+=i**b
#     a=int(a)
#     if a==p:
#         print("Armstrong Number")
#     else:
#         print("Not Armstrong Number")

    
# a=153
# am(a)

# problem-----------------Check whether a number is Perfect Number or not
# def pe(a):
#     r=0
#     a=int(a)
#     for i in range(1,a):
#         if a%i==0:
#             r+=i
#     if r==a:
#         print(" is Perfect Number")
#     else:
#         print(" is not Perfect Number")
# a=28
# pe(a)

# problem--------------------Find Sum of AP Series
# def ap(n,a,d):
#     p=[]

#     for i in range(n):
#         p.append(a)
#         a+=d
#     return sum(p)

# n,a,d=4,2,2
# print(ap(n,a,d))

# problem--------------Find Sum of GP Series

# def ap(n,a,d):
#     p=[]

#     for i in range(n):
#         p.append(a)
#         a*=d
#     return sum(p)

# n,a,d=2,3,5
# print(ap(n,a,d))

# problem--------------Check if given year is a leap year or not
# def lip(ye):
#     # if ye%4==0 and ye%100!=0:
#     #     print("leap year")
#     # elif ye%100==0:
#     #     print("not leap year")
#     # elif ye%400==0:
#     #     print("leap year")
#     # else:
#     #     print("not leap year")
# ye=2020
# lip(ye)

# problem-----------fibonacci series find up to index number
# def fi(n):
#     ar=[0,1]
#     for i in range(2,n+1):
#         j=ar[i-1]+ar[i-2]
#         ar.append(j)
#     return ar
# n=5
# print(fi(n))

# problem---------ASCII VALUE
# a='e'
# print(ord(a))
# provlem --------------Remove all vowels from the String
# def vo(v):
#     # v=str(v)
#     a=[]
#     j=['a','e','i','o','u']
#     for i in v:
#         if i.lower() not in j:
#             a.append(i)
#     a=''.join(a)
#     return a


# v="take u forward"
# print(vo(v))
# program -----------------Remove Spaces from a String
# def remove(string):
#     return string.replace(" ", "")
    
# string="Take you forward"
# print(remove(string))
# program-----------------remove in string ecept in alphbet
# def alp(al):
#     a=[]
#     for i in al:
#         if i.isalpha():
#             a.append(i)

#     return "".join(a)
# al="take12% *&u ^$#forward"
# print(alp(al))
# program---------------------revers string 4
# def re(st):
#     a=list(st[::-1])
#     return "".join(a)
# st="I AM BHARGAV"
# print(re(st))
# program--------------------Remove brackets from an algebraic expression
# def re(br):
#     j=["(",")"]
#     for i in br:
#         if i in j:
#             br=br.replace(i,"")
#     return br

# br="a+((b-c)+d)"
# print(re(br))
# problem----------Sum of the Numbers in a String
# def su(st):
#     temp="0"
#     sum=0
#     for i in st:
#         if i.isdigit():
#             temp+=i
#         else:
#             sum+=int(temp)

#             temp="0"
#     return sum + int(temp) 


# st="1xyz23"
# print(su(st))

# problem------------------Capitalize first and last character of each word of a string
# def capitalize_first_last_letters(str1):
#      str1 = result = str1.title()
#      result =  ""
#      for word in str1.split():
#         # print(word)
#         result += word[:-1] + word[-1].upper() + " "
#      return result[:-1]  
     
# print(capitalize_first_last_letters("python exercises practice solution"))
# print(capitalize_first_last_letters("w3resource"))

# problem --------------Calculate Frequency of characters in a String
# def cal(fr):
#     a={}
#     for i in fr:
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1
            
#     return str(a)

# fr="w3resource"
# print(cal(fr))

# program--------------------Check if two Strings are anagrams of each other
# def an(s1,s2):
#     if sorted(s1)==sorted(s2):
#         print("The String is a anagran")
#     else:
#         print("The String are not anagram")
    
# s1 ="listen"
# s2 ="silent"
# print(an(s1,s2))

# program ------------------Maximum occurring character in a string
# def oc(ch):
#     a={}
#     for i in ch :
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1
#     if a,key>1:
#         return a,key=a.get
#     return a,key=a.get)


# ch="takeuforward"
# print(oc(ch))

# problem ---------prinnt dublicate in input String

# def oc(ch):
#     a={}
#     for i in ch :
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1

#     b={}
#     for key,value in a.items():
#         if value>1:
#             # b=key,value
#             print(key,value)
    
# ch="takeuforward"
# oc(ch)

# problem-----------remove dublication in String

# def re(st):
#     a=[]
#     for i in st:
#         if i in a:
#             pass
#         else:
#             a.append(i)
#     return str("".join(a))

# st="cbacdcbc"
# print(re(st))

# problem -----------------Remove character First String to Second String
# def re(str1,str2):
#     a=[]
#     for i in str1:
#         for j in str2:
#             if i==j:
#                 pass
#             else:
#                 a.append(i)
#     print(a)

# str1 = "abcdef"
# str2 = "cefz"
# re(str1,str2)
# problem---------------------- Change every letter with next lexicographic alphabe
# def ch(st):
#     a=[]
#     # for i in st:
#     #     if i=='z':
#     #         a.append('a')
#     #     else:
#     #         i=i+1
#     #         print(i)
#     #         j+=1
#     #         m=str(j)
#     #         a.append(i)
    


# ch(st)

# problem -------------Count the number of words in a given string
# def co(st):
#     ste=st.split()
#     j=len(ste)
#     return j   

# st="MY NAME IS BHARGAV"
# print(co(st))
# problem------------Find word with highest number of repeated letters in string
# def hi(st):
#     a=[]
#     b={}
#     j=st.split()
#     for i in j:
#         for k in i:
#             if k in b:
#                 b[k]+=1
#             else:
#                 b[k]=1 
#     return b


# st="abcdefghij google microsoft"
# print(hi(st))