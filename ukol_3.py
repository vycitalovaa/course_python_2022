import json
with open ('course_python_2022/body.json', encoding='utf-8') as file:
    points = json.load(file)
prospel = 0
prospech = {}
for jmeno, body in points.items():
    if body >= 60:
        prospel = "pass"
        prospech[jmeno] = prospel
    else:
        prospel = "fail"
        prospech[jmeno] = prospel
print(prospech)
with open ("prospech.json", mode="w", encoding="utf-8") as output_file:
    json.dump(prospech, output_file, ensure_ascii=False)