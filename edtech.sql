-- Create a table to store student data and recommendations
CREATE TABLE StudentData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    interest_in_subject INT,
    previous_scores INT,
    recommended_subject INT
);

-- Insert a new student's data and their recommended subject
INSERT INTO StudentData (age, interest_in_subject, previous_scores, recommended_subject)
VALUES (14, 2, 75, 2);  -- 2 for Science

-- Retrieve recommended subjects for students
SELECT * FROM StudentRecommendations;
