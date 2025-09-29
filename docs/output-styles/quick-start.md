# Quick Start Guide

Get professional output styles working in 2 minutes.

## Step 1: Install Styles

Copy the style files to your Claude output styles directory:

```bash
# Copy all 12 professional styles
cp output-styles/*.md ~/.claude/output-styles/

# Or copy individual styles as needed
cp output-styles/product-manager.md ~/.claude/output-styles/
cp output-styles/data-scientist.md ~/.claude/output-styles/
```

## Step 2: Activate a Style

Use Claude's output style commands:

```bash
# List available styles
/output-style

# Activate a professional style
/output-style product-manager

# Return to default
/output-style default
```

## Step 3: Start Using Professional Communication

**Example: Product Manager Style**

```text
You: "How should we prioritize our mobile app features?"

Claude (Product Manager style):
**Problem Statement**: Feature backlog contains 15+ items without clear prioritization framework.

**Recommended Framework**: RICE scoring (Reach × Impact × Confidence ÷ Effort)

**Top 3 Priorities**:
1. User onboarding flow (RICE: 320)
2. Push notification system (RICE: 240)
3. Offline mode capability (RICE: 180)

**Implementation Strategy**:
- Sprint 1-2: Onboarding flow with A/B testing
- Sprint 3-4: Push notifications with segmentation
- Sprint 5-6: Offline mode MVP validation

**Confidence Level**: 8/10 (based on user research data)
```

## Next Steps

- **[Browse All Styles →](style-catalog.md)** - Explore all 12 professional styles
- **[See More Examples →](examples.md)** - Real-world usage scenarios
- **[Advanced Features →](advanced-usage.md)** - Style switching and customization

## Need Help

- **Style not working?** Check [Troubleshooting →](troubleshooting.md)
- **Want to customize?** See [Advanced Usage →](advanced-usage.md)
- **Questions?** View [Comprehensive Guide →](comprehensive-guide.md)

---

**🎯 Pro Tip**: Start with styles matching your current role, then experiment with others to gain new perspectives on your projects.
