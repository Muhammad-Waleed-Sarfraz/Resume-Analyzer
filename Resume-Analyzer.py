print("-----Welcome To Resume Analyzer Who Helps You To Draft A Strong Winning Resume----")
skill_input = input("Paste your required set of skills (Seperate each by Comma) : ").lower()
resume_data = input("Paste your resume data here : ").lower()
required_skill = skill_input.split(",")
score = 0
found_skills = []
missing_skills = []
for skill in required_skill:
    clean_skill = skill.strip()
    if clean_skill in resume_data:
        score += 1
        found_skills.append(skill)
    else:
        missing_skills.append(skill)
ATS_Score = (score/len(required_skill))*100
print("After a crefull analysis of your resume we found that you have the",found_skills," skills which matches the required set of skill and " \
"you have a lack of",missing_skills,"skills and your final score is",ATS_Score)