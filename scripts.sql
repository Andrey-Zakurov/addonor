# скрипты sqlite

# скрипты создания скелета базы данных приложения
CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_tlgm INTEGER,
	id_group INTEGER,
	id_job_title INTEGER,
	structure_id INTEGER,
	FOREIGN KEY (id_group) REFERENCES groups (id),
	FOREIGN KEY (structure_id) REFERENCES structures_company (id)
	FOREIGN KEY (id_job_title) REFERENCES job_titles (id));
CREATE TABLE groups(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, permisssions_id INTEGER);
CREATE TABLE job_titles (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary INTEGER, id_group INTEGER);
CREATE TABLE structures_company (id INTEGER PRIMARY KEY AUTOINCREMENT, name_structure TEXT, permissions_id INTEGER);
CREATE TABLE groups(id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					perm_id INTEGER,
					FOREIGN key (perm_id) REFERENCES permissions_groups (id));
