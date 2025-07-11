# Codebase Exploration Guide

This guide provides systematic approaches for LLM tools to understand unfamiliar codebases efficiently and thoroughly before making any changes or additions.

## Core Exploration Strategy

### Exploration Phases
1. **High-Level Overview** - Project structure and technology stack
2. **Architecture Analysis** - Design patterns and system organization
3. **Code Pattern Discovery** - Conventions and coding styles
4. **Dependency Mapping** - External libraries and internal relationships
5. **Testing and Build Understanding** - Development workflow and processes

## Phase 1: High-Level Overview

### Project Structure Discovery
**Start with understanding the overall project organization.**

#### Essential Commands
```bash
# Get project overview
ls -la
tree -L 3 -I 'node_modules|.git|__pycache__'

# Find configuration files
find . -maxdepth 2 -name "*.json" -o -name "*.yml" -o -name "*.yaml" -o -name "*.toml" -o -name "*.ini"

# Identify project type and language
file $(find . -maxdepth 2 -name "package.json" -o -name "requirements.txt" -o -name "pom.xml" -o -name "build.gradle" -o -name "Cargo.toml" -o -name "go.mod")
```

#### Key Files to Examine
- **Package/Dependency Files**: `package.json`, `requirements.txt`, `pom.xml`, `build.gradle`, `Cargo.toml`
- **Configuration Files**: `tsconfig.json`, `webpack.config.js`, `jest.config.js`, `.env`
- **Documentation**: `README.md`, `CONTRIBUTING.md`, `docs/` directory
- **Build Files**: `Makefile`, `Dockerfile`, `.github/workflows/`

### Technology Stack Identification
**Determine what technologies and frameworks are being used.**

#### Framework Detection Commands
```bash
# JavaScript/TypeScript projects
grep -E "(react|vue|angular|express|nest)" package.json
grep -E "(typescript|javascript)" package.json

# Python projects
grep -E "(django|flask|fastapi|pytest)" requirements.txt setup.py
python --version 2>/dev/null || echo "Python not found"

# Java projects
grep -E "(spring|junit|maven|gradle)" pom.xml build.gradle
java -version 2>/dev/null || echo "Java not found"

# Database detection
grep -E "(mysql|postgres|mongodb|redis)" package.json requirements.txt pom.xml
```

#### Architecture Type Indicators
- **Monolithic**: Single large application structure
- **Microservices**: Multiple service directories, docker-compose files
- **Serverless**: Functions directory, serverless.yml
- **SPA**: Frontend build tools, API separation
- **Full-Stack**: Both frontend and backend in same repo

## Phase 2: Architecture Analysis

### Directory Structure Analysis
**Understand how code is organized and what patterns are used.**

#### Common Patterns to Look For
```bash
# MVC Pattern
find . -name "*controller*" -o -name "*model*" -o -name "*view*" | head -10

# Component-Based (React/Vue)
find . -name "*component*" -o -name "*components*" -type d | head -10

# Service Layer Pattern
find . -name "*service*" -o -name "*services*" -type d | head -10

# Domain-Driven Design
find . -name "*domain*" -o -name "*entity*" -o -name "*aggregate*" | head -10
```

#### Data Flow Analysis
```bash
# State Management
grep -r "redux\|vuex\|mobx\|context" . --include="*.js" --include="*.ts" | head -5

# API Integration
grep -r "axios\|fetch\|http" . --include="*.js" --include="*.ts" | head -5

# Database Integration
grep -r "prisma\|sequelize\|mongoose\|typeorm" . --include="*.js" --include="*.ts" | head -5
```

### Entry Points and Flow
**Identify how the application starts and processes requests.**

#### Application Entry Points
```bash
# Find main entry files
find . -name "main.*" -o -name "index.*" -o -name "app.*" | grep -v node_modules

# Package.json scripts
grep -A 10 -B 2 "scripts" package.json

# Server entry points
grep -r "listen\|createServer\|app\.listen" . --include="*.js" --include="*.ts" | head -5
```

## Phase 3: Code Pattern Discovery

### Naming Conventions
**Identify the project's naming and coding conventions.**

#### File and Directory Naming
```bash
# Check case conventions
ls | grep -E "[A-Z]" | head -5  # PascalCase files
ls | grep -E "[a-z].*[_-]" | head -5  # snake_case or kebab-case

# Component naming patterns
find . -name "*.jsx" -o -name "*.tsx" | head -10
find . -name "*.vue" | head -10
```

#### Code Style Analysis
```bash
# Check for linting configuration
find . -name ".eslintrc*" -o -name ".prettierrc*" -o -name "pyproject.toml"

# Indentation and style
head -20 $(find . -name "*.js" -o -name "*.ts" | head -1)
```

### Import/Export Patterns
**Understand how modules are organized and imported.**

#### Module System Detection
```bash
# ES6 modules vs CommonJS
grep -r "import.*from\|export" . --include="*.js" --include="*.ts" | head -5
grep -r "require\|module.exports" . --include="*.js" | head -5

# Path alias patterns
grep -r "import.*@\/" . --include="*.js" --include="*.ts" | head -5
```

#### Dependency Injection Patterns
```bash
# Constructor injection
grep -r "constructor.*inject\|@Injectable\|@Component" . --include="*.js" --include="*.ts" | head -5

# Service location patterns
grep -r "getService\|resolve\|container" . --include="*.js" --include="*.ts" | head -5
```

## Phase 4: Dependency Mapping

### External Dependencies
**Catalog and understand external libraries and their usage.**

#### Dependency Analysis Commands
```bash
# List all dependencies
npm list --depth=0 2>/dev/null || echo "No npm dependencies"
pip list 2>/dev/null || echo "No pip dependencies"
mvn dependency:tree 2>/dev/null || echo "No Maven dependencies"

# Find usage of major libraries
grep -r "lodash\|axios\|moment\|jquery" . --include="*.js" --include="*.ts" | head -5
```

#### Critical Dependencies to Identify
- **UI Frameworks**: React, Vue, Angular, jQuery
- **State Management**: Redux, Vuex, MobX
- **HTTP Clients**: Axios, Fetch, Request
- **Testing**: Jest, Mocha, Pytest, JUnit
- **Database**: Prisma, Sequelize, SQLAlchemy
- **Utilities**: Lodash, Ramda, Date-fns

### Internal Dependencies
**Map relationships between different parts of the codebase.**

#### Relationship Discovery
```bash
# Find shared utilities
find . -name "*util*" -o -name "*helper*" -o -name "*common*" | head -10

# Identify shared components
find . -name "*shared*" -o -name "*common*" -o -name "*core*" -type d | head -10

# Cross-module imports
grep -r "import.*\.\./\.\." . --include="*.js" --include="*.ts" | head -5
```

## Phase 5: Testing and Build Understanding

### Test Infrastructure
**Understand how tests are structured and executed.**

#### Test Discovery Commands
```bash
# Find test files
find . -name "*.test.*" -o -name "*.spec.*" -o -name "*_test.*" | head -10

# Test configuration
find . -name "jest.config.*" -o -name "pytest.ini" -o -name "karma.conf.*"

# Test directories
find . -name "__tests__" -o -name "tests" -o -name "test" -type d
```

#### Test Pattern Analysis
```bash
# Testing frameworks
grep -r "describe\|it\|test\|expect" . --include="*.js" --include="*.ts" | head -5
grep -r "pytest\|unittest\|assert" . --include="*.py" | head -5

# Mock patterns
grep -r "mock\|stub\|spy" . --include="*.js" --include="*.ts" | head -5
```

### Build and Development Workflow
**Understand the development and deployment process.**

#### Build System Analysis
```bash
# Build tools
find . -name "webpack.config.*" -o -name "rollup.config.*" -o -name "vite.config.*"

# Package scripts
grep -A 20 "scripts" package.json | grep -E "(build|dev|test|start)"

# Environment configuration
find . -name ".env*" -o -name "config.js" -o -name "config.json"
```

## Exploration Methodology

### Systematic Approach
**Follow a structured process to avoid missing important details.**

#### Phase-by-Phase Checklist
**Phase 1: High-Level Overview**
- [ ] Project structure understood
- [ ] Technology stack identified
- [ ] Key configuration files reviewed
- [ ] Documentation examined

**Phase 2: Architecture Analysis**
- [ ] Architectural patterns identified
- [ ] Directory organization understood
- [ ] Entry points located
- [ ] Data flow comprehended

**Phase 3: Code Pattern Discovery**
- [ ] Naming conventions documented
- [ ] Import/export patterns understood
- [ ] Coding style identified
- [ ] Dependency injection patterns found

**Phase 4: Dependency Mapping**
- [ ] External dependencies catalogued
- [ ] Internal relationships mapped
- [ ] Shared utilities identified
- [ ] Cross-module dependencies understood

**Phase 5: Testing and Build**
- [ ] Test infrastructure understood
- [ ] Build process documented
- [ ] Development workflow identified
- [ ] Deployment process comprehended

### Documentation During Exploration
**Keep track of findings for later reference.**

#### Exploration Notes Template
```markdown
# Codebase Exploration Notes

## Project Overview
- **Type**: [Web app/API/Library/etc.]
- **Language**: [JavaScript/Python/Java/etc.]
- **Framework**: [React/Django/Spring/etc.]
- **Architecture**: [Monolithic/Microservices/Serverless/etc.]

## Key Directories
- `src/` - [Description]
- `tests/` - [Description]
- `config/` - [Description]

## Important Files
- `package.json` - [Key dependencies and scripts]
- `README.md` - [Setup and usage instructions]
- `config.js` - [Configuration details]

## Patterns and Conventions
- **Naming**: [PascalCase/camelCase/snake_case]
- **File Organization**: [By feature/By type/Hybrid]
- **Import Style**: [Absolute/Relative/Mixed]

## Dependencies
- **UI**: [React 18, Material-UI]
- **State**: [Redux Toolkit]
- **Testing**: [Jest, React Testing Library]
- **Build**: [Webpack, Babel]

## Testing Setup
- **Framework**: [Jest]
- **Location**: [__tests__ directories]
- **Command**: [npm test]

## Build Process
- **Development**: [npm run dev]
- **Production**: [npm run build]
- **Testing**: [npm test]
```

## Common Exploration Patterns

### Frontend Applications
```bash
# React/Vue/Angular specific
find . -name "*.jsx" -o -name "*.tsx" -o -name "*.vue" | head -10
grep -r "useState\|useEffect\|computed\|@Component" . --include="*.js" --include="*.ts" | head -5

# Styling approaches
find . -name "*.css" -o -name "*.scss" -o -name "*.less" | head -10
grep -r "styled-components\|emotion\|tailwind" . --include="*.js" --include="*.ts" | head -5
```

### Backend Applications
```bash
# API endpoints
grep -r "app\.get\|app\.post\|@GetMapping\|@PostMapping" . --include="*.js" --include="*.ts" --include="*.java" | head -5

# Database connections
grep -r "connect\|createConnection\|DataSource" . --include="*.js" --include="*.ts" | head -5

# Middleware patterns
grep -r "middleware\|interceptor\|filter" . --include="*.js" --include="*.ts" | head -5
```

### Full-Stack Applications
```bash
# API routes
find . -name "*route*" -o -name "*api*" | head -10

# Database models
find . -name "*model*" -o -name "*schema*" | head -10

# Frontend/backend separation
ls | grep -E "(client|frontend|ui|web)" && ls | grep -E "(server|backend|api)"
```

## Troubleshooting Exploration

### When Exploration is Unclear
- **Start Smaller**: Focus on one component or feature at a time
- **Ask Questions**: Request clarification on confusing patterns
- **Check Documentation**: Look for architecture decision records or design docs
- **Trace Execution**: Follow a simple request through the system

### When Patterns Don't Match Standards
- **Document Deviations**: Note unusual patterns for discussion
- **Understand Rationale**: Try to understand why patterns exist
- **Propose Alternatives**: Suggest standard patterns if appropriate
- **Respect Existing**: Don't force changes without understanding reasons

## Integration with Feature Development

### Before Feature Planning
- Complete all exploration phases
- Document findings in exploration notes
- Identify similar existing features
- Understand integration points

### During Feature Development
- Refer back to exploration notes
- Follow discovered patterns and conventions
- Leverage identified utilities and services
- Maintain architectural consistency

### After Feature Completion
- Update exploration notes if new patterns discovered
- Document any new conventions introduced
- Share findings with team if applicable

This systematic exploration approach ensures comprehensive understanding of any codebase before making changes, leading to better decisions and higher quality implementations.