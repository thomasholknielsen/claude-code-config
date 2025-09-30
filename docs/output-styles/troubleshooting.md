# Troubleshooting

Common issues and solutions for professional output styles.

## 🚫 Style Not Working

### Problem: Style commands not recognized

**Symptoms:**

- `/output-style` command not found
- Style not activating after selection

**Solutions:**

1. **Check file location**

   ```bash
   # Verify files are in correct directory
   ls ~/.claude/output-styles/

   # Should show your .md style files
   ```

2. **Verify file format**

   ```bash
   # Check YAML front matter is correct
   head -5 ~/.claude/output-styles/product-manager.md
   ```

   Should show:

   ```yaml
   ---
   name: Product Manager
   description: Strategic product thinking...
   ---
   ```

3. **Restart Claude Code session**

   ```bash
   # Exit and restart Claude Code to reload styles
   exit
   # Start new session
   ```

### Problem: Style partially working

**Symptoms:**

- Style activates but doesn't follow instructions consistently
- Missing professional frameworks or formatting

**Solutions:**

1. **Check style file size**

   ```bash
   wc -w ~/.claude/output-styles/product-manager.md
   # Should be under 500 words for optimal performance
   ```

2. **Simplify style instructions**
   - Remove conflicting directives
   - Focus on positive instructions ("Use..." vs "Don't use...")
   - Test with shorter, more specific prompts

3. **Check for conflicts**
   - Ensure no contradictory instructions in style file
   - Verify style doesn't conflict with Claude's base training

## ⚠️ Inconsistent Behavior

### Problem: Style works sometimes but not others

**Symptoms:**

- Professional formatting appears inconsistently
- Framework application varies between responses
- Confidence scoring missing occasionally

**Solutions:**

1. **Use explicit prompts**

   ```text
   Bad: "Analyze this market"
   Good: "Provide strategic consultant analysis of SaaS market opportunity including framework application and confidence score"
   ```

2. **Reinforce style mid-conversation**

   ```bash
   # Reactivate style if behavior drifts
   /output-style strategic-consultant
   "Continue analysis using consultant frameworks"
   ```

3. **Break complex requests into steps**

   ```text
   Step 1: Market analysis with frameworks
   Step 2: Risk assessment with confidence scoring
   Step 3: Strategic recommendations with implementation timeline
   ```

## 🔄 Style Switching Issues

### Problem: Style switching not working properly

**Symptoms:**

- Previous style behavior persists
- Mixed communication patterns
- Confusion between style characteristics

**Solutions:**

1. **Clear style transition**

   ```bash
   /output-style default  # Reset to neutral
   /output-style data-scientist  # Activate new style
   ```

2. **Explicit context break**

   ```text
   "Now switching to data scientist perspective for statistical analysis..."
   ```

3. **Use style-specific language**

   ```text
   # For data scientist style
   "Please provide hypothesis-driven analysis with statistical significance"

   # For product manager style
   "Please use RICE prioritization framework with user impact focus"
   ```

## 📝 Customization Problems

### Problem: Custom styles not working as expected

**Symptoms:**

- Modified styles don't apply changes
- Custom instructions ignored
- Organization-specific terminology not used

**Solutions:**

1. **Validate YAML syntax**

   ```yaml
   ---
   name: "Custom Style Name"  # Use quotes for names with spaces
   description: "Clear description"
   ---
   ```

2. **Test incrementally**
   - Start with small modifications to working style
   - Test each change before adding more customization
   - Keep base structure intact

3. **Check instruction clarity**

   ```markdown
   # Good: Specific and actionable
   Always include ROI calculations using company's 12% discount rate.

   # Bad: Vague and conflicting
   Be better at financial analysis but don't be too technical.
   ```

## 🚀 Performance Issues

### Problem: Styles causing slow responses

**Symptoms:**

- Longer response times with styles active
- Token limit warnings
- Incomplete responses

**Solutions:**

1. **Optimize style length**

   ```bash
   # Check style word count
   wc -w ~/.claude/output-styles/style-name.md
   # Target: under 300 words for best performance
   ```

2. **Simplify complex styles**
   - Remove redundant instructions
   - Focus on essential behavioral changes
   - Use concise professional language

3. **Split complex requests**

   ```text
   # Instead of one complex request:
   "Analyze market, create strategy, plan implementation, assess risks"

   # Use sequence of focused requests:
   1. "Market analysis with strategic frameworks"
   2. "Strategy recommendations based on analysis"
   3. "Implementation timeline with risk assessment"
   ```

## 🔍 Quality Issues

### Problem: Professional output quality inconsistent

**Symptoms:**

- Missing industry terminology
- Inconsistent framework application
- Unprofessional tone or structure

**Solutions:**

1. **Enhance style specificity**

   ```markdown
   # Add specific examples
   Use consulting terminology: "value proposition", "competitive moats", "market positioning"

   # Include format requirements
   Always structure as: Executive Summary → Analysis → Recommendations → Next Steps
   ```

2. **Add quality checkpoints**

   ```text
   "Please review response for professional terminology and framework compliance"
   ```

3. **Use style validation prompts**

   ```text
   "Rate this response's adherence to strategic consultant communication style (1-10)"
   ```

## 📞 Getting More Help

### Additional Resources

- **[Quick Start →](quick-start.md)** - Basic setup and activation
- **[Style Catalog →](style-catalog.md)** - Browse all available styles
- **[Advanced Usage →](advanced-usage.md)** - Style switching and customization
- **[Comprehensive Guide →](comprehensive-guide.md)** - Complete reference

### Community Support

- **GitHub Issues**: Report bugs or request features
- **Style Sharing**: Community library of custom professional styles
- **Best Practices**: Learn from other professional users

### Professional Services

For organization-wide deployments:

- Custom style development for your industry
- Team training and best practices
- Integration with existing workflows

---

**💡 Quick Fix Checklist:**

1. ✅ Files in `~/.claude/output-styles/` directory
2. ✅ Valid YAML front matter format
3. ✅ Style under 500 words
4. ✅ Claude Code session restarted
5. ✅ Clear, specific prompts used
