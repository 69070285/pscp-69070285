# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
OJ3476 - [LEARNING LOGS] CuteCat CuteFox
```

OJ submission ID, if submitted:

```text
659496
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
1-3 hours
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
Input:
Line 1 - An integer (amount) representing the number of JSON data lines.
Next amount lines - Strings containing dictionaries of names and IDs.

Output:
Line 1 - The total number of cats.
Line 2 - The total number of foxes.
Next lines - All cats sorted by their ID numbers.
Following lines - All foxes sorted by their ID numbers.

Constraints:
It checks whether "Cat" appears in the value string to decide whether an item belongs to the cats or foxes dictionary. If "Garfield" is not in foxes and "Cat01" is not already used in cats, the code adds "Garfield": "Cat01" to cats. If "Fubuki" is not in cats and "Fox01" is not already used in foxes, the code adds "Fubuki": "Fox01" to foxes. This also ensures that the IDs are sorted numerically.
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: Read the total number of items (amount).
Step 2: Create empty dictionaries for cats and foxes.
Step 3: Use a loop to read each raw string amount times. Try to parse it as standard JSON. If it fails because of single quotes, replace them with double quotes and try again.
Step 4: Go through the parsed dictionary items and check whether the value contains "Cat". Use this to decide whether to put the item in cats or foxes.
Step 5: Check the special rules for adding "Garfield" and "Fubuki", and add them if the conditions are met.
Step 6: Print the total number of cats and foxes.
Step 7: Sort both dictionaries by their ID numbers and print each animal’s name and ID on a separate line.
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
My final approach is the same as my first plan because this way is not too complicated for me.
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
This is a normal case with new cat and fox names, and add Garfield as Cat01 and Fubuki as Fox01 since they aren’t in the input.
```

Input:

```text
4
{"Luna" : "Cat04"}
{"Max" : "Cat02"}
{"Rex" : "Fox03"}
{"Zorro" : "Fox05"}
```

Expected output:

```text
Cat : 3
Fox : 3
Garfield : Cat01
Max : Cat02
Luna : Cat04
Fubuki : Fox01
Rex : Fox03
Zorro : Fox05
```

Actual output:

```text
Cat : 3
Fox : 3
Garfield : Cat01
Max : Cat02
Luna : Cat04
Fubuki : Fox01
Rex : Fox03
Zorro : Fox05
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
This is the case when Garfield and Fubuki are already included in the input with their default IDs (Cat01 and Fox01).
```

Input:

```text
4
{"Garfield" : "Cat01"}
{"Fubuki" : "Fox01"}
{"Tiger" : "Cat03"}
{"Vixen" : "Fox04"}
```

Expected output:

```text
Cat : 2
Fox : 2
Garfield : Cat01
Tiger : Cat03
Fubuki : Fox01
Vixen : Fox04
```

Actual output:

```text
Cat : 2
Fox : 2
Garfield : Cat01
Tiger : Cat03
Fubuki : Fox01
Vixen : Fox04
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
This tests input with single quotes ('), making sure the JSON fallback correctly handles them.
```

Input:

```text
2
{'Leo' : 'Cat05'}
{'Roxy' : 'Fox02'}
```

Expected output:

```text
Cat : 2
Fox : 2
Garfield : Cat01
Leo : Cat05
Fubuki : Fox01
Roxy : Fox02
```

Actual output:

```text
Cat : 2
Fox : 2
Garfield : Cat01
Leo : Cat05
Fubuki : Fox01
Roxy : Fox02
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text

```

What did they help with?

```text

```

What did you still do by yourself?

```text

```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
