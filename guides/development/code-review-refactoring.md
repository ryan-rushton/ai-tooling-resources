# Code Review and Refactoring Guide

This guide provides systematic approaches for LLM tools to review existing code quality, identify improvement opportunities, and safely refactor code while maintaining functionality.

## Core Review and Refactoring Strategy

### Philosophy
- **Functionality First**: Never break working code without clear benefit
- **Incremental Improvement**: Make small, safe changes rather than large rewrites
- **Test-Driven Refactoring**: Ensure tests exist before making changes
- **Evidence-Based Decisions**: Use metrics and concrete examples to justify changes

### Process Phases
1. **Code Assessment** - Analyze current code quality and identify issues
2. **Opportunity Identification** - Find specific improvement opportunities
3. **Refactoring Planning** - Create safe, incremental improvement plan
4. **Safe Implementation** - Execute changes with continuous validation
5. **Quality Verification** - Confirm improvements without regression

## Phase 1: Code Assessment

### Systematic Code Analysis
**Start with comprehensive assessment of code quality and structure.**

#### Code Quality Metrics
```bash
# Lines of code analysis
find . -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.java" | xargs wc -l | sort -n

# Complexity analysis (if tools available)
npx complexity-report src/ 2>/dev/null || echo "No complexity tools found"
radon cc . --min B 2>/dev/null || echo "No Python complexity tools found"

# Duplication detection
grep -r "function\|def\|class" . --include="*.js" --include="*.py" | cut -d: -f2 | sort | uniq -d | head -10
```

#### Code Structure Assessment
```bash
# File organization analysis
find . -name "*.js" -o -name "*.py" | head -20 | while read file; do
  echo "=== $file ==="
  head -10 "$file"
  echo
done

# Dependency analysis
grep -r "import\|require\|from.*import" . --include="*.js" --include="*.py" | head -20

# Function/class size analysis
grep -n "^def\|^function\|^class" . --include="*.js" --include="*.py" | head -20
```

### Code Quality Checklist

#### Readability Assessment
- [ ] **Naming**: Variables, functions, and classes have clear, descriptive names
- [ ] **Comments**: Complex logic is documented appropriately
- [ ] **Structure**: Code is well-organized and follows consistent patterns
- [ ] **Length**: Functions and classes are reasonably sized
- [ ] **Complexity**: Logic flow is easy to follow

#### Maintainability Assessment
- [ ] **DRY Principle**: No significant code duplication
- [ ] **Single Responsibility**: Each function/class has one clear purpose
- [ ] **Loose Coupling**: Components don't depend heavily on each other
- [ ] **High Cohesion**: Related functionality is grouped together
- [ ] **Error Handling**: Proper error handling throughout

#### Performance Assessment
- [ ] **Algorithmic Efficiency**: No obvious performance bottlenecks
- [ ] **Resource Usage**: Memory and CPU usage are reasonable
- [ ] **Network Calls**: API calls are optimized and cached appropriately
- [ ] **Database Queries**: Queries are efficient and not over-fetching

### Assessment Documentation Template
```markdown
## Code Quality Assessment

### Overview
- **Files Analyzed**: [Number and types]
- **Total Lines**: [Line count]
- **Languages**: [Primary languages used]
- **Frameworks**: [Key frameworks/libraries]

### Quality Ratings (1-5, 5 being best)
- **Readability**: [Score] - [Brief justification]
- **Maintainability**: [Score] - [Brief justification]
- **Performance**: [Score] - [Brief justification]
- **Test Coverage**: [Score] - [Brief justification]

### Key Strengths
- [Strength 1]: [Location and description]
- [Strength 2]: [Location and description]

### Major Issues
- [Issue 1]: [Location, impact, and priority]
- [Issue 2]: [Location, impact, and priority]

### Improvement Opportunities
- [Opportunity 1]: [Description and potential benefit]
- [Opportunity 2]: [Description and potential benefit]
```

## Phase 2: Opportunity Identification

### Code Smell Detection
**Systematically identify specific areas needing improvement.**

#### Common Code Smells

##### Structural Issues
```bash
# Long functions/methods
grep -n "^def\|^function" . --include="*.js" --include="*.py" | while read line; do
  file=$(echo $line | cut -d: -f1)
  line_num=$(echo $line | cut -d: -f2)
  # Count lines until next function (simplified)
  echo "Function at $file:$line_num"
done

# Large classes
grep -n "^class" . --include="*.js" --include="*.py" | head -10

# Deep nesting
grep -E "    if|        if|            if" . --include="*.js" --include="*.py" | head -10
```

##### Logic Issues
```bash
# Duplicated code blocks
grep -A 5 -B 5 "console.log\|print" . --include="*.js" --include="*.py" | grep -E ":\s*(console\.log|print)" | head -10

# Magic numbers
grep -E "[^a-zA-Z_][0-9]{2,}[^a-zA-Z_]" . --include="*.js" --include="*.py" | head -10

# Long parameter lists
grep -E "(def|function).*,.{50,}" . --include="*.js" --include="*.py" | head -5
```

##### Naming Issues
```bash
# Single letter variables (outside of loops)
grep -E "\b[a-z]\s*=" . --include="*.js" --include="*.py" | grep -v "for.*in\|for.*range" | head -10

# Non-descriptive names
grep -E "(data|info|temp|var)[0-9]*\s*=" . --include="*.js" --include="*.py" | head -10

# Inconsistent naming
grep -E "(camelCase|snake_case)" . --include="*.js" --include="*.py" | head -10
```

### Refactoring Opportunity Classification

#### High-Impact, Low-Risk Opportunities
- **Extract Constants**: Replace magic numbers with named constants
- **Rename Variables**: Improve variable names for clarity
- **Add Comments**: Document complex logic
- **Extract Simple Functions**: Break down long functions

#### Medium-Impact, Medium-Risk Opportunities
- **Extract Classes**: Group related functionality
- **Reorganize File Structure**: Improve module organization
- **Simplify Conditionals**: Reduce nested if statements
- **Remove Dead Code**: Delete unused functions/variables

#### High-Impact, High-Risk Opportunities
- **Algorithm Changes**: Improve algorithmic efficiency
- **Architecture Refactoring**: Change fundamental structure
- **Framework Updates**: Upgrade to newer versions
- **Database Schema Changes**: Modify data structures

### Prioritization Matrix

```markdown
## Refactoring Opportunities Priority Matrix

### Immediate (High Impact, Low Risk)
1. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]
2. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]

### Soon (Medium Impact, Low-Medium Risk)
1. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]
2. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]

### Later (High Impact, High Risk)
1. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]
2. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]

### Consider (Low Impact)
1. [Opportunity]: [File:line] - [Benefit] - [Effort: hours]
```

## Phase 3: Refactoring Planning

### Safe Refactoring Strategy
**Plan changes to minimize risk while maximizing benefit.**

#### Pre-Refactoring Checklist
- [ ] **Tests Exist**: Adequate test coverage for code being changed
- [ ] **Tests Pass**: All existing tests are currently passing
- [ ] **Version Control**: Clean working directory, ready to commit
- [ ] **Backup Plan**: Clear rollback strategy if changes fail
- [ ] **Scope Defined**: Specific, limited scope for this refactoring session

#### Refactoring Plan Template
```markdown
## Refactoring Plan: [Feature/Component Name]

### Objective
[What you're trying to improve and why]

### Current State
- **Files Affected**: [List of files]
- **Key Functions**: [Functions being modified]
- **Dependencies**: [What depends on this code]
- **Test Coverage**: [Current test status]

### Proposed Changes
#### Step 1: [Preparation]
- **Actions**: [Specific actions to take]
- **Verification**: [How to verify this step worked]
- **Rollback**: [How to undo if needed]

#### Step 2: [Implementation]
- **Actions**: [Specific actions to take]
- **Verification**: [How to verify this step worked]
- **Rollback**: [How to undo if needed]

#### Step 3: [Cleanup]
- **Actions**: [Specific actions to take]
- **Verification**: [How to verify this step worked]
- **Rollback**: [How to undo if needed]

### Success Criteria
- [ ] All tests pass
- [ ] No performance regression
- [ ] Code is more readable/maintainable
- [ ] No breaking changes to public API

### Risk Assessment
- **High Risk**: [Potential issues and mitigation]
- **Medium Risk**: [Potential issues and mitigation]
- **Low Risk**: [Minor potential issues]
```

### Incremental Refactoring Patterns

#### The Strangler Fig Pattern
```javascript
// Phase 1: Add new implementation alongside old
function oldCalculation(data) {
  // Existing implementation
}

function newCalculation(data) {
  // Improved implementation
}

function calculation(data) {
  // Use feature flag to gradually switch
  return useNewImplementation ? newCalculation(data) : oldCalculation(data);
}

// Phase 2: Gradually migrate
// Phase 3: Remove old implementation
```

#### Extract Function Safely
```javascript
// Before: Large function
function processOrder(order) {
  // 50 lines of mixed logic
  // validation, calculation, persistence, notification
}

// Step 1: Extract validation (test still passes)
function validateOrder(order) {
  // validation logic
}

function processOrder(order) {
  validateOrder(order);
  // remaining 40 lines
}

// Step 2: Extract calculation (test still passes)
// Step 3: Continue incrementally
```

## Phase 4: Safe Implementation

### Implementation Strategy
**Execute refactoring with continuous validation and safety checks.**

#### Red-Green-Refactor Cycle
```bash
# 1. RED: Ensure tests are comprehensive and failing scenarios exist
npm test 2>&1 | grep -E "(pass|fail)"

# 2. GREEN: Make minimal change to pass tests
git add -p  # Stage only refactoring changes
git commit -m "Refactor: [specific change]"

# 3. REFACTOR: Improve implementation while keeping tests green
npm test  # Verify tests still pass
```

#### Safety Procedures

##### Continuous Testing
```bash
# Run tests after each small change
npm test
# Or run specific test file
npm test -- tests/specific-component.test.js

# For other languages
python -m pytest tests/test_specific.py -v
mvn test -Dtest=SpecificTest
```

##### Incremental Commits
```bash
# Make tiny, reversible commits
git add specific_file.js
git commit -m "Extract validateInput function"

git add specific_file.js
git commit -m "Move calculateTotal to utils"

# Easy to revert if something breaks
git revert HEAD  # Undo last commit
```

##### Branch Protection
```bash
# Work on feature branch
git checkout -b refactor/improve-user-service
# Make changes
git push origin refactor/improve-user-service
# Review before merging to main
```

### Implementation Patterns

#### Extract Method
```javascript
// Before
function processUser(userData) {
  // Validate email
  if (!userData.email || !userData.email.includes('@')) {
    throw new Error('Invalid email');
  }
  
  // Calculate age
  const birthYear = new Date(userData.birthDate).getFullYear();
  const age = new Date().getFullYear() - birthYear;
  
  // Save to database
  return database.save({
    ...userData,
    age,
    createdAt: new Date()
  });
}

// After: Extract methods one at a time
function validateEmail(email) {
  if (!email || !email.includes('@')) {
    throw new Error('Invalid email');
  }
}

function calculateAge(birthDate) {
  const birthYear = new Date(birthDate).getFullYear();
  return new Date().getFullYear() - birthYear;
}

function processUser(userData) {
  validateEmail(userData.email);
  const age = calculateAge(userData.birthDate);
  
  return database.save({
    ...userData,
    age,
    createdAt: new Date()
  });
}
```

#### Replace Magic Numbers
```javascript
// Before
function calculateShipping(weight) {
  if (weight < 5) return 10;
  if (weight < 20) return 15;
  return 25;
}

// After
const SHIPPING_THRESHOLDS = {
  LIGHT_WEIGHT: 5,
  MEDIUM_WEIGHT: 20
};

const SHIPPING_COSTS = {
  LIGHT: 10,
  MEDIUM: 15,
  HEAVY: 25
};

function calculateShipping(weight) {
  if (weight < SHIPPING_THRESHOLDS.LIGHT_WEIGHT) return SHIPPING_COSTS.LIGHT;
  if (weight < SHIPPING_THRESHOLDS.MEDIUM_WEIGHT) return SHIPPING_COSTS.MEDIUM;
  return SHIPPING_COSTS.HEAVY;
}
```

#### Simplify Conditionals
```javascript
// Before
function getDiscount(user) {
  if (user.isPremium) {
    if (user.yearsActive > 5) {
      if (user.totalSpent > 1000) {
        return 0.25;
      } else {
        return 0.15;
      }
    } else {
      return 0.10;
    }
  } else {
    return 0;
  }
}

// After
function getDiscount(user) {
  if (!user.isPremium) return 0;
  if (user.yearsActive <= 5) return 0.10;
  if (user.totalSpent > 1000) return 0.25;
  return 0.15;
}
```

## Phase 5: Quality Verification

### Post-Refactoring Validation
**Ensure improvements achieved without introducing regressions.**

#### Functional Verification
```bash
# Run full test suite
npm test 2>&1 | tee refactor_test_results.log
python -m pytest tests/ -v --tb=short
mvn test

# Performance testing (if applicable)
npm run benchmark 2>/dev/null || echo "No benchmark script"
time npm start & sleep 5 && kill %1  # Quick startup time test
```

#### Quality Metrics Comparison
```bash
# Before/after comparison
echo "Before refactoring:" > quality_comparison.md
wc -l original_file.js >> quality_comparison.md

echo "After refactoring:" >> quality_comparison.md
wc -l refactored_file.js >> quality_comparison.md

# Complexity comparison (if tools available)
npx complexity-report src/ 2>/dev/null >> quality_comparison.md
```

#### Integration Testing
```bash
# Test with real data/scenarios
npm run test:integration 2>/dev/null || echo "No integration tests"

# Manual testing of key paths
echo "Manual test: user registration flow"
echo "Manual test: data processing pipeline"
echo "Manual test: API endpoint responses"
```

### Success Verification Checklist
- [ ] **All Tests Pass**: No regressions in functionality
- [ ] **Performance Maintained**: No significant performance degradation
- [ ] **Readability Improved**: Code is easier to understand
- [ ] **Maintainability Enhanced**: Future changes will be easier
- [ ] **Documentation Updated**: Comments and docs reflect changes
- [ ] **No Breaking Changes**: Public APIs remain compatible

### Documentation of Improvements
```markdown
## Refactoring Results

### Summary
[Brief description of what was accomplished]

### Metrics Improvement
- **Lines of Code**: [Before] → [After] ([% change])
- **Function Complexity**: [Before] → [After]
- **Test Coverage**: [Before] → [After]
- **Performance**: [Before] → [After]

### Specific Improvements
1. **[Improvement 1]**: [Description and location]
2. **[Improvement 2]**: [Description and location]
3. **[Improvement 3]**: [Description and location]

### Future Opportunities
- [Opportunity 1]: [Description and priority]
- [Opportunity 2]: [Description and priority]

### Lessons Learned
- [Lesson 1]: [What was learned and how to apply it]
- [Lesson 2]: [What was learned and how to apply it]
```

## Code Review Best Practices

### Review Checklist

#### Functionality Review
- [ ] **Correctness**: Code does what it's supposed to do
- [ ] **Edge Cases**: Handles boundary conditions appropriately
- [ ] **Error Handling**: Proper error handling and recovery
- [ ] **Security**: No security vulnerabilities introduced
- [ ] **Performance**: No obvious performance issues

#### Code Quality Review
- [ ] **Readability**: Code is clear and self-documenting
- [ ] **Consistency**: Follows established patterns and conventions
- [ ] **Simplicity**: Implementation is as simple as possible
- [ ] **Testability**: Code is structured to be easily testable
- [ ] **Maintainability**: Future modifications will be straightforward

#### Review Process
1. **Understand Context**: What problem is being solved?
2. **Check Requirements**: Does code meet all requirements?
3. **Assess Design**: Is the approach sound?
4. **Review Implementation**: Is code well-written?
5. **Test Adequacy**: Are tests comprehensive?
6. **Consider Alternatives**: Are there better approaches?

### Constructive Feedback Patterns

#### Positive Feedback
```markdown
✅ **Good**: Clear variable naming in `calculateUserScore()` makes the logic easy to follow.
✅ **Nice**: The error handling in line 45 covers the edge case we discussed.
```

#### Improvement Suggestions
```markdown
💡 **Suggestion**: Consider extracting the validation logic into a separate function for reusability.
💡 **Alternative**: Using a Map instead of multiple if statements might be cleaner here.
```

#### Required Changes
```markdown
❗ **Required**: This function is missing error handling for null inputs.
❗ **Security**: This SQL query is vulnerable to injection attacks.
```

## Integration with Other Guides

### With Codebase Exploration
- Use exploration techniques to understand code before refactoring
- Follow systematic analysis patterns from exploration guide
- Document findings using exploration templates

### With Testing Guide
- Ensure comprehensive test coverage before refactoring
- Write additional tests for complex refactoring scenarios
- Use test-driven refactoring approach

### With Planning Guide
- Create detailed refactoring plans for complex changes
- Use risk assessment templates from planning guide
- Get human review for major refactoring plans

### With Error Handling Guide
- Apply systematic debugging when refactoring introduces issues
- Use error handling patterns to improve code robustness
- Document and resolve any issues that arise

## Common Refactoring Pitfalls

### Planning Mistakes
- **Scope Creep**: Trying to refactor too much at once
- **Insufficient Testing**: Not having adequate test coverage before starting
- **No Clear Goal**: Refactoring without specific improvement objectives

### Implementation Mistakes
- **Breaking Changes**: Modifying public APIs without considering impact
- **Performance Regression**: Making code cleaner but significantly slower
- **Over-Engineering**: Making code more complex in the name of "better design"

### Process Mistakes
- **Inadequate Review**: Not getting proper review of refactoring plans
- **Poor Documentation**: Not documenting what changed and why
- **Rushing**: Moving too quickly without proper validation

This systematic approach to code review and refactoring ensures continuous improvement of code quality while maintaining system reliability and functionality.