"""
Identifying the classes:
1.Trainer
2.Trainee
3.Technology
4.Course
5.Module
6.Unit
7.Topic

Identifying the relationships:
Only Has-A relationships
        Relationship                     Cardinality
1. Trainer -> Course, association       (1-0..*)
2. Trainer -> Trainee, association      (1-0..*)
3. Technology-> Course, association    (1-0..*) [on a given technology in this course] 
[technology is never owned by a course but can be used by 0 or more courses]
4. Course -> Module , composition  (1-1..*) [the course contains many modules so implies at least 1]
5. Module -> Unit, composition     (1-1..*) [each module comprised of diff units]
6. Unit -> Topic,composition      (1-1..*) [each unit has many topics]

"""

