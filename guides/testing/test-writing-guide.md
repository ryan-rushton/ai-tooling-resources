# Test Writing Guide (Unit & Integration)

This guide provides comprehensive instructions for LLM-backed tools on how to write effective unit and integration tests by combining established patterns with best practices.

## Core Approach

### 1. Pattern Discovery and Analysis
**Always start by understanding existing test patterns before writing new tests.**

- **Search Strategy**: Use specific search commands to find test files:
  - Start with `find . -name "*.test.*" -o -name "*.spec.*" -o -name "*Test.*"` in the target directory
  - Search for test directories: `find . -type d -name "test*" -o -name "spec*" -o -name "__tests__"`
  - Expand search to parent directories if fewer than 3 test files found
  - Look for testing configuration files: `package.json`, `jest.config.js`, `pytest.ini`, `build.gradle`
- **Pattern Analysis**: Review at least 3 existing test files, prioritizing those that mock or inject similar dependencies
- **Convention Identification**: Look for:
  - Naming conventions (test file names, test method names)
  - Directory structure patterns
  - Import/dependency injection patterns
  - Mock setup patterns
  - Assertion styles

### 2. Test Structure Review
**Understand the existing test architecture before adding new tests.**

- **Framework Identification**: Determine which testing framework is being used by examining:
  - Package.json dependencies: `grep -E "jest|mocha|jasmine|vitest" package.json`
  - Python requirements: `grep -E "pytest|unittest|nose" requirements.txt setup.py`
  - Java build files: `grep -E "junit|testng" build.gradle pom.xml`
  - Config files: Look for `jest.config.js`, `pytest.ini`, `karma.conf.js`
- **Test Organization**: Identify how tests are grouped (describe/context blocks, test classes, modules)
- **Setup Patterns**: Look for common setup/teardown patterns, fixtures, and test data management
- **Consistency Goals**: Ensure new tests match existing structure for maintainability

### 3. Iterative Development
**Build tests incrementally to ensure each step works correctly.**

- **Test File Skeleton**: Start by creating a test file with a simple "hello world" style test that verifies basic functionality:
  - For React/Vue components: `it('renders', () => { ... })`
  - For TypeScript modules/functions: `it('produces output', () => { ... })`
  - For Java classes: `it('generates expected output', () => { ... })`
  - For API endpoints: `it('responds', () => { ... })`
- **Basic Validation**: Run this skeleton test to ensure the testing infrastructure works:
  - Identify test command: Check `package.json` scripts, `Makefile`, or `README.md` for test commands
  - Common commands: `npm test`, `yarn test`, `pytest`, `mvn test`, `gradle test`
  - If test fails to run, check for missing dependencies or incorrect paths
  - Verify test file is in correct location (same directory as source, `__tests__` folder, etc.)
- **Single Test Focus**: Build one meaningful test at a time after the skeleton
- **Validation**: Run each test to ensure it passes before proceeding
- **Incremental Addition**: Add one test at a time, running the test suite between each addition
- **Human-Like Chunking**: Break complex testing scenarios into logical chunks that can be verified independently

### 4. Failure Resolution Protocol
**Handle test failures systematically and know when to ask for help.**

- **Context Gathering**: When a test fails, collect full context on:
  - Mock configurations and return values
  - Dependency injection setup
  - Test data and fixtures
  - Error messages and stack traces
- **Systematic Debugging**: Analyze what the error indicates and form hypotheses
- **Three-Attempt Rule**: Make up to 3 focused attempts to resolve the issue:
  - Attempt 1: Address the direct error message (missing imports, syntax errors, etc.)
  - Attempt 2: Check mock setup, test data, and environment configuration
  - Attempt 3: Review test structure and assertions for logical errors
  - Each attempt should focus on one specific aspect of the problem
- **Human Escalation**: If unable to resolve after 3 attempts, ask for human assistance with full context

### 5. Code Review and Refactoring
**Always review completed tests for quality and maintainability.**

- **Duplication Detection**: Look for nearly identical tests that should be merged
- **Common Setup**: Extract repeated setup code into helper methods or fixtures
- **Test Data**: Consolidate similar test data into reusable fixtures
- **Assertion Patterns**: Ensure consistent assertion styles across tests

### 6. Test File Placement and Naming
**Determine correct test file location and naming conventions.**

- **Location Discovery**: Identify test file placement patterns:
  - Same directory as source: `MyComponent.tsx` → `MyComponent.test.tsx`
  - Dedicated test directory: `src/components/MyComponent.tsx` → `src/components/__tests__/MyComponent.test.tsx`
  - Mirror source structure: `src/utils/helper.js` → `test/utils/helper.test.js`
- **Naming Convention Analysis**: Look for existing patterns:
  - Extensions: `.test.js`, `.spec.js`, `.test.tsx`, `Test.java`
  - Prefixes/suffixes: `test_`, `Test`, `Spec`
- **Import Path Resolution**: Determine correct import syntax:
  - Relative imports: `import { MyComponent } from './MyComponent'`
  - Absolute imports: `import { MyComponent } from '@/components/MyComponent'`
  - Check `tsconfig.json`, `jest.config.js`, or `webpack.config.js` for path mapping

### 7. Documentation Standards
**Write clear, behavior-focused comments using structured patterns.**

- **Given-When-Then Structure**: Use these indicators to clarify test intent:
  - `// Given: [initial state/setup]`
  - `// When: [action being tested]`  
  - `// Then: [expected outcome]`
- **Behavior Focus**: Document why the test exists, not just what it does
- **Self-Documenting Code**: Prefer clear variable names and test names over extensive comments
- **Essential Only**: Only comment on behavior that isn't obvious from reading the code

## Handling Edge Cases and Missing Infrastructure

### No Existing Tests Scenario
**When no test files exist in the project:**

- **Framework Selection**: Choose framework based on project type:
  - Node.js projects: Default to Jest unless React (use React Testing Library + Jest)
  - Python projects: Default to pytest unless Django (use Django test framework)
  - Java projects: Default to JUnit 5 unless Spring (use Spring Boot Test)
- **Initial Setup**: Create minimal test configuration if missing
- **Directory Structure**: Create standard test directory structure
- **First Test**: Start with simplest possible test to validate setup

### Missing Dependencies Scenario
**When test infrastructure is incomplete:**

- **Dependency Detection**: Check for missing test dependencies:
  - JavaScript: `npm ls` or `yarn list` to verify test packages
  - Python: `pip list` to check for test packages  
  - Java: Check `pom.xml` or `build.gradle` for test dependencies
- **Installation Guidance**: Suggest missing dependencies but don't install automatically
- **Configuration Files**: Identify missing config files (`jest.config.js`, `pytest.ini`, etc.)

### Import Resolution Failures
**When imports fail in test files:**

- **Path Mapping**: Check configuration files for custom path mappings
- **Relative vs Absolute**: Try both relative and absolute import patterns
- **File Extensions**: Verify correct file extensions for imports
- **Module Resolution**: Check if files are properly exported from source modules

## Unit vs Integration Test Strategy

### Unit Test Characteristics
- **Single Responsibility**: Test one function, method, or component in isolation
- **Fast Execution**: Should run quickly (milliseconds) with minimal setup
- **Isolated Dependencies**: Mock or stub all external dependencies
- **Predictable**: Same inputs always produce same outputs
- **Focused Scope**: Test specific behaviors, edge cases, and error conditions

### Integration Test Characteristics  
- **Multi-Component**: Test interactions between multiple modules or services
- **Real Dependencies**: Use actual implementations for components being integrated
- **End-to-End Flows**: Test complete user journeys or business processes
- **Database Integration**: Test actual database operations, not just mocked ones
- **External Dependencies**: Test with real or realistic external service interactions

### Choosing Between Unit and Integration Tests

**Write Unit Tests When:**
- Testing pure functions or utility methods
- Testing component behavior in isolation
- Testing error handling and edge cases
- Testing business logic without external dependencies
- Need fast feedback during development

**Write Integration Tests When:**
- Testing database operations and queries
- Testing API endpoints and request/response flows
- Testing service-to-service communication
- Testing user workflows that span multiple components
- Testing configuration and environment setup

## Test Best Practices

### Test Scope and Boundaries

### Test Data Management
- **Isolated Test Data**: Each test should have its own data to avoid interdependencies
- **Cleanup Strategy**: Implement proper cleanup to prevent test pollution
- **Realistic Data**: Use data that closely resembles production scenarios
- **Edge Cases**: Include boundary conditions and error scenarios

### Test Data Setup Patterns
**Common patterns for managing test data:**

- **Factories and Builders**: Create reusable data builders:
  ```javascript
  const userFactory = (overrides = {}) => ({
    id: 1,
    name: 'Test User',
    email: 'test@example.com',
    ...overrides
  });
  ```
- **Fixtures**: Use static test data files:
  ```javascript
  // fixtures/user.json
  { "id": 1, "name": "Test User", "email": "test@example.com" }
  
  // In test
  const userData = require('./fixtures/user.json');
  ```
- **Database Seeds**: For database integration tests:
  ```javascript
  beforeEach(async () => {
    await db.seed.run(); // Reset to known state
  });
  ```
- **Mock Data Generation**: Use libraries like faker.js for dynamic data:
  ```javascript
  const userData = {
    name: faker.name.firstName(),
    email: faker.internet.email()
  };
  ```

### Mock Strategy for Integration Tests
- **Selective Mocking**: Mock only external dependencies that are unreliable or expensive
- **Real Dependencies**: Use real implementations for components being integrated
- **Test Doubles**: Use appropriate test doubles (stubs, fakes, mocks) based on the scenario
- **Contract Testing**: Ensure mocks accurately represent real service contracts

### Performance Considerations
- **Test Execution Time**: Keep integration tests reasonably fast while maintaining coverage
- **Resource Usage**: Monitor memory and CPU usage during test execution
- **Parallel Execution**: Design tests to run safely in parallel when possible
- **Test Isolation**: Ensure tests don't interfere with each other's execution

## Test File Skeleton Examples

### Unit Test Skeletons

#### Pure Function Unit Test Skeleton
```typescript
import { calculateTotal } from './utils';

describe('calculateTotal', () => {
  it('produces output', () => {
    // Given: Valid input
    const items = [{ price: 10, quantity: 2 }];
    
    // When: Calling function
    const result = calculateTotal(items);
    
    // Then: Function should return expected value
    expect(result).toBe(20);
  });
});
```

#### Class Method Unit Test Skeleton
```typescript
import { UserService } from './UserService';

describe('UserService', () => {
  it('produces output', () => {
    // Given: Service instance with mocked dependencies
    const mockDatabase = { findUser: jest.fn() };
    const service = new UserService(mockDatabase);
    
    // When: Calling method
    const result = service.validateUser('test@example.com');
    
    // Then: Method should return expected type
    expect(result).toBeDefined();
    expect(typeof result).toBe('boolean');
  });
});
```

### Integration Test Skeletons

#### React/TypeScript Component Integration Test Skeleton
```typescript
import { render } from '@testing-library/react';
import { MyComponent } from './MyComponent';

describe('MyComponent', () => {
  it('renders', () => {
    // Given: Component with basic props
    const props = { title: 'Test' };
    
    // When: Rendering component
    const { container } = render(<MyComponent {...props} />);
    
    // Then: Component should render without errors
    expect(container.firstChild).toBeInTheDocument();
  });
});
```

### TypeScript Module Test Skeleton
```typescript
import { myFunction } from './myModule';

describe('myModule', () => {
  it('produces output', () => {
    // Given: Valid input
    const input = 'test';
    
    // When: Calling function
    const result = myFunction(input);
    
    // Then: Function should return expected type
    expect(result).toBeDefined();
    expect(typeof result).toBe('string');
  });
});
```

### Java Class Test Skeleton
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MyClassTest {
    @Test
    void generatesExpectedOutput() {
        // Given: Valid input
        String input = "test";
        MyClass instance = new MyClass();
        
        // When: Calling method
        String result = instance.process(input);
        
        // Then: Method should return expected type
        assertNotNull(result);
        assertTrue(result instanceof String);
    }
}
```

## Common Test Patterns

### Unit Test Patterns

#### Testing Pure Functions
```typescript
// Testing business logic without side effects
describe('taxCalculator', () => {
  it('calculates tax correctly for standard rate', () => {
    // Given: Valid input
    const amount = 100;
    const rate = 0.1;
    
    // When: Calculating tax
    const result = calculateTax(amount, rate);
    
    // Then: Tax should be calculated correctly
    expect(result).toBe(10);
  });
  
  it('handles edge case of zero amount', () => {
    // Given: Zero amount
    const amount = 0;
    const rate = 0.1;
    
    // When: Calculating tax
    const result = calculateTax(amount, rate);
    
    // Then: Tax should be zero
    expect(result).toBe(0);
  });
});
```

#### Testing Classes with Mocked Dependencies
```typescript
describe('EmailService', () => {
  let emailService: EmailService;
  let mockTransport: jest.Mocked<EmailTransport>;
  
  beforeEach(() => {
    // Given: Mocked dependencies
    mockTransport = {
      send: jest.fn().mockResolvedValue(true)
    };
    emailService = new EmailService(mockTransport);
  });
  
  it('sends email successfully', async () => {
    // Given: Valid email data
    const email = { to: 'test@example.com', subject: 'Test', body: 'Hello' };
    
    // When: Sending email
    const result = await emailService.sendEmail(email);
    
    // Then: Email should be sent
    expect(result).toBe(true);
    expect(mockTransport.send).toHaveBeenCalledWith(email);
  });
});
```

### Integration Test Patterns

#### Database Integration Tests
```javascript
// Given: Clean database state with test data
beforeEach(async () => {
  await database.clear();
  await database.seed(testData);
});

// When: Testing user creation flow
test('should create user with profile', async () => {
  // Given: Valid user data
  const userData = { name: 'John', email: 'john@example.com' };
  
  // When: Creating user through service
  const result = await userService.createUser(userData);
  
  // Then: User and profile should be created
  expect(result.user.id).toBeDefined();
  expect(result.profile.userId).toBe(result.user.id);
});
```

### API Integration Tests
```javascript
// Given: Test server setup
beforeAll(async () => {
  server = await createTestServer();
  await server.start();
});

// When: Testing API endpoint integration
test('should process order end-to-end', async () => {
  // Given: Valid order data
  const orderData = { items: [{ id: 1, quantity: 2 }] };
  
  // When: Submitting order via API
  const response = await request(server)
    .post('/api/orders')
    .send(orderData);
  
  // Then: Order should be processed and persisted
  expect(response.status).toBe(201);
  expect(response.body.orderId).toBeDefined();
  
  const savedOrder = await orderRepository.findById(response.body.orderId);
  expect(savedOrder.status).toBe('pending');
});
```

### Service Integration Tests
```python
# Given: Service dependencies setup
@pytest.fixture
def payment_service():
    return PaymentService(
        payment_gateway=MockPaymentGateway(),
        order_service=RealOrderService(),
        notification_service=MockNotificationService()
    )

# When: Testing service integration
def test_payment_processing_flow(payment_service):
    # Given: Valid payment request
    payment_request = PaymentRequest(
        amount=100.00,
        order_id="order-123",
        customer_id="customer-456"
    )
    
    # When: Processing payment
    result = payment_service.process_payment(payment_request)
    
    # Then: Payment should be processed and order updated
    assert result.status == PaymentStatus.SUCCESS
    assert result.transaction_id is not None
    
    # Verify order was updated
    order = payment_service.order_service.get_order("order-123")
    assert order.payment_status == "paid"
```

## Error Handling and Edge Cases

### Test Failure Scenarios
- **Network Failures**: Test how the system handles network timeouts and connection errors
- **Data Corruption**: Verify system behavior with invalid or corrupted data
- **Resource Exhaustion**: Test behavior under resource constraints
- **Concurrent Access**: Test system behavior under concurrent load

### Boundary Testing
- **Input Validation**: Test with boundary values and invalid inputs
- **State Transitions**: Test all valid and invalid state transitions
- **Timing Issues**: Test race conditions and timing-sensitive operations
- **Security Boundaries**: Test authentication and authorization edge cases

## Test Execution Commands

### Command Discovery Process
**Systematic approach to finding the correct test command:**

1. **Check package.json scripts**: `grep -A 5 -B 5 "scripts" package.json`
2. **Look for Makefile**: `cat Makefile | grep -i test`
3. **Check README.md**: `grep -i "test\|testing\|run" README.md`
4. **Try common commands**: Based on detected framework and project type

### Framework-Specific Commands
- **JavaScript/TypeScript**: `npm test`, `yarn test`, `npm run test:unit`, `npm run test:integration`
- **Python**: `pytest`, `python -m pytest`, `python -m unittest`, `py.test`
- **Java**: `mvn test`, `gradle test`, `./gradlew test`
- **Go**: `go test`, `go test ./...`
- **Rust**: `cargo test`

### Command Validation
- **Dry Run**: Use `--dry-run` flags when available to validate without execution
- **Verbose Output**: Use `-v` or `--verbose` flags for detailed output when debugging
- **Specific Test**: Run single test file first to validate setup
- **Watch Mode**: Use `--watch` for iterative development when available

## Quality Checklist

Before considering integration tests complete, verify:

- [ ] Tests follow existing project patterns and conventions
- [ ] Each test has a clear, single responsibility
- [ ] Test data is properly isolated and cleaned up
- [ ] Mocks accurately represent real dependencies
- [ ] All critical integration points are covered
- [ ] Tests run reliably and consistently
- [ ] Performance impact is acceptable
- [ ] Error scenarios are adequately tested
- [ ] Documentation clearly explains test purpose
- [ ] No unnecessary duplication between tests

## Troubleshooting Common Issues

### Flaky Tests
- **Root Cause**: Often due to timing issues, shared state, or environmental dependencies
- **Solution**: Add proper waits, isolate test data, mock unstable dependencies

### Slow Test Execution
- **Root Cause**: Excessive database operations, network calls, or large data sets
- **Solution**: Optimize test data, use test databases, implement proper mocking

### Test Pollution
- **Root Cause**: Tests affecting each other through shared state or resources
- **Solution**: Implement proper setup/teardown, use transaction rollbacks, isolate data

### Mock Synchronization
- **Root Cause**: Mocks don't accurately represent real service behavior
- **Solution**: Use contract testing, regularly update mocks, prefer integration over unit tests for critical paths

This guide should be used as a reference for writing high-quality unit and integration tests that are maintainable, reliable, and provide meaningful coverage of both individual components and system integration points.

## Quick Reference: Test Type Decision Matrix

| Scenario | Test Type | Key Characteristics |
|----------|-----------|-------------------|
| Pure function with no dependencies | Unit | Fast, isolated, predictable |
| Class method with injected dependencies | Unit | Mock all dependencies |
| Component rendering with props | Unit | Mock context, focus on component logic |
| Database queries and transactions | Integration | Real database, test data isolation |
| API endpoint request/response | Integration | Real HTTP server, realistic data |
| Service-to-service communication | Integration | Real implementations, network calls |
| User workflow across multiple pages | Integration | End-to-end user journey |
| Configuration and environment setup | Integration | Real environment variables |

## Test Naming Conventions

### Unit Test Names
- Focus on behavior: `should return user when valid ID provided`
- Include conditions: `should throw error when email is invalid`
- State the expected outcome: `should calculate discount correctly for premium users`

### Integration Test Names
- Focus on workflow: `should create order and update inventory`
- Include system boundary: `should authenticate user via OAuth and create session`
- State business outcome: `should process payment and send confirmation email`