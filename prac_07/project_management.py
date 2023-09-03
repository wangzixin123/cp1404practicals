from project import Project

# Import the datetime module for working with dates
import datetime


# Define the main function
def main():
    # Set the filename for the text file containing project data
    filename = 'project.txt'
    # Load the list of projects from the text file
    projects = load_projects(filename)
    print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")
    choice = input(">>> ").strip().lower()
    # Create a menu loop for user interaction
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print("Projects loaded successfully.")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved successfully.")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice. Please select a valid option.")
        print("""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")
        choice = input(">>> ").strip().lower()


# Function to load projects from a text file
def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                name, start_date, priority, estimate, completion_percent = line.strip().split('\t')
                # Convert the start_date string to a datetime.date object
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                # Create a Project object and append it to the list
                projects.append(Project(name, start_date, int(priority), float(estimate), int(completion_percent)))
    except FileNotFoundError:
        pass  # Handle the case where the file doesn't exist
    return projects


# Function to save projects to a text file
def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion Percent\n")
        for project in projects:
            # Write project data in a tab-separated format
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}"
                f"\t{project.priority}\t{project.estimate:.2f}\t{project.completion_percent}\n")


# Function to display projects (incomplete and completed, sorted by priority)
def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percent < 100]
    completed_projects = [project for project in projects if project.completion_percent == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(project)


# Function to filter projects by start date
def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


# Function to add a new project
def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
        priority = int(input("Priority: "))
        estimate = float(input("Cost estimate: $"))
        completion_percent = int(input("Percent complete: "))
        # Create a new Project object and append it to the list
        projects.append(Project(name, start_date, priority, estimate, completion_percent))
        print("Project added successfully.")
    except ValueError:
        print("Invalid input format.")


# Function to update a project
def update_project(projects):
    print("Update a project")
    for i, project in enumerate(projects):
        print(f"{i}: {project}")
    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            new_completion_percent = int(input("New Percentage: "))
            new_priority = int(input("New Priority: "))
            # Update the project's completion percent and priority
            project.completion_percent = new_completion_percent
            project.priority = new_priority
            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input format.")


main()
