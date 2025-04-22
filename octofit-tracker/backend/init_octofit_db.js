// 'use octofit_db;' n'est pas une instruction valide en JavaScript pour mongo shell v3.6+
// On utilise la ligne de commande mongo pour sélectionner la base de données
// Les instructions suivantes créent les collections et l'index unique

db.createCollection("users");
db.createCollection("teams");
db.createCollection("activity");
db.createCollection("leaderboard");
db.createCollection("workouts");
db.users.createIndex({ email: 1 }, { unique: true });
