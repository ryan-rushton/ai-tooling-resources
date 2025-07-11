# Planning and Documentation Guide

This guide provides systematic approaches for LLM tools to create effective plans, documentation, and get meaningful human review before implementation.

## Core Planning Principles

### Planning Philosophy
- **Plans are Communication Tools**: Plans should clearly convey intent to both humans and future AI sessions
- **Specificity Over Generality**: Concrete details prevent ambiguity and implementation drift
- **Iterative Refinement**: Plans should be refined through human feedback before implementation
- **Living Documents**: Plans should be updated when implementation reveals new insights

### Planning Hierarchy
1. **Strategic Planning** - High-level approach and architecture decisions
2. **Tactical Planning** - Specific implementation steps and file changes
3. **Operational Planning** - Detailed task breakdown and acceptance criteria

## Plan Structure and Content

### Universal Plan Template
```markdown
# [Feature/Change Name]

## Overview
### Purpose
Brief description of what this change accomplishes and why it's needed.

### Success Criteria
- [ ] Criterion 1: [Specific, measurable outcome]
- [ ] Criterion 2: [Specific, measurable outcome]
- [ ] Criterion 3: [Specific, measurable outcome]

## Technical Analysis
### Current State
- Relevant existing code and architecture
- Dependencies and constraints
- Integration points

### Proposed Changes
- Architecture/design decisions
- New components/modules to create
- Existing components to modify
- Data flow changes

## Implementation Plan
### Phase 1: [Phase Name]
**Objective**: [What this phase accomplishes]
**Steps**:
1. [Specific action with file paths]
2. [Specific action with file paths]
3. [Specific action with file paths]

**Acceptance Criteria**:
- [ ] [Specific testable outcome]
- [ ] [Specific testable outcome]

### Phase 2: [Phase Name]
[Same structure as Phase 1]

## File Changes
### Files to Create
- `path/to/new/file.ext` - [Purpose and key functionality]
- `path/to/another/file.ext` - [Purpose and key functionality]

### Files to Modify
- `path/to/existing/file.ext` - [What changes and why]
- `path/to/another/existing.ext` - [What changes and why]

## Testing Strategy
### Unit Tests
- [Component/function to test] - [Test scenarios]
- [Component/function to test] - [Test scenarios]

### Integration Tests
- [Integration point to test] - [Test scenarios]
- [Integration point to test] - [Test scenarios]

### Manual Testing
- [User scenario to test manually]
- [Edge case to verify]

## Risks and Mitigation
### High Risk
- **Risk**: [Specific risk description]
- **Impact**: [What happens if this occurs]
- **Mitigation**: [How to prevent or handle]

### Medium Risk
- **Risk**: [Specific risk description]
- **Mitigation**: [How to prevent or handle]

## Dependencies and Assumptions
### External Dependencies
- [Dependency name] - [How it's used and version requirements]

### Internal Dependencies
- [Existing component/service] - [How it's used]

### Assumptions
- [Assumption 1] - [Impact if assumption is wrong]
- [Assumption 2] - [Impact if assumption is wrong]

## Questions for Review
1. [Specific question about approach/architecture]
2. [Specific question about implementation details]
3. [Specific question about testing/deployment]
```

## Plan Creation Process

### Step 1: Requirements Analysis
**Before creating any plan, thoroughly understand the requirements.**

#### Requirements Gathering Checklist
- [ ] Functional requirements clearly defined
- [ ] Non-functional requirements identified (performance, security, etc.)
- [ ] User stories or use cases documented
- [ ] Success criteria established
- [ ] Constraints and limitations understood
- [ ] Integration requirements specified

#### Requirements Documentation Template
```markdown
## Requirements Analysis

### Functional Requirements
1. **FR-1**: [Specific functional requirement]
   - **Description**: [Detailed description]
   - **Acceptance Criteria**: [How to verify it's met]

2. **FR-2**: [Another functional requirement]
   - **Description**: [Detailed description]
   - **Acceptance Criteria**: [How to verify it's met]

### Non-Functional Requirements
- **Performance**: [Specific performance requirements]
- **Security**: [Security requirements and constraints]
- **Scalability**: [Scalability requirements]
- **Maintainability**: [Maintainability requirements]

### User Stories
- **As a** [user type], **I want** [functionality] **so that** [benefit/value]
- **As a** [user type], **I want** [functionality] **so that** [benefit/value]

### Constraints
- **Technical**: [Technical constraints]
- **Business**: [Business constraints]
- **Timeline**: [Timeline constraints]
```

### Step 2: Technical Research
**Research the technical landscape before proposing solutions.**

#### Research Areas
- **Existing Solutions**: Similar features in the codebase
- **Framework Patterns**: Standard patterns for the technology stack
- **Library Options**: Available libraries and their trade-offs
- **Architecture Implications**: Impact on existing architecture

#### Research Documentation
```markdown
## Technical Research

### Existing Similar Features
- **Feature Name**: [Location] - [How it works and what to learn from it]
- **Feature Name**: [Location] - [How it works and what to learn from it]

### Framework Patterns
- **Pattern Name**: [How it's used in this project]
- **Pattern Name**: [How it's used in this project]

### Library Analysis
| Library | Pros | Cons | Recommendation |
|---------|------|------|----------------|
| Library A | [Advantages] | [Disadvantages] | [Use/Don't Use] |
| Library B | [Advantages] | [Disadvantages] | [Use/Don't Use] |

### Architecture Impact
- **Impact on [Component]**: [Description of impact]
- **Impact on [Component]**: [Description of impact]
```

### Step 3: Solution Design
**Design the solution based on requirements and research.**

#### Design Principles
- **Consistency**: Follow existing patterns and conventions
- **Modularity**: Create reusable, testable components
- **Separation of Concerns**: Clear boundaries between responsibilities
- **Extensibility**: Design for future enhancements

#### Design Documentation
```markdown
## Solution Design

### Architecture Overview
[High-level architecture diagram in text/ASCII or description]

### Component Design
#### Component 1: [Name]
- **Purpose**: [What it does]
- **Interface**: [Public API/methods]
- **Dependencies**: [What it depends on]
- **Location**: [Where it will be placed]

#### Component 2: [Name]
- **Purpose**: [What it does]
- **Interface**: [Public API/methods]
- **Dependencies**: [What it depends on]
- **Location**: [Where it will be placed]

### Data Flow
1. [Step 1 of data flow]
2. [Step 2 of data flow]
3. [Step 3 of data flow]

### API Design (if applicable)
```json
{
  "endpoint": "/api/example",
  "method": "POST",
  "request": {
    "field1": "string",
    "field2": "number"
  },
  "response": {
    "id": "string",
    "status": "string"
  }
}
```
```

### Step 4: Implementation Planning
**Break down the solution into concrete implementation steps.**

#### Implementation Breakdown Principles
- **Incremental**: Each step should produce a working state
- **Testable**: Each step should be verifiable
- **Reversible**: Each step should be easy to undo if needed
- **Logical**: Steps should follow a logical dependency order

#### Implementation Steps Template
```markdown
## Implementation Steps

### Step 1: [Foundation/Setup]
**Objective**: [What this step accomplishes]
**Duration**: [Estimated time]
**Files**:
- Create: `path/to/file.ext`
- Modify: `path/to/existing.ext`

**Tasks**:
1. [Specific task with details]
2. [Specific task with details]
3. [Specific task with details]

**Verification**:
- [ ] [How to verify this step is complete]
- [ ] [Another verification point]

**Rollback**: [How to undo this step if needed]

### Step 2: [Core Implementation]
[Same structure as Step 1]

### Step 3: [Integration]
[Same structure as Step 1]

### Step 4: [Testing and Polish]
[Same structure as Step 1]
```

## Human Review Process

### Review Preparation
**Prepare the plan for effective human review.**

#### Review Package Components
- **Main Plan Document**: Complete plan following the template
- **Supporting Research**: Technical research and analysis
- **Visual Aids**: Diagrams, flowcharts, or mockups if helpful
- **Specific Questions**: Targeted questions for human input

#### Review Request Template
```markdown
## Plan Review Request

### Summary
I've created a comprehensive plan for [feature/change name]. The plan includes:
- [X] implementation phases
- [Y] files to create/modify
- Testing strategy covering [areas]
- Risk analysis and mitigation strategies

### Key Decisions for Review
1. **[Decision 1]**: [Description and rationale]
2. **[Decision 2]**: [Description and rationale]
3. **[Decision 3]**: [Description and rationale]

### Specific Questions
1. [Question about architecture/approach]
2. [Question about implementation details]
3. [Question about testing/deployment]

### Files to Review
- `plan-[feature-name].md` - Main implementation plan
- `research-[feature-name].md` - Technical research (if separate)

### Timeline
- **Planning**: [Time spent on planning]
- **Estimated Implementation**: [Estimated implementation time]
- **Review Required By**: [When feedback is needed]

Please review and provide feedback on:
- Technical approach and architecture decisions
- Implementation phases and order
- Testing strategy completeness
- Risk assessment and mitigation
- Any missing considerations
```

### Review Feedback Handling
**Systematically address all feedback.**

#### Feedback Processing Steps
1. **Categorize Feedback**: Group feedback by type (technical, scope, process, etc.)
2. **Prioritize Changes**: Identify blocking issues vs. suggestions
3. **Update Plan**: Revise plan based on feedback
4. **Address Questions**: Provide clarification or additional research
5. **Request Re-review**: When significant changes are made

#### Feedback Response Template
```markdown
## Response to Plan Review Feedback

### Changes Made
#### Major Changes
- **Change 1**: [What was changed and why]
- **Change 2**: [What was changed and why]

#### Minor Changes
- **Change 1**: [What was changed]
- **Change 2**: [What was changed]

### Questions Addressed
1. **Q**: [Original question]
   **A**: [Detailed answer with rationale]

2. **Q**: [Original question]
   **A**: [Detailed answer with rationale]

### Outstanding Questions
1. [Question still needing clarification]
2. [Question for follow-up discussion]

### Updated Files
- `plan-[feature-name].md` - Updated with feedback
- `research-[feature-name].md` - Additional research added

### Ready for Implementation
- [ ] All blocking feedback addressed
- [ ] Plan updated and finalized
- [ ] Implementation approach confirmed
- [ ] Testing strategy approved
```

## Documentation During Implementation

### Progress Documentation
**Keep stakeholders informed during implementation.**

#### Progress Update Template
```markdown
## Implementation Progress Update

### Completed
- [Step/Phase]: [Brief description of what was completed]
- [Step/Phase]: [Brief description of what was completed]

### In Progress
- [Current Step/Phase]: [What's currently being worked on]
- [Expected Completion]: [Timeline estimate]

### Upcoming
- [Next Step/Phase]: [What's coming next]
- [Dependencies]: [What's needed to proceed]

### Blockers
- [Blocker 1]: [Description and impact]
- [Blocker 2]: [Description and impact]

### Deviations from Plan
- [Deviation 1]: [What changed and why]
- [Deviation 2]: [What changed and why]

### Questions/Decisions Needed
1. [Question requiring human input]
2. [Decision point requiring approval]
```

### Change Documentation
**Document any changes to the original plan.**

#### Change Log Template
```markdown
## Plan Change Log

### Change 1: [Change Description]
- **Date**: [When change was made]
- **Reason**: [Why the change was necessary]
- **Impact**: [What parts of the plan were affected]
- **Approval**: [Who approved the change]

### Change 2: [Change Description]
- **Date**: [When change was made]
- **Reason**: [Why the change was necessary]
- **Impact**: [What parts of the plan were affected]
- **Approval**: [Who approved the change]
```

## Plan Quality Assurance

### Plan Quality Checklist
**Ensure plans meet quality standards before review.**

#### Content Quality
- [ ] Purpose and objectives clearly stated
- [ ] Success criteria specific and measurable
- [ ] Technical approach well-reasoned
- [ ] Implementation steps concrete and actionable
- [ ] File changes explicitly listed
- [ ] Testing strategy comprehensive
- [ ] Risks identified and mitigated
- [ ] Dependencies and assumptions documented

#### Communication Quality
- [ ] Language clear and jargon-free
- [ ] Structure logical and easy to follow
- [ ] Visual aids used where helpful
- [ ] Specific questions highlighted
- [ ] Timeline and effort estimates provided
- [ ] Review requirements clearly stated

#### Technical Quality
- [ ] Follows project patterns and conventions
- [ ] Considers existing architecture
- [ ] Addresses scalability and maintainability
- [ ] Includes appropriate error handling
- [ ] Considers security implications
- [ ] Includes performance considerations

### Common Planning Pitfalls

#### Insufficient Detail
- **Problem**: Plan too high-level to be actionable
- **Solution**: Include specific file paths, function names, and implementation details
- **Test**: Could another developer implement from the plan alone?

#### Missing Context
- **Problem**: Plan doesn't explain why decisions were made
- **Solution**: Include rationale for all major decisions
- **Test**: Are the trade-offs and alternatives clear?

#### Unrealistic Scope
- **Problem**: Plan tries to accomplish too much at once
- **Solution**: Break large features into smaller, independent phases
- **Test**: Can each phase be implemented and tested independently?

#### Inadequate Risk Assessment
- **Problem**: Plan doesn't identify potential problems
- **Solution**: Systematically consider what could go wrong
- **Test**: Are the biggest risks identified with mitigation strategies?

## Plan Templates by Project Type

### Frontend Feature Plan
```markdown
# Frontend Feature: [Feature Name]

## User Experience
### User Stories
- As a [user type], I want [functionality] so that [benefit]

### User Flow
1. [Step 1 of user interaction]
2. [Step 2 of user interaction]
3. [Step 3 of user interaction]

### UI Components
- **Component 1**: [Purpose and behavior]
- **Component 2**: [Purpose and behavior]

## Technical Implementation
### State Management
- [State needed and how it's managed]

### API Integration
- [Endpoints used and data flow]

### Styling Approach
- [CSS/styling strategy]

## Testing Strategy
### Unit Tests
- [Component testing approach]

### Integration Tests
- [User flow testing approach]

### Accessibility Testing
- [A11y testing approach]
```

### Backend Feature Plan
```markdown
# Backend Feature: [Feature Name]

## API Design
### Endpoints
- `GET /api/resource` - [Description]
- `POST /api/resource` - [Description]

### Data Models
- **Model 1**: [Fields and relationships]
- **Model 2**: [Fields and relationships]

## Technical Implementation
### Database Changes
- [Schema changes needed]

### Service Layer
- [Business logic organization]

### Integration Points
- [External services or APIs]

## Testing Strategy
### Unit Tests
- [Service/model testing]

### Integration Tests
- [API endpoint testing]

### Performance Testing
- [Load/performance considerations]
```

This comprehensive planning approach ensures that all implementation work is well-thought-out, properly reviewed, and effectively communicated to all stakeholders.