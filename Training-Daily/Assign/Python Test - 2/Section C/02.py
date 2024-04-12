"""    2) Suppose there is a sports tournament, and you have a dictionary representing the current points of teams in the tournament. Each team is represented by its name (a string) and its points (an integer). Write a Python program to perform the following tasks:
        ◦ Implement a function 'add_team' which takes the team's name and points as an input and adds it to the dictionary if it doesn’t exist.
        ◦ Implement a function 'remove_team' which takes the team's name as input and deletes it from the dictionary if it exists.
        ◦ Implement a function 'update_points' which takes existing team’s names and points as input and updates it to the dictionary.
        ◦ Implement a function 'get_top_teams' which takes n as an input and gives top n teams from the dictionary.
        ◦ Implement a function 'write_to_file' that takes the dictionary and a filename as input and writes the information to the given filename in the format: "Team: Points".
Example:
(’Team 1“. 120, ’Team2". 150, ’Team3". 170, ’Team4". 140, ’Team5". 200)"""

class Tournament:
    def __init__(self):
        self.teams = {}

    def add_team(self, name, points):
        if name not in self.teams:
            self.teams[name] = points
            print(f"Team '{name}' added with {points} points.")
        else:
            print(f"Team '{name}' already exists.")

    def remove_team(self, name):
        if name in self.teams:
            del self.teams[name]
            print(f"Team '{name}' removed.")
        else:
            print(f"Team '{name}' not found.")

    def update_points(self, name, points):
        if name in self.teams:
            self.teams[name] = points
            print(f"Points for team '{name}' updated to {points}.")
        else:
            print(f"Team '{name}' not found.")

    def get_top_teams(self, n):
        sorted_teams = sorted(self.teams.items(), key=lambda x: x[1], reverse=True)
        return sorted_teams[:n]

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for team, points in self.teams.items():
                file.write(f"{team}: {points}\n")
        print(f"Data written to '{filename}'.")

ob_t = Tournament()

while True:
    print("""
    1. Add Team
    2. Remove Team
    3. Update Points
    4. Get Top Teams
    5. Write to File
    6. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter team name: ")
        points = int(input("Enter points: "))
        ob_t.add_team(name, points)
    elif choice == '2':
        name = input("Enter team name to remove: ")
        ob_t.remove_team(name)
    elif choice == '3':
        name = input("Enter team name to update points: ")
        points = int(input("Enter new points: "))
        ob_t.update_points(name, points)
    elif choice == '4':
        n = int(input("Enter number of top teams to display: "))
        top_teams = ob_t.get_top_teams(n)
        print(f"Top {n} teams:")
        for team, points in top_teams:
            print(f"{team}: {points}")
    elif choice == '5':
        filename = input("Enter filename to write to: ")
        ob_t.write_to_file(filename)
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
