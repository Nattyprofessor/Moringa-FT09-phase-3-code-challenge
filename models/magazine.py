class Magazine:
    def __init__(self, id, name, category=None):
        # If category is not provided, set it to a default value
        self.id = id
        self.name = name
        self.category = category if category else 'Uncategorized'  # Use a default category if not provided

    def __repr__(self):
        return f'<Magazine {self.name}>'
