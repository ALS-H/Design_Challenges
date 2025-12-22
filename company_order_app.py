"""
Classes:
1.Company
2.Item
3.Customer 
4.RegisteredCustomer
5.Order
6.OrderDetails

Relationships and Cardinality:
1.RegisteredCustomer-> IS-A Customer (Inheritance) 
2.Company-> Item (aggregation) (1 ─ 0..*)
3.Customer - Order (association)  (1 ─ 0..*)
4.Order -> OrderDetails (composition)   (1..* ─ 1..*)  
5.Item - OrderDetail (association)  (1-0..*) [One item can appear in many order details, Each order detail refers to exactly one item]
"""

