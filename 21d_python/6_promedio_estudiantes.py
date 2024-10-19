grade_list = [
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
]

def get_student_average(input):
  output = {}
  students = []
  class_average = 0
  average_counter = 0
  
  for item in input:
    entry = {}
    entry["name"] = item["name"]
    entry["average"] = round(sum(item["grades"])/len(item["grades"]),2)
    students.append(entry)
  
  for item in students:
    average_counter += item["average"]

  class_average = round(average_counter/len(students),2)
  output["class_average"] = class_average
  output["students"] = students

  return output

print(get_student_average(grade_list))

'''
Output
  "class_average": 88.17,
  "students": [
    {
      "name": "Pedro",
      "average": 88.75
    },
    {
      "name": "Jose",
      "average": 88.5
    },
    {
      "name": "Maria",
      "average": 87.25
    }
  ]
'''