# TDD Examples

## Example 0

```
Task: Implement a function to validate email addresses

RED:
- Write test: test_should_return_true_when_valid_email()
- Run tests → FAIL ✗

GREEN:
- Implement basic email validation
- Run tests → PASS ✓

REFACTOR:
- Extract regex pattern to constant
- Run tests → PASS ✓

RED:
- Write test: test_should_return_false_when_missing_at_symbol()
- Run tests → FAIL ✗

GREEN:
- Update validation logic
- Run tests → PASS ✓

...continue cycle...
```

## Example 1: String Calculator Kata

### Iteration 1: Empty String
```python
# test_calculator.py
def test_should_return_zero_when_empty_string():
    assert add("") == 0
```
**Run → FAIL ✗** (function doesn't exist)

```python
# calculator.py
def add(numbers):
    return 0
```
**Run → PASS ✓**

### Iteration 2: Single Number
```python
def test_should_return_number_when_single_number():
    assert add("1") == 1
```
**Run → FAIL ✗**

```python
def add(numbers):
    if numbers == "":
        return 0
    return int(numbers)
```
**Run → PASS ✓**

### Iteration 3: Two Numbers
```python
def test_should_return_sum_when_two_numbers():
    assert add("1,2") == 3
```
**Run → FAIL ✗**

```python
def add(numbers):
    if numbers == "":
        return 0
    parts = numbers.split(",")
    return sum(int(n) for n in parts)
```
**Run → PASS ✓**

**Refactor:** All tests still pass

---

## Example 2: User Authentication

### Iteration 1: Valid Credentials
```typescript
// auth.test.ts
describe('authenticate', () => {
  test('should return user when credentials are valid', async () => {
    const result = await authenticate('user@example.com', 'password123');
    expect(result).toHaveProperty('id');
    expect(result).toHaveProperty('email', 'user@example.com');
  });
});
```
**Run → FAIL ✗**

```typescript
// auth.ts
export async function authenticate(email: string, password: string) {
  // Hardcode for now - just make it pass
  return { id: 1, email };
}
```
**Run → PASS ✓**

### Iteration 2: Invalid Credentials
```typescript
test('should throw error when credentials are invalid', async () => {
  await expect(
    authenticate('user@example.com', 'wrongpassword')
  ).rejects.toThrow('Invalid credentials');
});
```
**Run → FAIL ✗**

```typescript
export async function authenticate(email: string, password: string) {
  if (password !== 'password123') {
    throw new Error('Invalid credentials');
  }
  return { id: 1, email };
}
```
**Run → PASS ✓**

**Refactor:** Move to database lookup, extract password verification

---

## Common Patterns

### Testing Edge Cases
1. **Empty/null input**
2. **Single element**
3. **Multiple elements**
4. **Boundary conditions** (max/min values)
5. **Invalid input**

### Test Organization
```
describe('FeatureName', () => {
  describe('methodName', () => {
    test('should do X when Y', () => { ... });
    test('should do A when B', () => { ... });
  });
});
```

### Mocking External Dependencies
```typescript
// Test with mock
test('should fetch user data', async () => {
  const mockFetch = jest.fn().mockResolvedValue({
    json: async () => ({ id: 1, name: 'Test' })
  });
  global.fetch = mockFetch;

  const user = await getUser(1);

  expect(user.name).toBe('Test');
  expect(mockFetch).toHaveBeenCalledWith('/api/users/1');
});
```

---

