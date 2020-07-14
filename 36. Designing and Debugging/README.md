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
