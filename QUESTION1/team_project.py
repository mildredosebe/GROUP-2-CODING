projects = [
    {"name": "AI App", "skills": {"python", "ml"}},
    {"name": "Web App", "skills": {"html", "css", "js"}}
]

teams = [
    {
        "name": "Team A",
        "skills": {"python", "ml", "sql"},
        "preferences": ["AI App"],
        "available": True
    },
    {
        "name": "Team B",
        "skills": {"html", "css", "js"},
        "preferences": ["Web App"],
        "available": True
    }
]

assignments = {}

for project in projects:
    best_team = None
    best_score = 0
    for team in teams:
        if team["available"] and project["skills"].issubset(team["skills"]):
            score = 1
            if project["name"] in team["preferences"]:
                score += 1
            if score > best_score:
                best_score = score
                best_team = team
    if best_team:
        assignments[project["name"]] = best_team["name"]
        best_team["available"] = False

        print(assignments)
