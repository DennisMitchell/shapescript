# ShapeScript

ShapeScript is a stack-based language with a relatively simple syntax. Unsurprisingly, most of its built-ins deal with altering the shape of strings. It is interpreted, character by character, as follows:

* `'` and `"` begin a string literal.

  Until the matching quote is found in the source code, all characters between these matching quotes are collected in a string, which is then pushed on the stack.

* `0` to `9` push the integers **0** to **9** on the stack. Note that `10` pushes *two* integers.

* `!` pops a string from the stack, and attempts to evaluate it as ShapeScript.

* `?` pops an integer from the stack, and pushes a copy of the stack item at that index.

  Index 0 corresponds to the topmost stack item (LIFO) and index -1 to the bottom-most one.

* `_` pops an iterable from the stack, and pushes its length.

* `@` pops two items from the stack, and pushes them in reversed order.

* `$` pops two strings from the stack, and splits the bottom-most one at occurrences of the topmost one. The resulting list is pushed in return.

* `~` pops a string (topmost) and an iterable from the stack, and joins the iterable, using the string as separator. The resulting string is pushed in return.

* All other characters **c** pop two items **x** and **y** (topmost) from the stack, and  evaluate the Python code `x c y`.

  For example, the sequence of characters `23+` would evaluate `2+3`, while the sequence of characters `"one"3*` would evaluate `'one'*3`, and the sequence of characters `1''A` would evaluate `1A''`.

  In the last case, since the result is not valid Python, a runtime error occurs.

Before executing the code, the interpreter will place the entire user input (if present) in form of a string on the stack. After executing the source code, the interpreter will print all items on the stack.

# Changeling

Changeling is a particularly cumbersome encoding of ShapeScript. It was created as a submission to the programming contest [Create a programming language that only appears to be unusable][contest], which it won. The syntax of the original submission was slightly different: it used `&` instead of  `~` for string joining, which is easier to incorporate into the Changeling encoding but also deprives ShapeScript of the bitwise AND operator.

A Changeling program must obey the following rules.

* All lines must have the same number of characters.

* All lines must consist of printable ASCII characters, followed by a single linefeed.

* The number of lines must match the number of printable characters per line.

It will generate a certain ShapeScript program – which isn't necessarily useful or even syntactically valid – as follows.

* Initially, there is no source code.

* For each line the following happens.

  * The accumulator is set to zero.

  * For each character **c** of the line (including the trailing linefeed), the code point of **c** is XORed with the accumulator divided by **2**, and the Unicode character that corresponds to the resulting code point is appended to the source code. Then, the difference between the code point of **c** and the integer **32** is added to the accumulator, and the next character of the line (if any) is processed.

If any part of the above fails, an error is raised. After all lines have been processed, the resulting ShapeScript program is executed as usual.

[contest]: http://codegolf.stackexchange.com/a/62064/12012 "Create a programming language that only appears to be unusable - Programming Puzzles & Code Golf Stack Exchange"
