Python- Everything_Is_Object
This Directory is covers many typical questions that may be asked during an interview concering python.

Tasks:

0. What function would you use to print the type of an object?

Write the name of the function in the file, without ().

1. How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 100

3. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

4. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

5. In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

6. What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

7. What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

8. What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

9. What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

10. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

11. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

12. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

13. What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

14. What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

15. What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

16. What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

17. What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

18. What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

19. Write a function def copy_list(a_list): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/$
No test cases needed

20. a = ()
Is a a tuple? Answer with Yes or No.

21. a = (1, 2)
Is a a tuple? Answer with Yes or No.

22. a = (1)
Is a a tuple? Answer with Yes or No.

23. a = (1, )
Is a a tuple? Answer with Yes or No.

24. What does this script print?

a = (1)
b = (1)
a is b

25. What does this script print?

a = (1, 2)
b = (1, 2)
a is b

26. What does this script print?

a = ()
b = ()
a is b

27. >>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

28. >>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

29. Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

introduction
id and type
mutable objects
immutable objects
why does it matter and how differently does Python treat mutable and immutable objects
how arguments are passed to functions and what does that imply for mutable and immutable objects
If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.
