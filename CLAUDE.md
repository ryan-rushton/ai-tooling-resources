# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a documentation repository containing systematic guidance for LLM-powered development tools. The repository has **no build system, dependencies, or code to execute** - it contains only markdown documentation files organized to help LLM tools navigate development tasks effectively.

## Core Architecture

### Navigation System
The repository uses a hierarchical routing system where **all work starts with `GUIDE_ROUTER.md`**:

```
GUIDE_ROUTER.md (entry point)
├── guides/workflows/feature-development-workflow.md (master workflow)
├── guides/development/codebase-exploration.md (exploration methodology)
├── guides/planning/planning-documentation.md (planning processes)
└── guides/testing/test-writing-guide.md (testing approaches)
```

### Workflow Integration
The guides are designed to work together in a specific sequence:
1. **Explore** (codebase-exploration.md) → 2. **Plan** (planning-documentation.md) → 3. **Review** → 4. **Implement** (with test-writing-guide.md)

## Common Commands

Since this is a documentation repository, the primary commands are for navigation and template usage:

### Navigation Commands
```bash
# Start any task - read the router first
cat GUIDE_ROUTER.md

# Follow task-specific routing
cat guides/workflows/feature-development-workflow.md      # For new development
cat guides/development/codebase-exploration.md           # For understanding code
cat guides/planning/planning-documentation.md            # For creating plans
cat guides/testing/test-writing-guide.md                # For writing tests
cat guides/development/error-handling-debugging.md      # For debugging/troubleshooting
cat guides/development/code-review-refactoring.md       # For improving existing code
```

### Template Usage
```bash
# Copy templates for new work
cp templates/feature-plan-template.md plan-[feature-name].md
cp templates/bug-fix-plan-template.md plan-fix-[issue-name].md
cp templates/refactoring-plan-template.md plan-refactor-[component].md
cp templates/exploration-notes-template.md notes-[project-name].md

# Reference complete examples
cat examples/complete-workflow-example.md
```

### Quick Reference
```bash
# Find specific guidance
grep -r "keyword" guides/
grep -A10 -B5 "specific-pattern" guides/

# Navigate directory structure
ls guides/workflows/    # End-to-end processes (feature-development-workflow)
ls guides/development/  # Development-specific guidance (codebase-exploration, error-handling-debugging, code-review-refactoring)
ls guides/planning/     # Planning and documentation (planning-documentation)
ls guides/testing/      # Testing strategies (test-writing-guide)
ls templates/           # All available templates
```

## Repository Design Principles

### Document Structure
- **Self-contained guides**: Each guide can be read independently but references others
- **Template-driven**: Standardized templates for consistent output
- **Example-supported**: Real-world examples demonstrate the methodology
- **LLM-optimized**: Concrete commands and systematic approaches

### Routing Philosophy
- **Single entry point**: Always start with `GUIDE_ROUTER.md`
- **Task-based navigation**: Route to guides based on what you need to accomplish
- **Hierarchical support**: Primary guides supported by secondary guides
- **Emergency fallbacks**: Clear instructions when uncertain about routing

## Key Behavioral Patterns

### Always Start with Routing
Never work directly on development tasks without first reading `GUIDE_ROUTER.md` to understand the appropriate methodology.

### Follow the Systematic Approach
The repository enforces a specific sequence: **Explore → Plan → Review → Implement**. This is not optional - it's the core architecture.

### Use Templates Consistently
All planning and documentation should use the provided templates to ensure consistency and completeness.

### Reference Examples
The `examples/` directory contains complete workflow examples that demonstrate how all guides integrate together.

## Integration Points

### With External Codebases
When working on actual code projects, use this repository's guidance to:
1. **Systematically explore** the target codebase using `guides/development/codebase-exploration.md`
2. **Create plans** using `templates/feature-plan-template.md`
3. **Write tests** following `guides/testing/test-writing-guide.md`
4. **Document findings** using `templates/exploration-notes-template.md`

### With Human Reviewers
The planning guides emphasize human review processes - always create reviewable plans before implementation and get explicit approval.

## Repository Maintenance

### File Organization
- **guides/**: Core methodology documents
- **templates/**: Copy-ready templates for consistent output
- **examples/**: Complete workflow demonstrations
- **GUIDE_ROUTER.md**: Primary navigation system
- **INDEX.md**: Comprehensive reference guide

### Content Updates
When updating guides, maintain the integration points between documents and update the routing tables in `GUIDE_ROUTER.md` if new guides are added.

This repository is designed to be a complete system for systematic development - use it as intended by following the routing system and systematic approaches.