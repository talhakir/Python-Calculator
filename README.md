# Python-Calculator

#### Description:
Used libraries:
* Python
* Tkinter

This calculator can calculate four basic calculations, handle priority of parenthesis and show the history.

There are two sets: history_setE(for expression) and history_setT(for result). These sets are used to display history.
They are appended in try block to be sure that the expressions will be added are valid. It is same for result.

Each different type of button have different colors to realize and differ easily.
- numbers, decimal point and parenthesis = green
- operators, result and clear = brown
- history = grey

History button has grey color because it needs to be different than the others.

When clicked on history, the results displayed as "expression" : "result" on a different page.
You need to reclick the history button to see the new results when you calculate new equations. They are not displayed if you do not reclick it.

You can click sum button to sum the expressions, you can click minus button to substract, you can click division button to divide, you can click multiplication button to multiply.

You can use priority of parenthesis to make your expression more precise. Do not forget to close the parenthesis.
You can use decimal point to evaluate decimal numbers, the result will be float variable.

If the expression is not valid, an error message comes up with except block.
In history window, you do not see the errors, you only see the valid expressions and their results.

This project has 4 functions:
- press
- Clear
- Result
- History

Press function is to prepare expression. It takes an argument and add it to the end of the current expression. After this function, the expression that is string remains as string.

Clear function is for clear the displayed expression.

Result is to show the result. It evaluates the expression and convert it to string.

History is to display the previous equations (except error).

Lastly, name == "main" statement is used to avoid using this class without intention. You do not have to worry about using this project mistakenly when you add these codes to your project.
