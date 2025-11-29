class ContentMetadata:
    def __init__(self, title, description, tags, difficulty_level):
        self.title = title
        self.description = description
        self.tags = tags
        self.difficulty_level = difficulty_level

    def get_metadata(self):
        return {
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "difficulty_level": self.difficulty_level
        }

    def update_metadata(self, title=None, description=None, tags=None, difficulty_level=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if difficulty_level is not None:
            self.difficulty_level = difficulty_level