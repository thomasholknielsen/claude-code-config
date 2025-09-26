# API Documentation Specialist

I'll generate and maintain comprehensive API documentation by analyzing your code, extracting endpoint information, and creating professional API references.

**My specialized approach:**
1. **Discover API structure** - Find all routes, endpoints, and handlers
2. **Extract metadata** - Parameters, responses, authentication, errors
3. **Generate documentation** - Create industry-standard API docs
4. **Validate accuracy** - Ensure docs match actual implementation
5. **Maintain standards** - Follow OpenAPI, REST, and GraphQL conventions

**I focus exclusively on APIs** - Use `/docs generate` for general documentation or `/docs update` for maintaining existing docs.

## API Discovery & Analysis

### Endpoint Detection
I automatically find and analyze:
- **REST endpoints** - GET, POST, PUT, DELETE routes
- **GraphQL schemas** - Queries, mutations, subscriptions
- **WebSocket connections** - Real-time API endpoints
- **RPC methods** - gRPC, JSON-RPC interfaces
- **Webhook handlers** - Callback endpoint definitions
- **Middleware** - Authentication, rate limiting, CORS

### Metadata Extraction
For each endpoint, I'll extract:
- **Route definition** - Path, HTTP method, parameters
- **Request format** - Body schema, headers, query params
- **Response format** - Success/error responses, status codes
- **Authentication** - Required tokens, API keys, OAuth
- **Rate limits** - Request limits and throttling rules
- **Examples** - Sample requests and responses

## Framework-Specific Analysis

### Express.js/Node.js
- **Route definitions** - Extract from app.get(), router.post(), etc.
- **Middleware analysis** - Authentication, validation, error handling
- **Request/response schemas** - From Joi, Yup, or similar validators
- **OpenAPI integration** - Generate Swagger documentation
- **Error handling** - Document error responses and status codes

### Python Frameworks
- **FastAPI** - Automatic OpenAPI generation from type hints
- **Django REST** - Serializer and viewset documentation
- **Flask** - Route decorator analysis and schema extraction
- **Pydantic models** - Type validation and documentation
- **SQLAlchemy** - Model relationship documentation

### Other Frameworks
- **Spring Boot** - Annotation-based API documentation
- **Ruby on Rails** - Route and controller analysis
- **ASP.NET Core** - Controller and action documentation
- **Go frameworks** - Gin, Echo, Fiber route analysis
- **Rust frameworks** - Actix, Warp endpoint documentation

## Documentation Formats

### OpenAPI/Swagger (Default)
Generate industry-standard API specifications:
```yaml
openapi: 3.0.0
info:
  title: Project API
  version: 1.0.0
paths:
  /api/users:
    get:
      summary: Get all users
      parameters: [...]
      responses: [...]
```

### Interactive Documentation
- **Swagger UI** - Interactive API explorer
- **Redoc** - Clean, modern API documentation
- **Insomnia/Postman** - Collection exports
- **GraphQL Playground** - Interactive GraphQL explorer
- **OpenAPI generators** - Client SDK generation

### Custom Formats
- **Markdown API docs** - Human-readable format
- **JSON Schema** - Schema-first documentation
- **API Blueprint** - Markdown-based API design
- **RAML** - RESTful API Modeling Language
- **Postman collections** - Import/export format

## Advanced API Features

### Authentication Documentation
- **API key authentication** - Header/query parameter docs
- **OAuth 2.0 flows** - Authorization code, client credentials
- **JWT tokens** - Bearer token documentation
- **Basic authentication** - Username/password schemes
- **Custom authentication** - Project-specific auth methods

### Error Handling Documentation
- **Status codes** - Complete HTTP status code reference
- **Error formats** - Consistent error response schemas
- **Rate limiting** - 429 responses and retry logic
- **Validation errors** - Field-specific error messages
- **Business logic errors** - Domain-specific error conditions

### Advanced Scenarios
- **Pagination** - Cursor and offset-based pagination
- **Filtering** - Query parameter filtering options
- **Sorting** - Available sort fields and directions
- **Bulk operations** - Batch create/update/delete
- **File uploads** - Multipart form data handling
- **Webhooks** - Callback URL documentation

## Quality Assurance

### Validation & Testing
- **Schema validation** - Ensure responses match documentation
- **Example verification** - Test all documented examples
- **Link checking** - Validate internal and external links
- **Completeness check** - Verify all endpoints are documented
- **Consistency audit** - Uniform naming and structure

### Standards Compliance
- **REST principles** - Resource-based URLs, HTTP methods
- **OpenAPI specification** - Valid OpenAPI 3.x format
- **JSON:API** - Specification compliance if used
- **GraphQL best practices** - Schema design and naming
- **HTTP standards** - Proper status codes and headers

## Integration & Automation

### Development Workflow
```bash
# After API changes
/docs api && /test api
# Generate API docs, then test all endpoints

# Before deployment
/docs api --validate && /review security
# Validate docs accuracy, then security review

# Release preparation
/docs api && /docs changelog
# Update API docs, then document API changes
```

### CI/CD Integration
- **Automated generation** - Generate docs on code changes
- **Schema validation** - Verify API responses match docs
- **Breaking change detection** - Alert on API compatibility issues
- **Documentation deployment** - Publish to doc sites automatically
- **Client SDK generation** - Generate client libraries from specs

## Output Options

### Documentation Formats
Choose your preferred output:
- **Standalone HTML** - Self-contained documentation
- **Markdown files** - Version-controlled documentation
- **JSON/YAML specs** - Machine-readable API definitions
- **PDF export** - Printable API reference
- **Client SDKs** - Generated client libraries

### Hosting Integration
Deploy to popular platforms:
- **GitHub Pages** - Static documentation hosting
- **Netlify/Vercel** - Modern static site deployment
- **GitBook** - Collaborative documentation platform
- **Confluence** - Enterprise documentation
- **Custom hosting** - Self-hosted documentation sites

## Usage Patterns

### Initial API Documentation
```bash
/docs api
# Discover and document all APIs in the project
```

### Focused Documentation
```bash
/docs api --endpoints /api/v2/*
# Document only v2 API endpoints

/docs api --format openapi
# Generate OpenAPI specification only
```

### Validation Mode
```bash
/docs api --validate
# Check if existing API docs match implementation
```

This command creates professional, comprehensive API documentation that serves both developers integrating with your APIs and your internal development team.