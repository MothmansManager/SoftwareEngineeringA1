DROP TABLE IF EXISTS tags;

CREATE TABLE tags
(
    tagName TEXT PRIMARY KEY,
    task1 TEXT,
    task2 TEXT,
    task3 TEXT
);

INSERT INTO tags (tagName, task1, task2, task3)
VALUES
    ('Student', 'How about you work on Assignments you have to submit soon!', 'Keep yourself up to date on study!', "Keep your workspace tidy!"),
    ('Teacher', "Grade assignments", "Get a start on new lesson plans!", "Plan something exciting for your next lesson!"),
    ('Pet Owner', "Play with your pet and give them your undivided attention for a while!", "Might be time to give your pet a bath!", "Don't forget to refill your pets commodities like food and water!!"),
    ('Artist', "Start on a new Project", "Work on a new Original Character!!", "Do some anatmoy practice :)"),
    ('Reading', "Start reading a new book", "Read your favourite book/book series", "Write an analysis on the last book you read!"),
    ('Sports/Gym', "Go to the gym", 'Play your favouite sport', 'Get yourself some new sports gear/gym gear'),
    ('Author', "Work on your manuscript", "Review your last written work", "Get some feed back from your author friends!"),
    ('Garden', "Weed the garden", "Buy new gardening tools", "Plant seeds"),
    ('Crochet', "Make a hat", "Buy new yarn", "Start a new gift project"),
    ('Dentist', "Organise Appointments", "Eat teeth", "Fight the tooth fairy");