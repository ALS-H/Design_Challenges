"""
Classes:
1.Company
2.Item
3.Customer 
4.RegisteredCustomer
5.Order

Relationships and Cardinality:
1.RegisteredCustomer-> IS-A Customer (Inheritance) 
2.Company-> Item (aggregation) (1 ─ 0..*)
3.Customer-> Order (association)  (1 ─ 0..*)
4.Order-> Item (association)   (1..* ─ 1..*)  [an item can appear in many orders]
"""

