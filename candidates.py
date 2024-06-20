required_skills = ["python", "github", "linux"]

candidates = {
    "anna": {"java", "linux", "windows", "github", "python", "full stack"},
    "bob": {"github", "linux", "python"},
    "carol": {"linux", "javascript", "html", "python", "github"},
    "daniel": {"pascal", "java", "c++", "github"},
    "ekani": {"html", "css", "github", "python", "linux"},
    "fenna": {"linux", "pascal", "java", "c", "lisp", "modula-2", "perl", "github"},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    #     interviewees.add(candidate)

    # Check for PROPER superset (more skills than required_skills)
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)

# Checking if skills (values in dict) are a SUPERSET of required_skills
# i.e. if a set (skills) contains all the items (required_skills) of another set, its a SUPERSET
