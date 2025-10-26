# 🧭 Naming Guidelines

> Consistent and meaningful naming improves readability, discoverability, and long-term maintainability of the project.
> Naming is not just convention — it’s design. Each name conveys purpose, structure, and intent.

---

## 1. General Principles

✅ Each name should:

1. **Reflect meaning, not mechanics**
   - `send_confirmation_email()` ✅  
     `do_email_stuff()` ❌
2. **Be specific to its role or domain**
   - `UserSessionManager` ✅  
     `Manager` ❌
3. **Be pronounceable and readable**
   - `user_profile` ✅  
     `usrprf` ❌
4. **Be consistent with conventions**
   - `snake_case` for functions and variables
   - `PascalCase` for classes
   - `SCREAMING_SNAKE_CASE` for constants
5. **Be self-documenting**
   - Names should make the code understandable without extra comments.
6. **Avoid redundancy and stuttering**
   - `User.user_name` → redundant. Prefer `User.name`.

---

## 2. Project / App / Directory Level

These names represent **domain boundaries** or **subsystems**.

| ✅ Good                                 | 🚫 Bad                    | Why                                                    |
| --------------------------------------- | ------------------------- | ------------------------------------------------------ |
| `billing`, `inventory`, `notifications` | `utils`, `misc`, `common` | Reflect a real domain area, not a technical catch-all. |
| `auth`, `api`, `dashboard`              | `stuff`, `backend`        | Each app name implies clear purpose.                   |

**Checklist**

- [ ] Represents a clear bounded context or domain.
- [ ] Scope of responsibility is obvious.
- [ ] Naming scheme (singular/plural) is consistent across apps.

---

## 3. Modules and Packages

Organize related logic or services inside each app.

| ✅ Good                                                             | 🚫 Bad                      |
| ------------------------------------------------------------------- | --------------------------- |
| `models`, `views`, `forms`, `services`, `repositories`, `selectors` | `helpers`, `extra`, `stuff` |
| `payment_gateway.py`, `email_sender.py`                             | `code.py`, `logic.py`       |

**Checklist**

- [ ] Describes what the module _contains_ or _does_.
- [ ] Aligns with project-wide architecture patterns.
- [ ] Avoid ambiguous files like `utils.py` — prefer domain-specific ones.

---

## 4. Classes (Models, Forms, Serializers, Services)

Classes represent **entities**, **value objects**, or **roles**.

| ✅ Good                                      | 🚫 Bad                                    |
| -------------------------------------------- | ----------------------------------------- |
| `UserProfile`, `OrderItem`, `PaymentService` | `DoPayment`, `HandlerThing`, `DataHolder` |

**Checklist**

- [ ] Is it a **noun**, not a verb phrase?
- [ ] Conveys its domain role (e.g. `Repository`, `Service`, `Form`).
- [ ] Concise but expressive — `InvoiceProcessor` > `InvoiceProcessingManagerService`.
- [ ] Avoid repeating the app name (`users.UserModel` → redundant).

---

## 5. Functions and Methods

Functions describe **actions, behaviors, or transformations**.

| ✅ Good                                                   | 🚫 Bad                                    |
| --------------------------------------------------------- | ----------------------------------------- |
| `calculate_total()`, `send_email()`, `get_user_profile()` | `total_calc()`, `do_stuff()`, `handler()` |

**Checklist**

- [ ] Verb phrase (“do something”).
- [ ] Describes _what_ it does, not _how_.
- [ ] `get_`, `fetch_`, `build_` → return values.
- [ ] `send_`, `update_`, `delete_` → perform side effects.
- [ ] No internal implementation details in name.

---

## 6. Variables and Constants

Variables hold **state**; constants define **fixed values**.

| ✅ Good                                                        | 🚫 Bad                  |
| -------------------------------------------------------------- | ----------------------- |
| `total_amount`, `user_count`, `MAX_RETRIES`, `DEFAULT_TIMEOUT` | `t`, `val`, `temp`, `x` |

**Checklist**

- [ ] Clearly describes the represented value.
- [ ] Contextually unambiguous (`user_count`, not just `count`).
- [ ] Constants use SCREAMING_SNAKE_CASE.
- [ ] Avoid cryptic abbreviations unless universally known (`id`, `url`, `db`).

---

## 7. Templates, HTMX Endpoints, and Frontend Fragments

Consistency matters between templates, views, and HTMX calls.

| ✅ Good                                         | 🚫 Bad                       |
| ----------------------------------------------- | ---------------------------- |
| `user_list_fragment.html`, `order_details.html` | `partial.html`, `thing.html` |
| `hx-get="/orders/{id}/details"`                 | `hx-get="/data/stuff"`       |

**Checklist**

- [ ] Template name matches what it renders.
- [ ] HTMX endpoint name describes its intent (`/users/list/fragment`).
- [ ] Keep naming consistent across HTML, views, and JS.

---

## 8. Django Views and URLs

Views represent **actions or endpoints**; URLs represent **resources**.

| ✅ Good                                | 🚫 Bad               |
| -------------------------------------- | -------------------- |
| `def user_list_view(request):`         | `def list(request):` |
| `/users/`, `/orders/<int:id>/details/` | `/data/`, `/stuff/`  |

**Checklist**

- [ ] View names show _what_ and _how_ they serve (`create_user_view`, `order_detail_view`).
- [ ] URL path mirrors resource name.
- [ ] No generic names reused across apps.

---

## 9. Tests

Tests act as **living documentation**.

| ✅ Good                                        | 🚫 Bad                     |
| ---------------------------------------------- | -------------------------- |
| `test_user_creation_sends_welcome_email()`     | `test_1()`, `test_email()` |
| `test_invalid_login_redirects_to_error_page()` | `test_login()`             |

**Checklist**

- [ ] Describes behavior under test (Given–When–Then style).
- [ ] Group related tests in well-named classes (`class TestUserRegistration:`).
- [ ] Avoid overly generic names.

---

## 10. Evaluate Alternatives

Before finalizing any name:

- [ ] Consider at least **two alternative names**.
- [ ] Choose the one balancing expressiveness, readability, and brevity.
- [ ] Does the name make sense _without_ reading its implementation?
- [ ] Would another developer immediately understand its purpose?

---

## 11. When Naming Feels Hard…

> If you can’t name it clearly, you probably don’t understand it yet.

Write a one-sentence explanation of what the entity _is_ or _does_.
The right name usually emerges from that sentence.

---

## 12. Quick Reference Summary

| Entity Type       | Naming Style                     | Describes                    |
| ----------------- | -------------------------------- | ---------------------------- |
| App / Package     | lowercase_with_underscores       | Domain or subsystem          |
| Module            | lowercase_with_underscores       | Purpose of code inside       |
| Class             | PascalCase                       | Entity, object, or role      |
| Function / Method | snake_case                       | Action or behavior           |
| Variable          | snake_case                       | State or data                |
| Constant          | SCREAMING_SNAKE_CASE             | Fixed configuration or limit |
| Template          | lowercase_with_underscores.html  | Rendered content             |
| Test              | snake*case starting with `test*` | Expected behavior            |

---

**Remember:**

> Names are the user interface of your code.  
> Choose them with the same care you design your APIs and UIs.
