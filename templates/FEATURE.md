# Feature-Specific Instructions

<!--
HOW TO USE THIS TEMPLATE:

This file provides additional context for a specific feature, module, or subsystem.
It supplements the project-level AGENTS.md with feature-specific details.

When initializing this file:
1. This file should be placed in the feature/module directory (e.g., src/authentication/, lib/payments/)
2. Read the existing code in this directory and subdirectories
3. Fill out sections that add value - skip sections that don't apply
4. Remove comment blocks after filling out each section
5. Keep it concise - only document what's unique to this feature
6. Assume the reader has already read the project-level AGENTS.md

The goal is to help AI assistants (and developers) quickly understand:
- What this feature/module does
- How it fits into the larger system
- Where to find key components
- Feature-specific patterns or gotchas
-->

## Feature Overview

<!--
Provide a 2-3 sentence description of this feature/module.
Include:
- What problem it solves or what capability it provides
- How it relates to other parts of the system
- High-level approach or architecture choice

Example:
Authentication module providing JWT-based user authentication. Handles login, logout, token refresh, and session management. Integrates with the user service for credential validation and the API gateway for request authentication.
-->

## Key Components

<!--
List the main files/classes/functions in this feature and their purposes.
Use a bulleted list with file paths or class names and brief descriptions.

Example:
- `auth_service.py` - Core authentication logic, token generation/validation
- `middleware.py` - Express middleware for protecting routes
- `token_store.py` - Redis-backed token storage and blacklisting
- `models/user.py` - User model with password hashing
-->

## Architecture

<!--
Describe how this feature is structured, in 2-4 bullet points.
Include:
- How data flows through the feature
- Key design decisions and why they were made
- Integration points with other features
- External dependencies (databases, APIs, services)

Example:
- Token-based authentication using JWT with RS256 signing
- Refresh tokens stored in Redis with 7-day expiration
- Access tokens are stateless and validated using public key
- Integrates with user service via gRPC for credential checks
-->

## Testing

<!--
Document testing approach specific to this feature.
Include:
- Location of test files for this feature
- How to run tests for just this feature
- Key test scenarios or edge cases
- Mock/fixture setup specific to this feature

Example:
- Tests in `tests/auth/` directory
- Run: `pytest tests/auth/ -v`
- Key scenarios: token expiration, refresh flow, invalid credentials, token blacklisting
- Use `auth_fixtures.py` for test users and tokens
-->

## Common Tasks

<!--
List common development tasks specific to this feature.
Use a bulleted or numbered list.

Example:
- Adding a new authentication method: Implement in `auth_service.py`, add validator, update tests
- Changing token expiration: Update constants in `config.py`, clear Redis cache
- Debugging auth failures: Check logs in `auth.log`, verify token signature, check Redis connection
-->

## Feature-Specific Patterns

<!--
Document patterns, conventions, or gotchas unique to this feature.
Use bulleted list with bold labels.

Example:
- **Token refresh race condition**: Always validate old token hasn't been used before issuing new one
- **Password hashing**: Use bcrypt with cost factor 12, never log passwords or hashes
- **Session cleanup**: Background job runs every hour to remove expired sessions from Redis
- **Auth headers**: All endpoints expect `Authorization: Bearer <token>`, case-sensitive
-->

## Integration Points

<!--
Document how this feature connects to other parts of the system.
Include:
- APIs or interfaces this feature provides
- APIs or interfaces this feature consumes
- Events this feature publishes or subscribes to
- Database tables or collections this feature owns

Example:
- **Provides**: `/api/auth/login`, `/api/auth/refresh`, `/api/auth/logout` endpoints
- **Consumes**: User service gRPC API for credential validation
- **Publishes**: `user.login` and `user.logout` events to message bus
- **Database**: `users`, `sessions`, `refresh_tokens` tables in PostgreSQL
-->

## Dependencies

<!--
List feature-specific dependencies (beyond project-wide dependencies).
Include why they're used and any important configuration.

Example:
- `PyJWT` (2.8.0+) - JWT token generation and validation
- `bcrypt` (4.0.0+) - Password hashing (cost factor configured in settings)
- `redis-py` (5.0.0+) - Token storage and session management
-->

______________________________________________________________________

_This file provides feature-specific guidance supplementing the project-level AGENTS.md._

## Additional Notes

<!-- Add any other feature-specific notes below this line -->
