import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

import django
django.setup()


from app1.models import Student
from faker import Faker
from random import randint

obj = Faker()

def call(num):

    for i in range(num):
        rn = randint(1,1000)
        name= obj.name()
        marks= randint(40,99)
        city = obj.city()

        std1 = Student.objects.get_or_create(rn=rn, name=name, marks=marks, city=city)

def main():
    call(int(input("How Many Student do You Want to Add:")))

if __name__ == '__main__':
    main()
