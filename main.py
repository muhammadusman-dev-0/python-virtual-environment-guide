import students
import random
import requests

print("===== STUDENT INFORMATION =====")
students.show_student()

print("\nRandom Number:", random.randint(1, 100))
print("\nRequests Version:", requests.__version__)
