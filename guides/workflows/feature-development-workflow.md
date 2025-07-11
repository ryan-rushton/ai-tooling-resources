# Feature Development Workflow Guide

This guide provides a systematic approach for LLM tools to develop new features from initial requirements to complete implementation, emphasizing exploration, planning, and iterative development.

## Core Workflow Overview

The feature development process follows these phases:
1. **Explore** - Understand the codebase and requirements
2. **Ask Questions** - Gather context and clarify requirements
3. **Plan** - Create detailed implementation plan
4. **Review** - Get human approval before implementation
5. **Implement** - Build feature iteratively with tests

## Phase 1: Codebase Exploration

### Initial Discovery
**Before starting any feature development, systematically explore the codebase.**

- **Project Structure Analysis**: Use the Codebase Exploration Guide to understand:
  - Directory structure and organization patterns
  - Key configuration files
  - Dependencies and frameworks in use
  - Existing similar features or components
- **Architecture Understanding**: Identify:
  - Application architecture patterns (MVC, microservices, etc.)
  - Data flow and state management
  - API patterns and conventions
  - Database schema and relationships
- **Code Patterns**: Look for:
  - Naming conventions
  - File organization patterns
  - Import/export patterns
  - Error handling approaches

### Targeted Exploration Commands
```bash
# Project structure overview
find . -type f -name "*.json" -o -name "*.yml" -o -name "*.yaml" | head -20
ls -la

# Find similar features or components
find . -name "*component*" -o -name "*feature*" -o -name "*module*" | head -20
grep -r "similar_functionality" . --include="*.js" --include="*.ts" --include="*.py"

# Identify frameworks and dependencies
cat package.json | grep -E "(dependencies|devDependencies)" -A 20
cat requirements.txt setup.py 2>/dev/null || echo "No Python requirements found"
```

### Exploration Checklist
- [ ] Understand overall project architecture
- [ ] Identify similar existing features
- [ ] Locate relevant configuration files
- [ ] Understand testing setup and patterns
- [ ] Identify development and build processes
- [ ] Find documentation or README files

## Phase 2: Context Gathering and Questions

### Systematic Question Framework
**Ask targeted questions to clarify requirements and gather missing context.**

#### Technical Context Questions
- **Framework-Specific**: "I see you're using [Framework]. Are there specific patterns or conventions I should follow?"
- **Integration Points**: "How should this feature integrate with [existing system/component]?"
- **Performance Requirements**: "Are there performance considerations or constraints I should be aware of?"
- **Security Considerations**: "Are there security requirements or authentication patterns to follow?"

#### Business Context Questions
- **User Experience**: "What's the expected user flow for this feature?"
- **Edge Cases**: "What edge cases or error scenarios should I handle?"
- **Scope Boundaries**: "What's included/excluded in this feature scope?"
- **Success Criteria**: "How will we know this feature is working correctly?"

#### Implementation Context Questions
- **Existing Patterns**: "Should I follow the pattern I see in [similar feature]?"
- **Dependencies**: "Are there existing utilities or services I should leverage?"
- **Testing Strategy**: "What level of testing is expected (unit, integration, e2e)?"
- **Deployment**: "Are there deployment or environment considerations?"

### Question Prioritization
1. **Critical Blockers**: Questions that prevent starting development
2. **Architecture Decisions**: Questions affecting overall implementation approach
3. **Implementation Details**: Questions about specific technical choices
4. **Nice-to-Have**: Questions that can be addressed during development

## Phase 3: Planning and Documentation

### Plan Creation Process
**Create a detailed implementation plan before starting development.**

#### Plan Structure Template
```markdown
# Feature: [Feature Name]

## Overview
Brief description of what this feature does and why it's needed.

## Technical Approach
- Architecture pattern to follow
- Key components to create/modify
- Integration points with existing code

## Implementation Steps
1. [Step 1: Setup and scaffolding]
2. [Step 2: Core functionality]
3. [Step 3: Integration points]
4. [Step 4: Testing]
5. [Step 5: Documentation and cleanup]

## Files to Create/Modify
- `/path/to/new/component.tsx` - New component
- `/path/to/existing/service.ts` - Modify existing service
- `/path/to/tests/component.test.tsx` - Unit tests

## Testing Strategy
- Unit tests for [specific components]
- Integration tests for [system interactions]
- Manual testing scenarios

## Assumptions and Dependencies
- Assumption 1: [What we're assuming]
- Dependency 1: [What we need from existing code]

## Questions/Risks
- Risk 1: [Potential issue and mitigation]
- Question 1: [Unresolved question]
```

#### Plan Location
- **Create in Target Directory**: Place plan file in the directory where new components will be created
- **Naming Convention**: Use descriptive names like `feature-plan-user-authentication.md`
- **Version Control**: Include in git for tracking and collaboration

### Plan Quality Checklist
- [ ] Clear feature description and purpose
- [ ] Detailed technical approach
- [ ] Step-by-step implementation plan
- [ ] Comprehensive file list (create/modify)
- [ ] Testing strategy defined
- [ ] Assumptions and dependencies listed
- [ ] Risks and open questions identified
- [ ] Plan is specific enough to implement without ambiguity

## Phase 4: Human Review and Approval

### Review Request Process
**Always get human approval before implementing.**

#### Review Request Template
```markdown
I've created a detailed implementation plan for [Feature Name]. The plan includes:

- Technical approach using [architecture/patterns]
- [X] implementation steps
- [Y] files to create/modify
- Testing strategy covering [unit/integration/e2e]

Please review the plan at: [path/to/plan.md]

Key decisions for your review:
1. [Decision 1]: [Rationale]
2. [Decision 2]: [Rationale]

Questions for clarification:
- [Question 1]
- [Question 2]

Once approved, I'll proceed with iterative implementation following the test-driven approach.
```

#### Review Criteria
- **Technical Soundness**: Does the approach align with project architecture?
- **Completeness**: Are all requirements addressed?
- **Testability**: Is the testing strategy comprehensive?
- **Maintainability**: Will the code be easy to maintain and extend?
- **Risk Management**: Are potential issues identified and mitigated?

### Handling Review Feedback
- **Plan Updates**: Revise plan based on feedback
- **Clarification**: Ask follow-up questions if feedback is unclear
- **Alternative Approaches**: Propose alternatives if suggested approach isn't feasible
- **Re-review**: Request re-review after significant changes

## Phase 5: Iterative Implementation

### Implementation Approach
**Follow test-driven, iterative development with comprehensive testing integration.**

#### Testing Guide Integration
**Reference the Test Writing Guide**: Use [`guides/testing/test-writing-guide.md`](../testing/test-writing-guide.md) throughout implementation. The test writing guide provides:
- **Comprehensive testing strategies** (unit, integration, end-to-end)
- **Test-driven development workflows** that integrate with this feature development process
- **Framework-specific testing patterns** based on codebase exploration findings
- **Code coverage and quality metrics** to ensure feature robustness

#### How Testing Integrates with Feature Development
1. **Pre-implementation**: Review existing test patterns (from Phase 1 exploration) to understand project testing conventions
2. **Test Setup**: Use the guide's framework detection to set up appropriate testing infrastructure
3. **TDD Cycles**: Follow the guide's red-green-refactor methodology for each feature component
4. **Integration Testing**: Apply the guide's integration testing strategies when connecting new features to existing systems
5. **Quality Assurance**: Use the guide's coverage and quality metrics to ensure comprehensive testing

#### Implementation Cycle
1. **Re-read Plan**: Always re-read the approved plan before starting implementation
2. **Start Small**: Begin with the simplest component or function
3. **Test First**: Write tests before implementation (follow Test Writing Guide methodology)
4. **Implement**: Build the minimal working version
5. **Verify**: Run tests and manual verification
6. **Iterate**: Move to next component/feature

#### Step-by-Step Process
```markdown
For each implementation step:

1. **Setup Phase**:
   - Create test file skeleton
   - Set up basic test infrastructure
   - Verify test runner works

2. **Development Phase**:
   - Write failing test for desired behavior
   - Implement minimal code to pass test
   - Refactor and improve code quality
   - Add additional tests for edge cases

3. **Integration Phase**:
   - Test integration with existing code
   - Update related components if needed
   - Verify no regressions introduced

4. **Documentation Phase**:
   - Add inline comments for complex logic
   - Update relevant documentation
   - Create usage examples if needed
```

### Progress Tracking
- **Status Updates**: Provide regular updates on implementation progress
- **Blockers**: Immediately escalate any blockers or unexpected issues
- **Scope Changes**: Discuss any needed scope adjustments
- **Testing Results**: Share test results and coverage information

## Quality Gates and Checkpoints

### Before Implementation
- [ ] Codebase thoroughly explored
- [ ] All critical questions answered
- [ ] Detailed plan created and approved
- [ ] Testing strategy defined
- [ ] Implementation approach validated

### During Implementation
- [ ] Following test-driven development
- [ ] Each component tested before moving to next
- [ ] Integration points verified
- [ ] Code follows project conventions
- [ ] No regressions introduced

### After Implementation
- [ ] All tests passing
- [ ] Manual testing completed
- [ ] Documentation updated
- [ ] Code reviewed for quality
- [ ] Plan vs. implementation alignment verified

## Common Pitfalls and Solutions

### Insufficient Exploration
- **Problem**: Starting development without understanding codebase
- **Solution**: Always complete exploration phase first
- **Time Investment**: Spend 20-30% of time on exploration

### Vague Planning
- **Problem**: Plans too high-level to be actionable
- **Solution**: Include specific file paths, function names, and test cases
- **Detail Level**: Plan should be specific enough for another developer to implement

### Implementation Drift
- **Problem**: Implementation diverges from approved plan
- **Solution**: Regularly refer back to plan during development
- **Checkpoint**: Review plan alignment after each major component

### Testing Shortcuts
- **Problem**: Skipping tests to move faster
- **Solution**: Strict adherence to test-first approach
- **Mindset**: Tests are development tools, not post-development tasks

## Success Metrics

### Planning Quality
- Human approves plan without major revisions
- Implementation follows plan with minimal deviations
- No major architectural surprises during development

### Implementation Quality
- All tests pass on first attempt
- Code follows established project patterns
- No regressions introduced to existing functionality

### Process Efficiency
- Clear understanding of requirements before starting
- Minimal back-and-forth during implementation
- Feature delivered matches original requirements

This workflow ensures systematic, well-planned feature development that minimizes risks and maximizes code quality while maintaining clear communication with human collaborators.