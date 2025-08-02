# Contributing to YouTube Analytics Dashboard

Thank you for your interest in contributing to the YouTube Analytics Dashboard! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- **Search existing issues** first to avoid duplicates
- **Use issue templates** when available
- **Provide detailed information** including:
  - Steps to reproduce the problem
  - Expected vs actual behavior
  - System information (OS, Python version)
  - Error messages or screenshots

### Suggesting Features
- **Check existing feature requests** to avoid duplicates
- **Describe the use case** and why it would be valuable
- **Provide mockups or examples** if applicable
- **Consider implementation complexity** and maintenance burden

### Code Contributions

#### Getting Started
1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/saawezali/youtube-trends-analyser.git
   cd youtube-trends-analyser
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Development Workflow
1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes**
3. **Test your changes**:
   ```bash
   python test_api.py YOUR_API_KEY
   streamlit run app.py
   ```
4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**

## 📝 Code Style Guidelines

### Python Code Style
- **Follow PEP 8** for Python code formatting
- **Use meaningful variable names** and function names
- **Add docstrings** to functions and classes
- **Keep functions focused** and reasonably sized
- **Use type hints** where appropriate

### Streamlit Best Practices
- **Use caching** (`@st.cache_data`) for expensive operations
- **Handle errors gracefully** with try-catch blocks
- **Provide user feedback** with spinners and status messages
- **Make UI responsive** and mobile-friendly

### Documentation
- **Update README.md** if adding new features
- **Add inline comments** for complex logic
- **Include examples** in docstrings
- **Update requirements.txt** if adding dependencies

## 🧪 Testing Guidelines

### Before Submitting
- **Test with real API key** to ensure functionality works
- **Test error handling** with invalid inputs
- **Check responsive design** on different screen sizes
- **Verify all visualizations** render correctly
- **Test export functionality** (CSV, JSON downloads)

### API Testing
- **Use test_api.py** to verify API connectivity
- **Test with different regions** and categories
- **Verify quota usage** is reasonable
- **Handle API rate limits** gracefully

## 🎯 Areas for Contribution

### High Priority
- **Performance optimizations** for large datasets
- **Additional visualizations** and chart types
- **Mobile responsiveness** improvements
- **Error handling** enhancements
- **Documentation** updates and examples

### Medium Priority
- **New data sources** (Instagram, TikTok integration)
- **Advanced analytics** features
- **Custom dashboard layouts**
- **Data export formats** (Excel, PDF)
- **Internationalization** support

### Low Priority
- **Theme customization** options
- **Advanced filtering** capabilities
- **Automated testing** suite
- **Performance monitoring**
- **Analytics tracking**

## 🔧 Development Setup

### Environment Variables
Create a `.streamlit/secrets.toml` file for development:
```toml
YOUTUBE_API_KEY = "your_api_key_here"
```

### Project Structure
```
youtube-trends-analyser/
├── app.py                 # Main application
├── test_api.py           # API testing utility
├── requirements.txt      # Dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
└── .streamlit/          # Streamlit configuration
    └── secrets.toml     # API keys (not in git)
```

## 📋 Pull Request Guidelines

### Before Submitting
- **Ensure your code works** with the latest main branch
- **Test thoroughly** with real data
- **Update documentation** if needed
- **Follow the code style** guidelines
- **Write clear commit messages**

### PR Description Template
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tested with real API key
- [ ] Verified all visualizations work
- [ ] Checked responsive design
- [ ] Tested error handling

## Screenshots
Include screenshots if UI changes were made.

## Additional Notes
Any additional information or context.
```

## 🐛 Bug Report Template

When reporting bugs, please include:

```markdown
## Bug Description
Clear description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Windows 10, macOS 12.0]
- Python Version: [e.g., 3.9.0]
- Browser: [e.g., Chrome 96.0]
- Streamlit Version: [e.g., 1.28.0]

## Additional Context
Screenshots, error messages, or other relevant information.
```

## 💡 Feature Request Template

```markdown
## Feature Description
Clear description of the proposed feature.

## Use Case
Describe the problem this feature would solve.

## Proposed Solution
How you envision this feature working.

## Alternatives Considered
Other approaches you've considered.

## Additional Context
Mockups, examples, or other relevant information.
```

## 🎉 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Documentation**: Check README.md and code comments

---

Thank you for contributing to the YouTube Analytics Dashboard! Your contributions help make this tool better for everyone.
