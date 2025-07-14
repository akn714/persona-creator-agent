**PEP 8 GUIDELINES**

1. **Indentation**: 4 spaces per indent level
2. **Line Length**: max 79 characters (72 for docstrings)
3. **Spacing**:
	* 1 space around operators (e.g., `a = 1`)
	* 1 space after commas (e.g., `a, b, c`)
4. **Naming Conventions**:
	* Variables: `lower_case_with_underscores`
	* Functions: `lower_case_with_underscores`
	* Classes: `CapWords`
5. **Comments**:
	* Use `#` for comments
	* Place comments on separate lines
6. **Docstrings**:
	* Use triple quotes `"""..."""` for docstrings
	* Place docstrings immediately after the definition

**EXAMPLE CODE**
```python
def greet(name: str) -> None:
    """Print a personalized greeting."""
    print(f"Hello, {name}!")

# Usage
greet("John")
```
**RESOURCES**

* PEP 8 Official Documentation: <https://peps.python.org/pep-0008/>  
