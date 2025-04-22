# Test data for populating octofit_db
# This file will be used by the management command to insert test data into MongoDB

TEST_USERS = [
    {"email": "paul.octo@mergington.edu", "username": "PaulO", "password": "testpass1", "first_name": "Paul", "last_name": "Octo"},
    {"email": "jessica.cat@mergington.edu", "username": "JessicaC", "password": "testpass2", "first_name": "Jessica", "last_name": "Cat"},
    {"email": "student1@mergington.edu", "username": "Student1", "password": "testpass3", "first_name": "Alex", "last_name": "Smith"}
]

TEST_TEAMS = [
    {"name": "OctoFit Allstars", "members": ["PaulO", "JessicaC"]},
    {"name": "Mergington Movers", "members": ["Student1"]}
]

TEST_ACTIVITIES = [
    {"user": "PaulO", "activity_type": "running", "duration": 30, "distance": 5.0, "points": 50},
    {"user": "JessicaC", "activity_type": "walking", "duration": 60, "distance": 4.0, "points": 40},
    {"user": "Student1", "activity_type": "strength", "duration": 45, "points": 60}
]

TEST_LEADERBOARD = [
    {"team": "OctoFit Allstars", "points": 90, "week": "2025-W17"},
    {"team": "Mergington Movers", "points": 60, "week": "2025-W17"}
]

TEST_WORKOUTS = [
    {"name": "Cardio Blast", "description": "A fun running and jumping workout.", "suggested_for": "All"},
    {"name": "Strength Circuit", "description": "Pushups, squats, and planks.", "suggested_for": "Intermediate"}
]
