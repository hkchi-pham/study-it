# Database Selection/Comparison

This document compares different databases (**MySQL, MariaDB, PostgreSQL, MongoDB, LiteQL**) to select the most suitable one for the **AI Companion Chatbot project**.  

---

## 🔎 Database Comparison

### 1. MySQL
- **Type:** SQL (RDBMS)  
- **Performance:** Fast for relational queries, slower for JSON operations.  
- **Soft Delete:** Supported via `is_deleted` or `deleted_at` field.  
- **History/Audit:** Implemented with triggers or separate audit tables.  
- **Pros:** Widely used, easy to deploy, strong community support.  
- **Cons:** Limited horizontal scaling, weaker JSON handling.  

---

### 2. MariaDB
- **Type:** SQL (RDBMS, fork of MySQL)  
- **Performance:** Optimized for JSON + analytical queries.  
- **Soft Delete:** Supported via flags.  
- **History/Audit:** Built-in **MariaDB Audit Plugin**.  
- **Pros:** Fully open-source, faster JSON support than MySQL.  
- **Cons:** Less popular than MySQL, smaller ecosystem.  

---

### 3. PostgreSQL
- **Type:** SQL + Semi-SQL (JSONB, HSTORE)  
- **Performance:**  
  - Strong for relational queries.  
  - JSONB operations are efficient, sometimes faster than MongoDB.  
- **Soft Delete:** Supported (`deleted_at`, `is_deleted`).  
- **History/Audit:** Strong support via **pgAudit**, triggers, and extensions.  
- **Pros:**  
  - Hybrid: works well with relational + JSON data.  
  - Powerful ecosystem (PostGIS, TimescaleDB, full-text search).  
- **Cons:** More complex administration than MySQL.  

---

### 4. MongoDB
- **Type:** NoSQL (Document-oriented)  
- **Performance:**  
  - Excellent for JSON/document storage.  
  - Fast inserts and queries for chat logs.  
- **Soft Delete:** Simple with an `is_deleted` flag.  
- **History/Audit:** Supports **Change Streams** and **Oplog** for auditing.  
- **Pros:**  
  - Flexible schema, great for chat/conversation history.  
  - Easy to scale horizontally.  
- **Cons:** Weaker for complex transactions and strong relational queries.  

---

### 5. LiteSQL / LiteDB
- **Type:** Semi-SQL / Embedded DB (depending on implementation).  
- **Performance:** Very fast locally, but limited scaling.  
- **Soft Delete:** Manual implementation.  
- **History/Audit:** Weak support, needs custom implementation.  
- **Pros:** Lightweight, great for prototyping.  
- **Cons:** Not suitable for production chatbot with many users.  

---

## 📌 Project Requirements

For the **AI Companion Chatbot**, the database must:  
1. Store **user profiles** (structured, relational).  
2. Store **conversation history** (JSON or document-based).  
3. Support **soft delete & audit logging**.  
4. Scale to handle many concurrent users.  

---

## ✅ Best Consideration

- **Single Choice:**  
  - **PostgreSQL** – balances relational data (profiles, audit) with JSONB (conversation history).  

- **Hybrid Choice:**  
  - **PostgreSQL** for user profiles, audit, and structured data.  
  - **MongoDB** for chat logs and flexible conversation storage.  

---

## 🗂️ Example Schema (PostgreSQL)

```sql
-- User profile
CREATE TABLE users (
  id UUID PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE,
  gender TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  created_by UUID,
  updated_at TIMESTAMP DEFAULT NOW(),
  updated_by UUID,
  deleted_at TIMESTAMP,
  is_deleted BOOLEAN DEFAULT FALSE,
);

-- Conversation history (JSONB)
CREATE TABLE conversations (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  messages JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  deleted_at TIMESTAMP,
  is_deleted BOOLEAN DEFAULT FALSE
);

-- Audit log
CREATE TABLE audit_logs (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  action TEXT NOT NULL,
  details JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
