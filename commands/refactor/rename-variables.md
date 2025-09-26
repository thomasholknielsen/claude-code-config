# Rename Variables

I'll improve code clarity by renaming variables, functions, and other identifiers to be more descriptive and follow naming conventions.

Arguments: `$ARGUMENTS` - files, identifiers, or scope to rename

## Naming Improvements

**Variable clarity:**
- Replace generic names (data, item, temp) with descriptive ones
- Use consistent naming patterns across codebase
- Follow language/framework conventions
- Make intent clear from the name alone

**Function naming:**
- Use verb-noun patterns for functions (getUserData, calculateTotal)
- Make return type obvious from name
- Avoid abbreviations unless widely understood
- Use consistent terminology across related functions

## Smart Renaming Process

**Context-aware analysis:**
- Understand variable usage patterns
- Consider scope and lifetime
- Analyze related code that might be affected
- Check for naming conflicts before renaming

**Safe renaming execution:**
- Use language server capabilities for accurate refactoring
- Update all references including imports/exports
- Handle string references where appropriate
- Preserve external API compatibility

## Validation

**Reference integrity:**
- Ensure all usages are updated correctly
- Check that imports/exports still work
- Verify no broken references remain
- Test that functionality remains identical

**Naming consistency:**
- Follow established project conventions
- Maintain consistent patterns across similar code
- Use domain-appropriate terminology
- Ensure names accurately reflect current purpose

Fast, safe variable renaming with comprehensive reference updating.