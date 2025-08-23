# Database
---

## 1. UUID (Universally Unique Identifier)

### What is UUID?
- A **128-bit identifier** that is statistically unique across space and time.  
- Common format:  550e8400-e29b-41d4-a716-446655440000


### Why use UUID?
- **Universal uniqueness** → prevents collisions across distributed systems or microservices.  
- **Security** → UUIDs are harder to guess than sequential IDs.  
- **Scalability** → multiple servers can generate UUIDs independently without coordination.  

### Types of UUID (commonly used versions)
- **UUID v1**: Based on timestamp + MAC address (ordered but reveals machine/time info).  
- **UUID v4**: Randomly generated (122 bits of randomness, 6 bits for version/variant, collision probability ≈ zero).  
- **UUID v5**: Hash-based (namespace + name → deterministic unique ID).  

### Collision Probability
- With UUID v4, the chance of a collision is practically **zero**, even when generating **1 billion UUIDs per second for 100 years**
- That’s why UUIDs are considered “unique enough” for production systems.

---

## 2. Entities from Functional Requirements

From the chatbot’s features, we can identify key **entities** in the database:

- **User**: Teenager or admin using the app.  
- **ChatSession**: A conversation session (linked to persona: listener, peer, mentor).  
- **Message**: Individual messages between user and chatbot.  
- **MoodCheckin**: Daily mood tracking entry.  
- **Activity / Mini-game**: Breathing, journaling, affirmation, garden.  
- **Achievement**: Rewards for streaks, consistency, or positive actions.  

Each entity should have a **UUID primary key**.

---

## 3. User Table Design

### Basic Fields
| Field | Type | Description |
|-------|------|-------------|
| `user_id` (PK) | UUID | Unique user ID |
| `username` | VARCHAR | Display name |
| `password_hash` | VARCHAR | Encrypted password |
| `email` | VARCHAR (unique) | Login email (optional for anonymity) |
| `phone` | VARCHAR (optional) | Contact number |
| `age` | INT | Age |
| `gender` | ENUM | Gender or "prefer not to say" |
| `preferred_language` | ENUM('vi','en') | Language preference |
| `status` | ENUM('active','inactive','deleted') | Account status |

### Audit Fields
| Field | Type | Description |
|-------|------|-------------|
| `created_at` | TIMESTAMP | When the user was created |
| `created_by` | UUID | Who created the account (self or admin) |
| `modified_at` | TIMESTAMP | Last modification time |
| `modified_by` | UUID | Who modified it last |
| `deleted_at` | TIMESTAMP (nullable) | When the account was deleted |
| `deleted_by` | UUID (nullable) | Who deleted the account |
| `is_deleted` | BOOLEAN (default: false) | Soft delete flag |

---

## 4. Why Do We Need Audit Fields?

### `created_at` / `created_by`
- Tracks when and by whom the account was created.
- Useful for onboarding analytics and admin-created accounts.

### `modified_at` / `modified_by`
- Records the last update and who made it.
- Ensures accountability, especially in multi-admin systems.

### `deleted_at` / `deleted_by` / `is_deleted`
- Enables **soft deletion** (disable account without losing history).  
- Supports **data recovery** if the user wants to return.  
- Allows **analytics** (user churn, lifetime users).  
- Provides **transparency** in case of admin intervention.

---



