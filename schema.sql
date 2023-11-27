DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password INTEGER NOT NULL,
    name TEXT,
    tag1 TEXT,
    tag2 TEXT,
    tag3 TEXT,
    currency INTEGER
);


DROP TABLE IF EXISTS tags;

CREATE TABLE tags
(
    tag_name TEXT PRIMARY KEY,
);

DROP TABLE IF EXISTS quests;

CREATE TABLE quests
(
    quest TEXT PRIMARY KEY,
    coin_reward INTEGER,
    tags TEXT
);

DROP TABLE IF EXISTS completed_quests;

CREATE TABLE completed_quests
(
    gun_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    description TEXT,
    gun_type TEXT,
    gun_price INTEGER,
    collection TEXT
);

DROP TABLE IF EXISTS shop;

CREATE TABLE cshop
(
    gun_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    description TEXT,
    gun_type TEXT,
    gun_price INTEGER,
    collection TEXT
);

INSERT INTO gunshop (name, price, description, gun_type, gun_price, collection)
VALUES
    ('Polymer KnifeTech Coated Knife', 4350, 'The knife in the BlastX Collection', 'Melee', 0, 'BlastX'),
    ('BlastX Frenzy', 2175, 'The Frenzy in the BlastX Collection', 'Pistol', 500, 'BlastX'),
    ('BlastX Spectre', 2175, 'The Spectre in the BlastX Collection', 'SMG', 1600, 'BlastX'),
    ('BlastX Phantom', 2175, 'The Phantom in the BlastX Collection', 'Rifle', 2900, 'BlastX'),
    ('BlastX Odin', 2175, 'The Odin in the BlastX Collection', 'Machine Gun', 3200, 'BlastX'),
    ('Elderflame Dagger', 4950, 'The dagger in the Elderflame Collection', 'Melee', 0, 'Elderflame'),
    ('Elderflame Frenzy', 2475, 'The Frenzy in the Elderflame Collection', 'Pistol', 500, 'Elderflame'),
    ('Elderflame Judge', 2475, 'The Judge in the Elderflame Collection', 'Shotgun', 1600, 'Elderflame'),
    ('Elderflame Vandal', 2475, 'The Vandal in the Elderflame Collection', 'Rifle', 2900, 'Elderflame'),
    ('Elderflame Operator', 2475, 'The Operator in the Elderflame Collection', 'Sniper Rifle', 5000, 'Elderflame'),
    ('Candy Cane', 2550, 'The knife in the Winterwunderland Collection', 'Melee', 0, 'Winterwunderland'),
    ('Winterwunderland Ghost', 1275, 'The Ghost in the Winterwunderland Collection', 'Pistol', 500, 'Winterwunderland'),
    ('Winterwunderland Marshal', 1275, 'The Marshal in the Winterwunderland Collection', 'Sniper Rifle', 1600, 'Winterwunderland'),
    ('Winterwunderland Phantom', 1275, 'The Phantom in the Winterwunderland Collection', 'Rifle', 2900, 'Winterwunderland'),
    ('Winterwunderland Vandal', 1275, 'The Vandal in the Winterwunderland Collection', 'Rifle', 2900, 'Winterwunderland');
