# Software QA Portfolio

**Anara Ashmukhanbetova**  
**Manual Testing | REST API Testing | Postman Test Automation | SQL**

Training and project-based QA work with documented evidence. Projects include reproducible manual tests, defect investigations, and automated REST API checks in Postman.

## Featured Work

### 1. Recruitment API — End-to-End Automated Checks (Postman)
- [Postman collection](api-testing/recruit-e2e-v2.postman_collection.json) — 14 linked API requests, dynamic IDs, authentication and cleanup.
- **116 automated Postman checks passed; 0 failed** in the recorded Collection Runner execution (November 19, 2026).
- [Sanitized test execution results](api-testing/recruit-e2e-v2-test-run-results.json), including request-level evidence.
- Tools: Postman, JavaScript `pm.test()` / `pm.expect()`, REST, JSON and environment variables.

### 2. Scientific Calculator — Manual UI Testing
- [Manual test cases and observed results](manual-testing/calculator/test-cases.md) — two responsive viewport scenarios, both linked to recorded evidence.
- [Bug report with screenshots](manual-testing/calculator/bug-report-01.md) — nonresponsive buttons investigated with Chrome DevTools and Safari Web Inspector.
- **Scope:** Button failures were observed in Chrome; Safari was used for element inspection, not confirmed defect reproduction. Chrome version was not recorded; no fix retest claimed.

### 3. Swagger Petstore — API Testing
- [Postman collection](api-testing/swagger-petstore.postman_collection.json) and [environment example](api-testing/petstore.postman_environment.json).
- Create/update/delete and image-upload exercises, including HTTP 404 and 415 investigations.
- [API project documentation and run instructions](api-testing/README.md).

## Skills & Tools

- **Manual QA:** functional and responsive UI testing, writing and executing test cases, documenting defects, Jira coursework.
- **API QA & automation:** Postman, REST requests, HTTP status codes, JSON validation, JavaScript-based automated Postman checks, Collection Runner.
- **Investigation & data:** Chrome DevTools, Safari Web Inspector, HTML/CSS fundamentals, SQL, Git/GitHub.
- **Currently learning:** Python, pytest, Playwright with Python, AI-assisted testing.

## What Is Not Yet Published

A runnable Python/Playwright UI automation framework and standalone CI/CD workflow are **not yet** part of this public portfolio. The published automated checks are in Postman.

> Evidence is limited to observed test executions and documented artifacts; unverified browser coverage or post-fix retests are not claimed.
