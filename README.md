# AI Code Reviews

This project has been initialized with Qodo for AI-powered code reviews.

## Getting Started

### Qodo Configuration

This project includes a comprehensive Qodo setup with:

- **Main Configuration**: `.qodo.yml` - Contains all project settings and review preferences
- **Custom Rules**: `.qodo/rules/` - Security and quality rules for automated code analysis
- **Templates**: `.qodo/templates/` - Customizable report templates
- **Reports**: `.qodo/reports/` - Generated review reports (gitignored)

### Features Enabled

✅ **Automatic Code Review** - Triggered on commits and pull requests  
✅ **Security Analysis** - Detects vulnerabilities and security issues  
✅ **Code Quality Checks** - Identifies code smells and maintainability issues  
✅ **Performance Analysis** - Suggests performance improvements  
✅ **Best Practices** - Enforces coding standards and conventions  

### Supported Languages

- Python (`.py`)
- JavaScript/TypeScript (`.js`, `.ts`)
- Java (`.java`)
- Go (`.go`)
- Rust (`.rs`)
- C/C++ (`.c`, `.cpp`)
- C# (`.cs`)

### Usage

1. **Run a code review**:
   ```bash
   qodo review
   ```

2. **Review specific files**:
   ```bash
   qodo review src/main.py
   ```

3. **Generate a report**:
   ```bash
   qodo report --format markdown
   ```

4. **Check configuration**:
   ```bash
   qodo config validate
   ```

### Configuration

Edit `.qodo.yml` to customize:

- **Review scope** - Which files to include/exclude
- **AI model settings** - Temperature, tokens, provider
- **Focus areas** - Security, performance, quality priorities
- **Output format** - Markdown, JSON, HTML options
- **Integration settings** - Git, GitHub, GitLab connections

### Custom Rules

Add custom review rules in `.qodo/rules/`:

- `security.yml` - Security-focused rules
- `quality.yml` - Code quality rules
- Create additional rule files as needed

### Reports

Review reports are generated in `.qodo/reports/` and include:

- Issue summaries by severity
- Code quality metrics
- Security vulnerability assessments
- Performance recommendations
- Best practice suggestions

## Next Steps

1. Add your source code to the project
2. Run your first code review with `qodo review`
3. Customize rules and configuration as needed
4. Set up CI/CD integration for automated reviews

---

*Powered by Qodo AI*