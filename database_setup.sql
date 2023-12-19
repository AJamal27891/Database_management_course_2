CREATE DATABASE IF NOT EXISTS SchoolDB;

USE SchoolDB;


DROP TABLE IF EXISTS enrollments;
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

DROP TABLE IF EXISTS students;
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    phone INT ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);


DROP TABLE IF EXISTS courses;

CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100)
);


INSERT INTO teachers (name, specialization, teacher_id) VALUES 
('John Doe', 'Mathematics',1),
('Jane Smith', 'Physics',2),
('Emily Johnson', 'Chemistry',3),
('Mike Brown', 'History',4),
('Sarah Davis', 'English Literature',5);


INSERT INTO courses (title, description, teacher_id) VALUES 
('Introduction to Mathematics', 'This course covers fundamental mathematical concepts.', 1),
('Fundamentals of Physics', 'An introductory course on the principles of physics.', 2),
('Basics of Chemistry', 'Explore the basics of chemical principles and reactions.', 3),
('World History', 'A comprehensive overview of world history.', 4),
('English Literature', 'Study of classic and contemporary works in English literature.', 5);
