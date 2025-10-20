# MCP Error Handling Guide

**Quick Summary**: When MCPs fail, show users a clear message and continue if the MCP is optional.

## The Problem

MCPs (Model Context Protocol tools) can fail for various reasons:

- Not installed (`/system:setup-mcp` not run)
- Network issue (timeout, no response)
- Configuration error
- Server crash

Without error handling, agents crash silently with unclear error messages. Users get frustrated.

## The Solution

**Two principles**:

1. **Always wrap MCP calls in try-catch** - Never let an MCP failure crash your agent
2. **Clear messages** - Tell users exactly what failed and what to do

## Pattern by MCP Type

### For Required MCPs

Use when the agent **cannot work** without this MCP (e.g., terraform analyst without terraform MCP).

```python
try:
    result = await mcp_tool.call(input)
    return result
except Exception as e:
    return f"❌ {MCP_NAME} is not available ({e}). Please run /system:setup-mcp to configure it."
```

**User sees**: Clear error with setup guidance. Analysis stops (as it should, because the tool is required).

### For Optional MCPs

Use when the agent works **better with** this MCP but can complete without it (e.g., fetch for external docs).

```python
try:
    result = await mcp_tool.call(input)
    return result + " (with external docs)"
except Exception as e:
    return f"⚠️ {MCP_NAME} unavailable ({e}). Proceeding with local analysis only."
```

**User sees**: Warning message. Analysis completes with partial results (as intended).

## Declaring MCP Dependencies

In your agent's frontmatter, document which MCPs you use:

```yaml
# MCP Dependencies

## Required MCPs:
- **fetch**: External documentation retrieval (required for analysis)

## Optional MCPs:
- **markitdown**: Document conversion (improves accuracy but agent works without)
```

## Error Message Formats

**Required MCP failed**:

```text
❌ Fetch MCP failed: Connection timeout
💡 Please run /system:setup-mcp to verify setup
```

**Optional MCP failed**:

```text
⚠️ Fetch MCP unavailable (timeout). Proceeding without external docs.
```

## Testing Your Error Handling

1. **Disable an MCP**: Stop the MCP server or rename it temporarily
2. **Run your agent**: Trigger a code path that uses the MCP
3. **Verify**: You see the error message (not a crash)
4. **For optional MCPs**: Agent completes with reduced functionality
5. **For required MCPs**: Agent stops with clear guidance

## Common MCP Failures

| Symptom | Likely Cause | Solution |
|---------|------|----------|
| `Connection refused` | MCP not running | Run `/system:setup-mcp` |
| `timeout` | MCP slow or unresponsive | Retry or check MCP logs |
| `Invalid API key` | Context7 setup incomplete | Get API key from context7.com |
| `Docker image not found` | terraform/markitdown not installed | Run `/system:setup-mcp` |

## When NOT to Catch MCP Errors

**Don't catch if you need to fail fast**:

- Authentication critical failure (let it propagate)
- System initialization failure (don't continue)
- Required MCP that agent explicitly needs

Let these fail loudly so the user knows something is wrong.

## Real Examples

### Example 1: Optional Fetch MCP

```python
async def analyze_with_external_docs(target):
    local_analysis = await analyze_locally(target)

    try:
        external_docs = await fetch_mcp.fetch(docs_url)
        return f"{local_analysis}\n\nWith external reference: {external_docs}"
    except Exception as e:
        return f"{local_analysis}\n\n⚠️ External docs unavailable ({e}). Local analysis above."
```

### Example 2: Required Terraform MCP

```python
async def analyze_terraform_config(file_path):
    try:
        modules = await terraform_mcp.search_modules("vpc")
        return analyze_with_modules(modules)
    except Exception as e:
        return f"❌ Terraform MCP failed ({e}). Run /system:setup-mcp to fix it."
```

## Summary

- Wrap MCP calls → try-catch
- Clear messages → tell user what failed
- Decide: Required or optional?
- Required → stop with guidance
- Optional → continue with note
- Test → disable MCP and verify error handling works

That's it! Simple and effective.
