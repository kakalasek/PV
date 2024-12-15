class SchoolProfile():

    def __init__(self, name, surname, username, favorite_school_subject, favorite_school, favorite_teacher):
        self.name = name
        self.surname = surname
        self.username = username
        self.favorite_school_subject = favorite_school_subject
        self.favorite_school = favorite_school
        self.favorite_teacher = favorite_teacher

    def __repr__(self):
        return f"""
                {self.name}
                {self.surname}
                {self.username}
                {self.favorite_school_subject}
                {self.favorite_school}
                {self.favorite_teacher}
                """
