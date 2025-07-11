# LLM Guide Router

**Instructions for LLM Tools**: This file helps you find the right guidance for any development task. Read this file first, then follow the links to the appropriate guides.

## Quick Task Routing

### 🚀 Starting a New Feature/Task
**Read First**: [`guides/workflows/feature-development-workflow.md`](guides/workflows/feature-development-workflow.md)
- Complete end-to-end process from requirements to implementation
- Includes exploration, planning, review, and iterative development
- **When to use**: Any time you're building something new

### 🔍 Understanding an Unfamiliar Codebase
**Read First**: [`guides/development/codebase-exploration.md`](guides/development/codebase-exploration.md)
- Systematic approach to exploring and understanding codebases
- Framework detection, pattern analysis, and architecture understanding
- **When to use**: Before making changes to unfamiliar code

### 📋 Creating Implementation Plans
**Read First**: [`guides/planning/planning-documentation.md`](guides/planning/planning-documentation.md)
- Comprehensive planning templates and review processes
- Requirements analysis and technical research methodologies
- **When to use**: Before implementing any significant changes

### 🧪 Writing Tests (Unit & Integration)
**Read First**: [`guides/testing/test-writing-guide.md`](guides/testing/test-writing-guide.md)
- Complete testing guidance for unit and integration tests
- Test-driven development and iterative testing approaches
- **When to use**: Whenever you need to write or improve tests

### 🐛 Debugging and Error Handling
**Read First**: [`guides/development/error-handling-debugging.md`](guides/development/error-handling-debugging.md)
- Systematic approach to diagnosing and resolving errors
- Methodical troubleshooting and problem-solving techniques
- **When to use**: When encountering bugs, errors, or unexpected behavior

### ✨ Code Review and Refactoring
**Read First**: [`guides/development/code-review-refactoring.md`](guides/development/code-review-refactoring.md)
- Systematic approach to improving existing code quality
- Safe refactoring techniques and code review best practices
- **When to use**: When improving existing code or conducting code reviews

## Task-Specific Routing

### Development Tasks

| Task Type | Primary Guide | Supporting Guides |
|-----------|---------------|-------------------|
| New Feature Development | [Feature Development Workflow](guides/workflows/feature-development-workflow.md) | [Codebase Exploration](guides/development/codebase-exploration.md), [Planning](guides/planning/planning-documentation.md), [Testing](guides/testing/test-writing-guide.md) |
| Bug Fix | [Error Handling & Debugging](guides/development/error-handling-debugging.md) | [Codebase Exploration](guides/development/codebase-exploration.md), [Testing](guides/testing/test-writing-guide.md) |
| Code Refactoring | [Code Review & Refactoring](guides/development/code-review-refactoring.md) | [Codebase Exploration](guides/development/codebase-exploration.md), [Planning](guides/planning/planning-documentation.md), [Testing](guides/testing/test-writing-guide.md) |
| Code Review | [Code Review & Refactoring](guides/development/code-review-refactoring.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |
| Performance Issues | [Error Handling & Debugging](guides/development/error-handling-debugging.md) | [Code Review & Refactoring](guides/development/code-review-refactoring.md), [Codebase Exploration](guides/development/codebase-exploration.md) |
| Adding Tests | [Testing](guides/testing/test-writing-guide.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |
| API Development | [Feature Development Workflow](guides/workflows/feature-development-workflow.md) | [Planning](guides/planning/planning-documentation.md), [Testing](guides/testing/test-writing-guide.md) |
| Component Creation | [Feature Development Workflow](guides/workflows/feature-development-workflow.md) | [Codebase Exploration](guides/development/codebase-exploration.md), [Testing](guides/testing/test-writing-guide.md) |

### Planning Tasks

| Task Type | Primary Guide | Supporting Guides |
|-----------|---------------|-------------------|
| Technical Planning | [Planning & Documentation](guides/planning/planning-documentation.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |
| Architecture Design | [Planning & Documentation](guides/planning/planning-documentation.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |
| Feature Scoping | [Planning & Documentation](guides/planning/planning-documentation.md) | [Feature Development Workflow](guides/workflows/feature-development-workflow.md) |
| Risk Assessment | [Planning & Documentation](guides/planning/planning-documentation.md) | - |

### Testing Tasks

| Task Type | Primary Guide | Supporting Guides |
|-----------|---------------|-------------------|
| Unit Testing | [Testing Guide](guides/testing/test-writing-guide.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |
| Integration Testing | [Testing Guide](guides/testing/test-writing-guide.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |
| Test Strategy | [Testing Guide](guides/testing/test-writing-guide.md) | [Planning](guides/planning/planning-documentation.md) |
| Test Debugging | [Testing Guide](guides/testing/test-writing-guide.md) | [Codebase Exploration](guides/development/codebase-exploration.md) |

## Usage Instructions for LLMs

### 1. Identify Your Task
Determine what type of task you're being asked to perform:
- **New Development**: Building something new
- **Maintenance**: Fixing, refactoring, or improving existing code  
- **Analysis**: Understanding or documenting existing code
- **Testing**: Writing or improving tests
- **Planning**: Creating plans or documentation

### 2. Find Your Starting Point
Use the routing tables above to identify:
- **Primary Guide**: The main guide to follow
- **Supporting Guides**: Additional guides that may be helpful

### 3. Follow the Workflow
Most tasks should follow this general pattern:
1. **Explore** (if working with unfamiliar code)
2. **Plan** (for any significant changes)
3. **Get Review** (for any implementation plans)
4. **Implement Iteratively** (with testing)

### 4. Use Templates
Check the [`templates/`](templates/) directory for:
- Feature plan templates (`feature-plan-template.md`)
- Bug fix plan templates (`bug-fix-plan-template.md`)
- Refactoring plan templates (`refactoring-plan-template.md`)
- Exploration notes templates (`exploration-notes-template.md`)

### 5. Reference Examples
Check the [`examples/`](examples/) directory for:
- Complete workflow examples
- Sample plans and documentation
- Test examples
- Common patterns

## Guide Dependencies

```
Feature Development Workflow
├── Codebase Exploration (Phase 1)
├── Planning & Documentation (Phase 3)
└── Testing Guide (Phase 5)

Codebase Exploration
├── No dependencies
└── Feeds into all other guides

Planning & Documentation  
├── Codebase Exploration (for context)
└── Used by Feature Development Workflow

Testing Guide
├── Codebase Exploration (for patterns)
└── Used by Feature Development Workflow

Error Handling & Debugging
├── Codebase Exploration (for context)
└── Used for troubleshooting in all workflows

Code Review & Refactoring
├── Codebase Exploration (for understanding)
├── Planning & Documentation (for complex refactoring)
└── Testing Guide (for safe refactoring)
```

## Quick Reference Commands

### For Exploration Tasks
```bash
# Read the exploration guide
cat guides/development/codebase-exploration.md

# Start with project structure
ls -la && find . -name "*.json" -o -name "*.yml" | head -10
```

### For Planning Tasks
```bash
# Read the planning guide
cat guides/planning/planning-documentation.md

# Use planning templates
cp templates/feature-plan-template.md plan-[your-feature].md
cp templates/bug-fix-plan-template.md plan-[bug-name].md
cp templates/refactoring-plan-template.md plan-[refactoring-scope].md
```

### For Testing Tasks
```bash
# Read the testing guide
cat guides/testing/test-writing-guide.md

# Find existing test patterns
find . -name "*.test.*" -o -name "*.spec.*" | head -5
```

### For Debugging Tasks
```bash
# Read the debugging guide
cat guides/development/error-handling-debugging.md

# Use bug fix template
cp templates/bug-fix-plan-template.md plan-fix-[issue-name].md
```

### For Code Review/Refactoring Tasks
```bash
# Read the code review guide
cat guides/development/code-review-refactoring.md

# Use refactoring template
cp templates/refactoring-plan-template.md plan-refactor-[component].md
```

### For Development Tasks
```bash
# Read the workflow guide
cat guides/workflows/feature-development-workflow.md

# Follow the complete workflow
```

## Emergency Quick Start

If you're unsure which guide to use:

1. **Read this file completely** to understand the routing system
2. **For any new development**: Start with [Feature Development Workflow](guides/workflows/feature-development-workflow.md)
3. **For unfamiliar code**: Start with [Codebase Exploration](guides/development/codebase-exploration.md)
4. **For planning**: Start with [Planning & Documentation](guides/planning/planning-documentation.md)
5. **For testing**: Start with [Testing Guide](guides/testing/test-writing-guide.md)
6. **For bugs/errors**: Start with [Error Handling & Debugging](guides/development/error-handling-debugging.md)
7. **For code improvement**: Start with [Code Review & Refactoring](guides/development/code-review-refactoring.md)

Remember: **Always explore before planning, always plan before implementing, always test during implementation.**