# Objective:
# The aim of this assignment is to apply the concepts of relational database design, normalization,
# and entity-relationship modeling to create an efficient and structured database for a 
# bookstore management system, "BookHaven."

# Problem Statement:
# "BookHaven" is facing challenges in managing its extensive collection of books, author 
# information, customer data, and transaction records. The current system has issues 
# with data redundancy, inconsistency, and inefficient data retrieval. Your task is to 
# design a relational database that addresses these problems while ensuring data integrity and ease of access.

# Task 1: Database Schema Design

# Design a normalized database schema for "BookHaven."
# Identify and create tables such as Books, Authors, Customers, and Transactions.
# Define columns for each table with appropriate data types and constraints.
# Ensure that the schema adheres to at least the Third Normal Form (3NF).
# Expected Outcome:
# A well-structured database schema diagram or document outlining tables, columns, data types, 
# primary keys, foreign keys, and any relevant constraints.

# Task 2: Entity-Relationship Diagram (ERD) Creation

# Develop an ERD to visually represent the relationships between the tables in your schema.
# Highlight key relationships such as the link between Books and Authors, and Customers and Transactions.
# Use standard ERD notation to illustrate one-to-many and many-to-one relationships.
# Expected Outcome:
# A clear and detailed ERD that accurately reflects the relationships within the "BookHaven" database.

# Task 3: Implementing a Self-Referencing Relationship

# Within the Authors table, implement a self-referencing relationship to represent authors who have collaborated with each other.
# Add necessary columns to facilitate this relationship, like collaborator_id, and adjust your ERD accordingly.
# Expected Outcome:
# An updated Authors table structure includes a self-referencing relationship, along with a revised ERD showcasing this addition.

# Task 4: Database Normalization Analysis

# Provide a written analysis explaining how your schema design adheres to the principles of normalization.
# Discuss specific examples from your design that demonstrate 1NF, 2NF, and 3NF.
# Expected Outcome:
# A comprehensive analysis document explaining the normalization process applied to the "BookHaven" 
# database schema, with examples highlighting each normal form.