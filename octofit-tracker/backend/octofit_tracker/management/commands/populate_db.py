from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import TEST_USERS, TEST_TEAMS, TEST_ACTIVITIES, TEST_LEADERBOARD, TEST_WORKOUTS

class Command(BaseCommand):
    help = 'Populate octofit_db with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        db.users.insert_many(TEST_USERS)
        db.teams.insert_many(TEST_TEAMS)
        db.activity.insert_many(TEST_ACTIVITIES)
        db.leaderboard.insert_many(TEST_LEADERBOARD)
        db.workouts.insert_many(TEST_WORKOUTS)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in octofit_db.'))
