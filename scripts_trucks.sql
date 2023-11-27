CREATE TABLE trucks (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	datetime_create INTEGER,
	description TEXT,
	id_status INTEGER,
	id_model_truck INTEGER,
	id_info INTEGER,
	FOREIGN KEY (id_status) REFERENCES tasks_status (id),
	FOREIGN KEY (id_model_truck) REFERENCES truck_models (id),
	FOREIGN KEY (id_info) REFERENCES trucks_info (id)
);
CREATE TABLE truck_models (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name_model TEXT,
	id_truck_factory INTEGER,
	id_region INTEGER,
	FOREIGN KEY (id_truck_factory) REFERENCES truck_factories (id),
	FOREIGN KEY (id_region) REFERENCES regions (id),
);
CREATE TABLE truck_factories1 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name_factory TEXT
);
CREATE TABLE truck_tasks_status (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_truck INTEGER,
	datetime_create INTEGER,
	id_task_name INTEGER,
	description TEXT,
	FOREIGN KEY (id_task_name) REFERENCES truck_task_names (id)
);
