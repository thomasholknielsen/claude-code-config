---
description: "Generate and maintain comprehensive API documentation by analyzing code and extracting endpoint information"
argument-hint: "[path] [--format=<type>] [--include-examples] [--update-schemas]"
category: "docs"
tools: ["Glob", "Read", "Grep", "Write", "mcp__context7__get-library-docs"]
complexity: "complex"
---

# Command: Api

## Purpose

Generates and maintains comprehensive API documentation by analyzing code and extracting endpoint information, schemas, and usage patterns.

## Usage

```bash
/docs:api $ARGUMENTS
```

**Arguments**:

- `$1` (path): Specific API files or directories to document (optional)
- `$2` (--format): Output format (openapi, markdown, html) (optional)
- `$3` (--include-examples): Generate usage examples and test cases (optional)
- `$4` (--update-schemas): Update existing API schemas and models (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/api/ --format=openapi"` - Document API with OpenAPI format
- `$ARGUMENTS = "--include-examples --update-schemas"` - Full documentation with examples
- `$ARGUMENTS = "controllers/ --format=markdown"` - Document controllers in markdown

## Process

1. **Parallel API Discovery**: Use Task() to comprehensively analyze API structure:

   ```python
   Task("scan-endpoints", "Identify all API endpoints, routes, and handlers"),
   Task("analyze-schemas", "Extract data models, request/response schemas"),
   Task("trace-authentication", "Map authentication and authorization patterns")
   ```

2. **Code Analysis**: Extract API information from source code based on $ARGUMENTS scope:
   - Parse route definitions and endpoint handlers
   - Extract parameter types, validation rules, and constraints
   - Identify request/response data structures
   - Analyze error handling and status codes
   - Map authentication and middleware requirements

3. **Schema Generation**: Create comprehensive API documentation:
   - Generate OpenAPI/Swagger specifications
   - Document request/response schemas with examples
   - Create parameter definitions and validation rules
   - Map error responses and status codes
   - Include authentication and authorization details

4. **Example Generation**: Create practical usage documentation:
   - Generate example requests for each endpoint
   - Create response examples with realistic data
   - Include code samples in multiple languages
   - Provide integration examples and workflows
   - Document common use cases and patterns

5. **Documentation Integration**: Organize and publish API docs:
   - Create structured documentation with navigation
   - Generate interactive API explorers
   - Integrate with existing project documentation
   - Set up automatic documentation updates
   - Validate documentation completeness and accuracy

## Agent Integration

- **Specialist Agent**: documenter - Can be spawned to handle comprehensive API documentation with current standards and Context7 MCP integration

## Parallelization Patterns

**Multi-Endpoint Analysis**: Simultaneously analyze different API endpoints to build complete documentation faster.

**Schema Processing**: Run parallel analysis of different data models and schemas for comprehensive API coverage.

## Examples

```bash
# Generate complete API documentation
/docs:api

# Document specific API modules
/docs:api $ARGUMENTS
# where $ARGUMENTS = "src/api/ --include-examples"

# Update OpenAPI schemas
/docs:api $ARGUMENTS
# where $ARGUMENTS = "--format=openapi --update-schemas"
