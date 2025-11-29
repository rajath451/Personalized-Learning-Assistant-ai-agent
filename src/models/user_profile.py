class UserProfile:
    def __init__(self, user_id, name, preferences=None):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences if preferences is not None else {}

    def update_preferences(self, new_preferences):
        self.preferences.update(new_preferences)

    def get_profile_info(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "preferences": self.preferences
        }