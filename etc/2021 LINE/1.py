table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
# result = "HARDWARE"

job = ['SI', 'CONTENTS', 'HARDWARE', 'PORTAL', 'GAME']
job.sort()
job_lst = [0]*5

def solution(table, languages, preference):
    for i in languages:
        for j in range(len(table)):
            if i in table[j].split():
                table_score = len(table[j].split()) - table[j].split().index(i)
                lang_idx = languages.index(i)
                score = preference[lang_idx]*table_score
                for k in job:
                    if k == table[j].split()[0]:
                        job_lst[job.index(k)] += score
    answer = job[job_lst.index(max(job_lst))]
    return answer

solution(table,languages,preference)