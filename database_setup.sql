CREATE DATABASE IF NOT EXISTS SchoolDB;

USE SchoolDB;

CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO teachers (name, specialization) VALUES 
('John Doe', 'Mathematics'),
('Jane Smith', 'Physics'),
('Emily Johnson', 'Chemistry'),
('Mike Brown', 'History'),
('Sarah Davis', 'English Literature');


INSERT INTO courses (title, description, teacher_id) VALUES 
('Introduction to Mathematics', 'This course covers fundamental mathematical concepts.', 1),
('Fundamentals of Physics', 'An introductory course on the principles of physics.', 2),
('Basics of Chemistry', 'Explore the basics of chemical principles and reactions.', 3),
('World History', 'A comprehensive overview of world history.', 4),
('English Literature', 'Study of classic and contemporary works in English literature.', 5);
