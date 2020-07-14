# Designing and Debugging

## Rules for If-Statements
1. Every if-statement must have an else.<br>
2. If this else should never be run because it doesn’t make sense, then<br>
you must use a die function in the else that prints out an error <br>
message and dies, just like we did in the last exercise. This will find<br>
many errors.<br>
3. Never nest if- statements more than two deep and always try to do them
<br> one deep. This means if you put an if in an if, then you should be<br>
looking to move that second if into another function.<br>
4. Treat if- statements like paragraphs, where each if, elif, else grouping
 <br>is like a set of sentences. Put blank lines before and after.<br>
5. Your boolean tests should be simple. If they are complex, move their<br>
calculations to variables earlier in your function and use a good name<br>
for the variable.<br>


## Rules for loop
1. Use a while-loop only to loop forever, and that means probably never.
<br> This only applies to Python; other languages are different.<br>
2. Use a for-loop for all other kinds of looping, especially if there<br>
is a fixed or limited number of things to loop over.<br>


## Tips for Debugging
1. Do not use a “debugger.” A debugger is like doing a full- body scan <br>
on a sick person. You do not get any specific useful information, and <br>
you find a whole lot of information that doesn’t help and is just confusing.
2. The best way to debug a program is to use print to print out the <br>
values of variables at points in the program to see where they go wrong.<br>
3. Make sure parts of your programs work as you work on them. Do not <br>
write massive files of code before you try to run them. Code a little,<br>
run a little, fix a little.
