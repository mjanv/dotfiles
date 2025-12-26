---
name: tdd
description: Implements features using Test-Driven Development methodology following the red-green-refactor cycle. Use when user explicitly requests TDD approach or asks to implement features test-first.
---

# Test-Driven Development (TDD)

Implement features following the strict Test-Driven Development methodology.

## Process

Follow the Red-Green-Refactor cycle for each feature or requirement:

1. **RED - Write ONE failing test**: Write the smallest possible test, with a descriptive name, that captures one aspect of the requirement. The test MUST fail initially (run it to verify). Focus on behavior and interface, not implementation.
2. **GREEN - Make it pass**: Write the minimal code needed to make the test pass. Don't worry about elegance yet - just make it work. Run the test to verify it passes. No extra features or "future-proofing".
3. **REFACTOR - Clean up**: Improve the code structure while keeping tests green. Remove duplication, improve naming and clarity. Run tests after each refactoring step to ensure they still pass

Continue with the next test case. Build functionality incrementally, one test at a time.

## Workflow

For each task:

1. **Analyze** the requirement and break it into small, testable behaviors
2. **Create todo list** with each behavior as a separate todo item
3. **For each behavior**, complete the red-green-refactor cycle and mark todo as completed
1. **Review** all tests pass and code is clean

## Key principles

- **Unit tests first**: Start with isolated unit tests, never write code without a failing test
- **One assertion per test**: Keep tests focused, write only enough code to pass the current test
- **Test behavior, not implementation**: Don't test private methods
- **Fast independents tests**: Tests should run quickly and not depend on each other
- **Always run tests after changes**
- **Descriptive names**: Use a test name describing the business behavior
- **Keep the cycle fast**: Each red-green-refactor cycle should be quick (minutes, not hours)

## Anti-Patterns to avoid

- **Writing multiple tests before implementation**: Stick to one test at a time
- **Writing production code without a test**: Always write the test first
- **Making tests pass by changing the test**: Fix the implementation, not the test
- **Skipping the refactor step**: Clean code is essential to maintainability

## Additional Resources

See [examples.md](examples.md) for detailed TDD examples and common patterns.
