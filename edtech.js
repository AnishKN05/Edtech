<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Learning Path</title>
</head>
<body>
    <h1>Personalized Learning Path</h1>
    <form id="studentForm">
        <label for="age">Age:</label>
        <input type="number" id="age" required><br><br>
        <label for="interest">Interest in Subject (1: Math, 2: Science):</label>
        <input type="number" id="interest" required><br><br>
        <label for="score">Previous Score:</label>
        <input type="number" id="score" required><br><br>
        <button type="submit">Get Recommendation</button>
    </form>
    <p id="result"></p>

    <script>
        document.getElementById('studentForm').addEventListener('submit', function(event) {
            event.preventDefault();
            
            const age = document.getElementById('age').value;
            const interest = document.getElementById('interest').value;
            const score = document.getElementById('score').value;

            fetch('/api/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ age, interest, score })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = `Recommended Subject: ${data.recommended_subject}`;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
