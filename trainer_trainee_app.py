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
1. Trainer -> Course, association       (1-1..*)
2. Trainer -> Trainee, association      (1-1..*)
3. Course -> Technology, aggregation    (1-1..*)
4. Course -> Module , composition  (1-1..*)
5. Module -> Unit, composition     (1-1..*)
6. Unit -> Topic,composition      (1-1..*)

"""

