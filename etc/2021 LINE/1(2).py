table = [i.split() for i in ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
# result = "HARDWARE"

job = ['SI', 'CONTENTS', 'HARDWARE', 'PORTAL', 'GAME']
job.sort()
job_lst = [0]*5

def solution(table, languages, preference):
    for i in languages:
        for j in table:
            if i in j:
                table_score = len(j) - j.index(i)
                lang_idx = languages.index(i)
                score = preference[lang_idx]*table_score
                for k in job:
                    if k == j[0]:
                        job_lst[job.index(k)] += score
    answer = job[job_lst.index(max(job_lst))]
    return answer

print(solution(table,languages,preference))