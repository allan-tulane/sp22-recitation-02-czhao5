# CMPS 2200  Recitation 02

(Team Member 1): Reagan Esteves 
(Team Member 2): Chenyu Zhao

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$. #done 

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones. #done

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.#done

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = n**2$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.
   W(n) for when f(n)=1 is W(n)=n. W(n) for when f(n) = n^2 is W(n)=n^2. W(n) for when f(n) = n is W(n)=nlogn. The trends match our derivations. There's a linear growth trend for f(n)=1 , f(n)= n has growth that increases more, and f(n)=n^2 is a quadratic growth. Our work is in work.pdf.
  
(Empirical evidence shown below)
              n          n^2
|     n |   W_1 |       W_2 |
|-------|-------|-----------|
|    10 |    20 |       122 |
|    20 |    40 |       488 |
|    50 |   110 |      3120 |
|   100 |   250 |     12750 |
|  1000 |  2790 |   1284894 |
|  5000 | 14288 |  32132164 |
| 10000 | 28950 | 128559238 |
              1
|     n |   W_1 |
|-------|-------|
|    10 |     7 |
|    20 |     7 |
|    50 |    15 |
|   100 |    31 |
|  1000 |   127 |
|  5000 |   255 |
| 10000 |   511 |

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) 
- 
  Let's assume b = 2 and a = 4, thus log_2 of 4 will equal 2. If c < 2, equaling 1, then the asymptotic behavior will be O(n lg n) because the work of a function with an n constant is O(n lg n). If c == 0, then the asymptotic behavior will be O(n) because n^0 is 1 and a function with a 1 constant is O(n) work. If c > 2, then let's assume it's 3. Then the asymptotic behavior of c == 3 is O(n^3) because a function with an n^3 constant has asymptotic behavior of n^3. If c == 2 (when c == log_b a) then the asymptotic behavior is O(n^2) because a function with an n^2 constant is O(n^2). These asymptotic behaviors match with our empirical evidence because when graphed they have the same numerical value.
(As shown below)
                n^0        n^1
      n |      W_1 |       W_2 |
|-------|----------|-----------|
|    10 |       85 |       126 |
|    20 |      341 |       524 |
|    50 |     1365 |      2518 |
|   100 |     5461 |     10172 |
|  1000 |   349525 |    697496 |
|  5000 | 22369621 |  34237688 |
| 10000 | 89478485 | 136960752 |
                  n^2             n^3
|     n |        W_1 |           W_2 |
|-------|------------|---------------|
|    10 |        328 |          1692 |
|    20 |       1712 |         14768 |
|    50 |      12936 |        236908 |
|   100 |      61744 |       1947632 |
|  1000 |    8544512 |    1987993280 |
|  5000 |  294904064 |  249711292352 |
| 10000 | 1279616256 | 1998845169408 |
  
- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 
S(n) for when f(n)=1 is O(n). S(n)for when f(n) = n^2 is O(n^2), S(n) for when f(n) = n is O(log_base2(n)).

(Empirical evidence shown below)
              n          n^2
|     n |   W_1 |       W_2 |
|-------|-------|-----------|
|    10 |    14 |       110 |
|    20 |    28 |       440 |
|    50 |    72 |      2782 |
|   100 |   148 |     11220 |
|  1000 |  1498 |   1124740 |
|  5000 |  7495 |  28121967 |
| 10000 | 14996 | 112497106 |
              1
|     n |   W_1 |
|-------|-------|
|    10 |     3 |
|    20 |     3 |
|    50 |     4 |
|   100 |     5 |
|  1000 |     7 |
|  5000 |     8 |
| 10000 |     9 |