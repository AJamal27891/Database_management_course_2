
# Database Management Course System

## Description

This project is a training example designed for educational purposes, particularly for teaching the fundamentals of database management. The system demonstrates the integration of a web application with a MySQL database, showcasing essential operations such as creating, reading, updating, and deleting data (CRUD).

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python (3.x recommended)
- Pip (Python package manager)
- MySQL Server

## Installation

### MySQL Setup

#### Windows:

1. **Download MySQL Installer**: Go to the [MySQL Downloads page](https://dev.mysql.com/downloads/installer/) and download the MySQL installer.
2. **Install MySQL**: Run the installer and follow the prompts to install MySQL. During installation:
   - Choose a setup type (Full, Developer, Server only, etc.).
   - Set up a root password when prompted.
   - Optionally, install MySQL Workbench.

#### macOS:

1. **Download MySQL**: Visit the [MySQL Downloads page](https://dev.mysql.com/downloads/mysql/) and download the MySQL Community Server for macOS.
2. **Install MySQL**: Open the downloaded DMG file and follow the installation instructions.
3. **Set Root Password**:
   - Open Terminal.
   - Start the MySQL server with `sudo /usr/local/mysql/support-files/mysql.server start`.
   - Secure MySQL with `sudo /usr/local/mysql/bin/mysql_secure_installation`.
   - Follow the prompts to set a root password.

### Python and Project Dependencies

1. **Clone/Download the Project**: Clone or download the project to your local machine.
2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the project directory.
3. **Create a Virtual Environment (optional but recommended)**:
   - Windows: `python -m venv venv`
   - macOS: `python3 -m venv venv`
4. **Activate the Virtual Environment**:
   - Windows: `.\venv\Scripts\activate`
   - macOS: `source venv/bin/activate`
5. **Install Dependencies**: Run `pip install -r requirements.txt`.

## Configuration

1. **Database Setup**: Use the provided SQL script to set up your database schema. This can be done through MySQL Workbench or the command line.
2. **Application Configuration**: Modify the `config.ini` file with the correct database credentials and other necessary configurations.

## Running the Application

1. **Start the Flask App**: Run `python app.py` (Windows) or `python3 app.py` (macOS) from the project directory.
2. **Access the App**: Open a web browser and go to `http://127.0.0.1:5000/`.


## Contributing

Contributions to this project are welcome! If you have improvements or fixes, please follow these steps to contribute:

1. **Fork the Repository**: Start by forking the repository. This creates your own copy of the project where you can make changes.

2. **Clone the Forked Repository**:
   - Clone your forked repository to your local machine to work on it.
   - Use the command: `git clone https://github.com/YourUsername/RepositoryName.git`.

3. **Create a New Branch**:
   - Navigate into the cloned directory.
   - Create a new branch for your changes: `git checkout -b your-branch-name`.
   - Use a name that describes the feature or fix you are working on.

4. **Make Your Changes**:
   - Implement your changes and enhancements or fix bugs in the code.
   - Make sure to test your changes locally.

5. **Commit and Push Your Changes**:
   - Commit your changes with a clear and descriptive commit message: `git commit -m "A brief description of changes"`.
   - Push the changes to your fork: `git push origin your-branch-name`.

6. **Create a Pull Request (PR)**:
   - Go to the original repository on GitHub.
   - You’ll see a banner suggesting to create a pull request from your newly pushed branch. Click on 'Compare & pull request'.
   - Add a title and description to your pull request explaining the changes you made.
   - Submit the pull request.

7. **Review and Merge**:
   - The repository maintainers will review your pull request.
   - If your changes are approved, they may be merged into the main branch.
   - If there are any comments or suggestions, please address them.

Please make sure your code adheres to the project's style and conventions to increase the likelihood of your changes being accepted.


### Additional Guidelines

- **Stay Up-to-Date**: Regularly pull from the main branch to keep your local repository updated.
- **Follow Project Standards**: Pay attention to coding style, naming conventions, and documentation within the project.
- **Discuss Major Changes**: For significant changes, it's best to open an issue first to discuss it with the maintainers.


For a project specifically designed for Pearson's "Database Management System" course, the license section of your README should be tailored to reflect Pearson's rights, course specifics, and usage policies. Here's an updated example of what this section could look like:
