<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quadratic Equation Solver</title>
</head>
<body>
    <h1>Quadratic Equation Solver</h1>
    <form method="POST">
        <label for="a">a:</label>
        <input type="text" id="a" name="a" required>
        <br>
        <label for="b">b:</label>
        <input type="text" id="b" name="b" required>
        <br>
        <label for="c">c:</label>
        <input type="text" id="c" name="c" required>
        <br>
        <button type="submit">Solve</button>
    </form>
    {% if result %}
        <h2>Result:</h2>
        <p text=3>{{ result }}</p>
    {% endif %}
</body>
</html>