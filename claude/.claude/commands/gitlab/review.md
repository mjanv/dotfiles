---
description: Review a GitLab merge request
argument-hint: [mr-number]
---

# GitLab Merge Request Review

You are reviewing merge request: **!$ARGUMENTS**

Follow this workflow to perform a comprehensive code review:

## Phase 1: Extract MR Information

1. **Determine the current GitLab project** from your working directory
2. **Fetch MR details** using the gitlab skill:
   - Get MR metadata: number, title, description, author, created date, updated date
   - Get source branch and target branch names
   - Get commit count and file changes
   - Get linked issues (Jira tickets)
   - Get pipeline status if available
   - Get comments and discussions

3. **Create report file** named `MR-$ARGUMENTS-review.md` in output directory:
   ```markdown
   # MR !$ARGUMENTS - [Title]

   - Author: [author name]
   - Created: [date]

   ## Description
   [Full MR description]
   ```

## Phase 2: Get Linked Jira Ticket Information

1. **Extract Jira ticket key** from MR description or linked issues
2. **Use jira skill** to fetch, if possible, ticket details (Summary, status, priority, type,...)
3. **Document in report**

## Phase 3: Fetch and Checkout Branch

Fetch the latest changes and checkout the MR branch:

```bash
git checkout master
git fetch origin [source-branch-name]
git checkout [source-branch-name]
```

## Phase 4: Perform code review using git diff

1. **Generate comprehensive diff** against target branch:
   ```bash
   git diff origin/[target-branch]..HEAD
   ```

2. **Analyze the changes**:
   - Files modified and their purpose
   - Lines added/removed
   - Code patterns and style consistency
   - Import/dependency changes
   - Test coverage changes
   - Configuration changes

3. **Look for issues**:
   - Potential bugs or logic errors
   - Security vulnerabilities (SQL injection, XSS, hardcoded secrets, etc.)
   - Performance concerns (N+1 queries, unnecessary loops, etc.)
   - Code quality issues (duplication, unclear logic, missing error handling)
   - Style and consistency violations
   - Missing tests or inadequate coverage
   - Breaking changes without documentation

4. **Document findings in report**:

```markdown
## Code Review

### Overview
- Files changed: [list]
- Primary changes: [high-level summary]

### What's Good 
- [positive observation 1]
- [positive observation 2]

### Issues Found
- **[Severity: Critical/Major/Minor]** - [file:line] [issue description]
   - Impact: [what could go wrong]
   - Suggested fix: [recommendation]

### Security Considerations
- [any security implications or concerns]

### Performance Considerations
- [any performance implications or concerns]

### Testing
- [test coverage assessment]
- [test quality observations]
```

## Important Notes

- **Be constructive**: Frame feedback to help improve code quality
- **Be specific**: Reference exact line numbers and code snippets
- **Security first**: Always check for security vulnerabilities
- **Performance matters**: Consider scalability and efficiency
- **Test coverage**: Ensure adequate testing for new functionality
- **Clear communication**: Use the report as a discussion starter, not final verdict
- **Document reasoning**: Explain *why* something is an issue, not just *what* is wrong

## Review Quality Criteria

A good review identifies:
1. Bugs and logic errors that would cause failures
2. Security vulnerabilities (OWASP Top 10)
3. Performance issues (database queries, memory usage)
4. Code quality problems (maintainability, clarity)
5. Test coverage gaps
6. Documentation gaps
7. Style inconsistencies
