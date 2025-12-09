class Subject:
    code: str
    name: str
    credits: int
    correlatives: list[str]
    semester: int
    is_elective: bool = False
    required_credits: int
    is_approved: bool = False
    course_grade: float | None = None
    final_grade: float | None = None

    def __init__(self, name: str, code: str, credits: int, correlatives: list[str], semester: int, is_elective: bool, required_credits: int):
        self.name = name
        self.code = code
        self.credits = credits
        self.correlatives = correlatives
        self.semester = semester
        self.is_elective = is_elective
        self.required_credits = required_credits
    
    def __repr__(self) -> str:
        return f"Subject(name={self.name}, code={self.code}, credits={self.credits}, correlatives={self.correlatives}, semester={self.semester}, is_elective={self.is_elective}, required_credits={self.required_credits})"
    
    
