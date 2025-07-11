# AI Tooling Resources - Master Index

**For LLM Tools**: This is your comprehensive guide to navigating this repository. Start here to find the right guidance for any development task.

## 🚀 Quick Start

1. **New to this repo?** → Read [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) for task-specific routing
2. **Starting development?** → Use [`guides/workflows/feature-development-workflow.md`](guides/workflows/feature-development-workflow.md)
3. **Need to understand code?** → Use [`guides/development/codebase-exploration.md`](guides/development/codebase-exploration.md)
4. **Writing tests?** → Use [`guides/testing/test-writing-guide.md`](guides/testing/test-writing-guide.md)

## 📁 Repository Structure

```
ai-tooling-resources/
├── GUIDE_ROUTER.md              # Main routing system - START HERE
├── INDEX.md                     # This file - master index
├── README.md                    # Repository overview and setup
├── guides/                      # Core guidance documents
│   ├── workflows/               # End-to-end process guides
│   │   └── feature-development-workflow.md
│   ├── development/             # Development-specific guides
│   │   └── codebase-exploration.md
│   ├── planning/                # Planning and documentation guides
│   │   └── planning-documentation.md
│   └── testing/                 # Testing guides and strategies
│       └── test-writing-guide.md
├── templates/                   # Reusable templates
│   ├── feature-plan-template.md
│   └── exploration-notes-template.md
└── examples/                    # Complete workflow examples
    └── complete-workflow-example.md
```

## 🎯 Task-Based Navigation

### I need to build something new
1. **Start**: [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) → "Starting a New Feature/Task"
2. **Follow**: [`guides/workflows/feature-development-workflow.md`](guides/workflows/feature-development-workflow.md)
3. **Use**: [`templates/feature-plan-template.md`](templates/feature-plan-template.md)
4. **Reference**: [`examples/complete-workflow-example.md`](examples/complete-workflow-example.md)

### I need to understand existing code
1. **Start**: [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) → "Understanding an Unfamiliar Codebase"
2. **Follow**: [`guides/development/codebase-exploration.md`](guides/development/codebase-exploration.md)
3. **Use**: [`templates/exploration-notes-template.md`](templates/exploration-notes-template.md)

### I need to write tests
1. **Start**: [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) → "Writing Tests"
2. **Follow**: [`guides/testing/test-writing-guide.md`](guides/testing/test-writing-guide.md)
3. **Reference**: Test examples in the testing guide

### I need to create a plan
1. **Start**: [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) → "Creating Implementation Plans"
2. **Follow**: [`guides/planning/planning-documentation.md`](guides/planning/planning-documentation.md)
3. **Use**: [`templates/feature-plan-template.md`](templates/feature-plan-template.md)

## 📚 Guide Details

### Core Workflow Guides

#### Feature Development Workflow
- **File**: [`guides/workflows/feature-development-workflow.md`](guides/workflows/feature-development-workflow.md)
- **Purpose**: Complete end-to-end feature development process
- **Phases**: Explore → Ask Questions → Plan → Review → Implement
- **Use When**: Building any new feature or significant change

#### Codebase Exploration
- **File**: [`guides/development/codebase-exploration.md`](guides/development/codebase-exploration.md)
- **Purpose**: Systematic approach to understanding unfamiliar code
- **Phases**: Overview → Architecture → Patterns → Dependencies → Testing
- **Use When**: Working with new or unfamiliar codebases

#### Planning & Documentation
- **File**: [`guides/planning/planning-documentation.md`](guides/planning/planning-documentation.md)
- **Purpose**: Creating effective plans and getting meaningful review
- **Includes**: Requirements analysis, technical research, plan templates
- **Use When**: Before implementing any significant changes

#### Test Writing Guide
- **File**: [`guides/testing/test-writing-guide.md`](guides/testing/test-writing-guide.md)
- **Purpose**: Comprehensive testing guidance for unit and integration tests
- **Approach**: Test-driven development with iterative implementation
- **Use When**: Writing any tests or implementing with testing

## 🛠️ Templates and Examples

### Templates
- **Feature Plan**: [`templates/feature-plan-template.md`](templates/feature-plan-template.md)
  - Complete plan structure for new features
  - Includes all sections needed for effective planning
  - Ready to copy and customize

- **Exploration Notes**: [`templates/exploration-notes-template.md`](templates/exploration-notes-template.md)
  - Structured template for codebase exploration findings
  - Helps organize and document exploration results
  - Reference for future development

### Examples
- **Complete Workflow**: [`examples/complete-workflow-example.md`](examples/complete-workflow-example.md)
  - Real-world example of the complete development workflow
  - Shows how all guides work together
  - Demonstrates best practices in action

## 🔄 Workflow Integration

### How the Guides Work Together
```
Start
  ↓
GUIDE_ROUTER.md (determine task type)
  ↓
┌─────────────────────────────────────────────────────────┐
│ Feature Development Workflow                            │
│ ├── Phase 1: Explore (→ Codebase Exploration)         │
│ ├── Phase 2: Ask Questions                             │
│ ├── Phase 3: Plan (→ Planning & Documentation)        │
│ ├── Phase 4: Review                                    │
│ └── Phase 5: Implement (→ Test Writing Guide)         │
└─────────────────────────────────────────────────────────┘
```

### Typical Usage Patterns

#### New Feature Development
1. [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) → Identify as "New Feature Development"
2. [`guides/workflows/feature-development-workflow.md`](guides/workflows/feature-development-workflow.md) → Follow complete workflow
3. [`guides/development/codebase-exploration.md`](guides/development/codebase-exploration.md) → Explore codebase (Phase 1)
4. [`guides/planning/planning-documentation.md`](guides/planning/planning-documentation.md) → Create plan (Phase 3)
5. [`guides/testing/test-writing-guide.md`](guides/testing/test-writing-guide.md) → Implement with tests (Phase 5)

#### Bug Fix or Maintenance
1. [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) → Identify as "Bug Fix"
2. [`guides/development/codebase-exploration.md`](guides/development/codebase-exploration.md) → Understand the code
3. [`guides/testing/test-writing-guide.md`](guides/testing/test-writing-guide.md) → Add tests if needed
4. [`guides/planning/planning-documentation.md`](guides/planning/planning-documentation.md) → Plan if complex

## 📖 Usage Instructions

### For First-Time Users
1. **Read**: [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) completely
2. **Understand**: The task routing system
3. **Identify**: Your specific task type
4. **Follow**: The recommended guide path
5. **Use**: Templates and examples as needed

### For Experienced Users
1. **Quick Reference**: [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) routing tables
2. **Direct Access**: Go directly to the appropriate guide
3. **Template Usage**: Copy templates for new tasks
4. **Example Reference**: Check examples for complex scenarios

### For Complex Projects
1. **Start**: With [`guides/workflows/feature-development-workflow.md`](guides/workflows/feature-development-workflow.md)
2. **Deep Dive**: Use all supporting guides as needed
3. **Document**: Create exploration notes and detailed plans
4. **Reference**: [`examples/complete-workflow-example.md`](examples/complete-workflow-example.md)

## 🎯 Success Metrics

### You're Using This Repository Well When:
- You consistently follow the systematic approaches
- You create and get approval for plans before implementing
- You write tests alongside implementation
- You document your exploration and findings
- You reference existing patterns and conventions

### You Know You're Done When:
- Your implementation matches the approved plan
- All tests pass and coverage is comprehensive
- Code follows established project patterns
- No regressions are introduced
- Documentation is updated appropriately

## 🤝 Integration with Development Tools

### Command Line Usage
```bash
# Quick access to guides
cat GUIDE_ROUTER.md | grep -A5 "task-type"

# Copy templates
cp templates/feature-plan-template.md plan-my-feature.md

# Reference examples
cat examples/complete-workflow-example.md | grep -A10 "Phase 1"
```

### IDE Integration
- Bookmark key files in your IDE
- Use snippet templates for common patterns
- Reference guides during code reviews
- Keep exploration notes in project directories

This index provides everything you need to navigate and use the AI tooling resources effectively. Start with the [`GUIDE_ROUTER.md`](GUIDE_ROUTER.md) and follow the systematic approaches for consistent, high-quality development outcomes.