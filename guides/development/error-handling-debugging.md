# Error Handling and Debugging Guide

This guide provides systematic approaches for LLM tools to diagnose, troubleshoot, and resolve errors in codebases efficiently and methodically.

## Core Debugging Strategy

### Debugging Philosophy
- **Systematic Investigation**: Follow structured approaches rather than random attempts
- **Evidence-Based Analysis**: Collect data before forming hypotheses
- **Incremental Testing**: Test one change at a time to isolate causes
- **Documentation**: Record findings to avoid repeating failed attempts

### Debugging Phases
1. **Problem Definition** - Clearly define what's wrong and expected behavior
2. **Information Gathering** - Collect all relevant data and context
3. **Hypothesis Formation** - Develop testable theories about the cause
4. **Systematic Testing** - Test hypotheses methodically
5. **Solution Implementation** - Apply fix and verify resolution

## Phase 1: Problem Definition

### Error Classification
**Start by clearly categorizing the type of error encountered.**

#### Runtime Errors
```bash
# Identify error type
grep -r "Error\|Exception\|Failed" logs/ | head -10

# Check for stack traces
grep -A 20 -B 5 "at.*line\|Traceback" logs/ | head -30

# Look for error patterns
grep -E "(404|500|timeout|connection)" logs/ | head -10
```

#### Build/Compilation Errors
```bash
# Language-specific error patterns
grep -E "(SyntaxError|TypeError|ImportError)" . --include="*.py" -n
grep -E "(cannot find symbol|incompatible types)" . --include="*.java" -n
grep -E "(error TS|Cannot resolve)" . --include="*.ts" -n

# Dependency issues
npm ls --depth=0 | grep -E "(UNMET|missing|invalid)"
pip check 2>&1 | grep -v "No broken requirements"
```

#### Logic/Behavioral Errors
```bash
# Find test failures
find . -name "*.test.*" -exec grep -l "failed\|error" {} \;

# Check for debugging statements
grep -r "console.log\|print\|System.out" . --include="*.js" --include="*.py" --include="*.java"

# Look for TODO/FIXME markers
grep -r "TODO\|FIXME\|XXX\|HACK" . --include="*.js" --include="*.py" --include="*.java"
```

### Problem Documentation Template
```markdown
## Error Report

### What Should Happen
[Expected behavior description]

### What Actually Happens
[Actual behavior description]

### Error Details
- **Error Message**: [Exact error text]
- **Error Type**: [Runtime/Build/Logic]
- **Location**: [File:line or component]
- **Frequency**: [Always/Sometimes/Rare]

### Environment
- **Language/Framework**: [Version info]
- **Operating System**: [OS details]
- **Browser** (if applicable): [Browser version]
- **Dependencies**: [Relevant package versions]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

## Phase 2: Information Gathering

### Context Collection
**Gather comprehensive information before attempting fixes.**

#### System Context
```bash
# Check system resources
df -h    # Disk space
free -h  # Memory usage
ps aux | head -10  # Running processes

# Environment variables
env | grep -E "(NODE_ENV|PYTHON_PATH|JAVA_HOME|PATH)" | head -10

# Version information
node --version 2>/dev/null || echo "Node not found"
python --version 2>/dev/null || echo "Python not found"
java -version 2>/dev/null || echo "Java not found"
```

#### Application Context
```bash
# Recent changes
git log --oneline -10
git diff HEAD~1 --name-only

# Configuration files
find . -name "*.config.*" -o -name "*.env*" -o -name "settings.*" | head -10

# Log analysis
tail -50 logs/error.log 2>/dev/null || echo "No error log found"
tail -50 logs/application.log 2>/dev/null || echo "No app log found"
```

#### Dependency Context
```bash
# Check for conflicting versions
npm outdated 2>/dev/null || echo "No npm packages"
pip list --outdated 2>/dev/null || echo "No pip packages"

# Verify installations
which node python java npm pip
```

### Data Collection Strategies

#### For Runtime Errors
- **Stack Traces**: Full error stack with line numbers
- **Input Data**: What data caused the error
- **Timing**: When the error occurs (startup, specific action, etc.)
- **User Context**: What user was doing when error occurred

#### For Build Errors
- **Build Output**: Complete build log
- **Dependencies**: Package versions and conflicts
- **Configuration**: Build tool configuration
- **Environment**: Build environment details

#### For Logic Errors
- **Test Results**: Which tests pass/fail
- **Input/Output**: Expected vs actual results
- **Data Flow**: How data moves through the system
- **State**: Application state when error occurs

## Phase 3: Hypothesis Formation

### Systematic Analysis
**Form testable hypotheses based on collected evidence.**

#### Common Error Patterns

##### Dependency Issues
```bash
# Hypothesis: Version conflict
npm ls | grep -E "(UNMET|deduped)"
pip show package_name | grep Version

# Test: Clean install
rm -rf node_modules package-lock.json
npm install
```

##### Configuration Problems
```bash
# Hypothesis: Environment mismatch
diff .env.example .env | head -10
grep -r "process.env\|os.environ" . --include="*.js" --include="*.py" | head -5

# Test: Reset configuration
cp .env.example .env.test
# Test with known good configuration
```

##### Path/Import Issues
```bash
# Hypothesis: Import path problems
find . -name "*.js" -o -name "*.ts" | xargs grep -l "import.*\.\." | head -5
grep -r "ModuleNotFoundError\|Cannot resolve" . | head -5

# Test: Verify paths exist
ls -la path/to/suspected/file
```

### Hypothesis Testing Framework

#### Test Design Principles
- **Minimal Changes**: Test one variable at a time
- **Reversible**: Easy to undo test changes
- **Measurable**: Clear success/failure criteria
- **Documented**: Record what was tested and results

#### Testing Template
```markdown
## Hypothesis Test

### Hypothesis
[What you think is causing the problem]

### Test Method
[How you'll test this hypothesis]

### Expected Result
[What should happen if hypothesis is correct]

### Actual Result
[What actually happened]

### Conclusion
[Confirmed/Rejected and next steps]
```

## Phase 4: Systematic Testing

### Testing Strategies

#### Binary Search Debugging
```bash
# For recent regressions
git bisect start
git bisect bad HEAD
git bisect good known_good_commit

# Test each commit automatically
git bisect run npm test
```

#### Component Isolation
```bash
# Test individual components
npm test component.test.js
python -m pytest tests/test_component.py -v
mvn test -Dtest=ComponentTest

# Mock external dependencies
# Create minimal reproduction case
```

#### Environment Testing
```bash
# Test in clean environment
docker run -it node:alpine sh
# Recreate minimal setup

# Test with different versions
nvm use 16.0.0  # For Node.js
pyenv local 3.9.0  # For Python
```

### Common Testing Patterns

#### For Network Issues
```bash
# Test connectivity
curl -I https://api.example.com
ping api.example.com

# Test with different endpoints
curl -X GET https://api.example.com/health
```

#### For Database Issues
```bash
# Test connection
psql -h localhost -U user -d database -c "SELECT 1;"
mysql -h localhost -u user -p -e "SELECT 1;"

# Test queries
# Run suspected query directly in database client
```

#### For Performance Issues
```bash
# Profile execution
time node script.js
python -m cProfile script.py
java -XX:+PrintGCDetails MyClass

# Memory analysis
valgrind --tool=memcheck ./program
node --inspect script.js
```

## Phase 5: Solution Implementation

### Fix Implementation Strategy

#### Minimal Viable Fix
```bash
# Apply smallest possible change
git checkout -b fix/specific-issue
# Make minimal change
git add -p  # Stage only relevant changes
git commit -m "Fix: specific issue description"
```

#### Testing Verification
```bash
# Run all relevant tests
npm test 2>&1 | tee test_results.log
python -m pytest tests/ -v
mvn test

# Test in multiple environments
npm run test:dev
npm run test:prod
```

#### Regression Prevention
```bash
# Add test for the bug
touch tests/test_bug_fix.js
# Write test that would have caught this bug

# Check for similar issues
grep -r "similar_pattern" . --include="*.js" --include="*.py"
```

### Solution Documentation

#### Fix Documentation Template
```markdown
## Bug Fix Summary

### Problem
[Brief description of the issue]

### Root Cause
[What actually caused the problem]

### Solution
[What was changed to fix it]

### Testing
- [Test 1: Description and result]
- [Test 2: Description and result]

### Prevention
[How to prevent this type of issue in the future]

### Related Issues
[Links to similar problems or potential related issues]
```

## Error Prevention Strategies

### Proactive Error Handling

#### Input Validation
```javascript
// Validate inputs early
function processData(data) {
  if (!data || typeof data !== 'object') {
    throw new Error('Invalid data: expected object');
  }
  // Process data
}
```

#### Graceful Degradation
```javascript
// Handle failures gracefully
try {
  const result = await riskyCOperation();
  return result;
} catch (error) {
  console.error('Operation failed:', error.message);
  return defaultValue;
}
```

#### Monitoring and Logging
```javascript
// Add comprehensive logging
console.log('Starting operation with params:', params);
try {
  const result = await operation(params);
  console.log('Operation completed successfully:', result.id);
  return result;
} catch (error) {
  console.error('Operation failed:', {
    error: error.message,
    params,
    timestamp: new Date().toISOString()
  });
  throw error;
}
```

### Code Quality Practices

#### Error Handling Patterns
- **Fail Fast**: Detect errors early in the process
- **Explicit Error States**: Don't hide or ignore errors
- **Context Preservation**: Include relevant context in error messages
- **Recovery Strategies**: Plan for error recovery when possible

#### Debugging Aids
- **Meaningful Variable Names**: Make debugging easier
- **Small Functions**: Easier to isolate problems
- **Clear Data Flow**: Obvious how data moves through system
- **Comprehensive Tests**: Catch issues before production

## Integration with Other Guides

### With Codebase Exploration
- Use exploration techniques to understand error context
- Follow systematic exploration when debugging unfamiliar code
- Document findings using exploration templates

### With Testing Guide
- Write tests to reproduce bugs before fixing
- Use test-driven debugging approach
- Follow testing patterns for error scenarios

### With Planning Guide
- Create debugging plans for complex issues
- Document systematic approaches for recurring problems
- Plan prevention strategies for common error types

## Common Debugging Pitfalls

### Cognitive Biases
- **Confirmation Bias**: Testing only theories that confirm expectations
- **Anchoring**: Focusing too much on first hypothesis
- **Availability Bias**: Assuming familiar problems without proper investigation

### Technical Mistakes
- **Changing Multiple Variables**: Testing too many things at once
- **Inadequate Testing**: Not thoroughly testing solutions
- **Environment Differences**: Assuming local environment matches production

### Process Issues
- **Insufficient Documentation**: Not recording what was tried
- **Impatience**: Moving to solutions before understanding problem
- **Scope Creep**: Trying to fix multiple issues simultaneously

## Troubleshooting Common Issues

### "It Works on My Machine"
1. **Environment Comparison**: Document differences between environments
2. **Dependency Audit**: Check for version mismatches
3. **Configuration Review**: Compare all configuration files
4. **Data Differences**: Verify test data matches production patterns

### Intermittent Issues
1. **Logging Enhancement**: Add more detailed logging
2. **Timing Analysis**: Look for race conditions
3. **Resource Monitoring**: Check for resource exhaustion
4. **Pattern Recognition**: Look for patterns in failure timing

### Performance Degradation
1. **Baseline Establishment**: Measure current performance
2. **Component Profiling**: Identify bottlenecks
3. **Resource Analysis**: Check CPU, memory, I/O usage
4. **Gradual Optimization**: Optimize one component at a time

This systematic approach to error handling and debugging ensures thorough problem resolution while building knowledge for future issue prevention.