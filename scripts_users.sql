CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_tlgm INTEGER,
	id_group INTEGER,
	id_job_title INTEGER,
	structure_id INTEGER,
	FOREIGN KEY (id_group) REFERENCES groups (id),
	FOREIGN KEY (structure_id) REFERENCES structures_company (id)
	FOREIGN KEY (id_job_title) REFERENCES job_titles (id));
CREATE TABLE permissions_groups (
	id INTEGER PRIMARY KEY,
	edit_user INTEGER DEFAULT (0),
	edit_permissions INTEGER DEFAULT (0),
	add_products INTEGER DEFAULT (0),
	edit_products INTEGER DEFAULT (0),
	edit_warehouse INTEGER DEFAULT (0),
	work_in_products INTEGER DEFAULT (0),
	create_truck_tasks INTEGER DEFAULT (0),
	work_in_truck_tasks INTEGER DEFAULT (0)
);
