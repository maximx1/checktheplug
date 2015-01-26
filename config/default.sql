CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, gravatar TEXT, admin INTEGER NOT NULL DEFAULT 0);
CREATE TABLE applications(id INTEGER PRIMARY KEY AUTOINCREMENT, appshortkey TEXT NOT NULL UNIQUE, name TEXT NOT NULL, description TEXT, host TEXT NOT NULL, owner_id INTEGER NOT NULL, FOREIGN KEY(owner_id) REFERENCES users(id))
CREATE TABLE applicationAdmins(app_id INTEGER, user_id INTEGER, PRIMARY KEY (app_id, user_id), FOREIGN KEY(app_id) REFERENCES applications(id), FOREIGN KEY(user_id) REFERENCES users(id));
CREATE TABLE envVariables(app_id INTEGER, envVariable TEXT, envValue TEXT, PRIMARY KEY (app_id, envVariable), FOREIGN KEY(app_id) REFERENCES applications(id));
CREATE TABLE authKeys(app_id TEXT, authKey TEXT, PRIMARY KEY (app_id, authKey), FOREIGN KEY(app_id) REFERENCES applications(id));

INSERT INTO users(username, password, gravatar, admin) values("admin", "admin", "https://s.gravatar.com/avatar/d42def31b1881aac9ed5c54300f50411?s=200", 1);
INSERT INTO users(username, password, gravatar) values("user1", "user1", "https://s.gravatar.com/avatar/a6b1b12cfc5907a60cd7517c88d3931e?s=200");
//INSERT INTO users(username, password, gravatar, admin) values("user2", "user2", "https://s.gravatar.com/avatar/a6b1b12cfc5907a60cd7517c88d3931e?s=200", DEFAULT);

// The Following represents "example.com" and "user1"
// Uncomment the following 2 lines if you want to import a sample app.
INSERT INTO applications(appshortkey, name, description, host, owner_id) values("g0zrN9i1", "example.com", "default site for giggles.", "example.com", 1);
INSERT INTO applicationAdmins(app_id, user_id) values(1, 2);
INSERT INTO envVariables(app_id, envVariable, envValue) values(1, "PORT_NUMBER", "3000");
INSERT INTO authKeys(app_id, authKey) values(1, "E8NU3BSSOJSH1XQWAWQZVJ29GCAHP6R2WAIQM60E")

// Dev Notes. You can ignore the following section.
// select u.* from users u join applicationAdmins a on a.user_id = u.id where a.app_id = 1;
// select ak.authKey from authKeys ak join applications a on ak.app_id = a.id where a.appshortkey = ? and ak.authKey = ?