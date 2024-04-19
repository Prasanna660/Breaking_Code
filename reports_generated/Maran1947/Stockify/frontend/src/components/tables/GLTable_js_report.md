**1. Testing the Code**

**Static Analysis:**
- The code was statically analyzed using the ESLint linter with the recommended configuration. The analysis revealed no major issues with syntax, formatting, or coding style.

**Code Reviews:**
- A code review was conducted to assess the overall structure, design, and implementation of the code. Several minor issues were identified, including:
    - Unnecessary nesting in the `getGL` function.
    - Redundant code for handling the `type` parameter.
    - Lack of error handling in the `refreshGainerLosers` function.

**Static Code Analysis Tools:**
- The code was analyzed using Sonarqube to identify potential bugs, vulnerabilities, or other issues. No critical or major issues were found, but a few minor code smells were reported:
    - High cyclomatic complexity in the `getGL` function.
    - Lack of unit tests.

**Code Linting:**
- The code was linted with ESLint to check for adherence to coding standards and best practices. The linting process identified several minor issues, such as:
    - Inconsistent indentation.
    - Missing semi-colons in some places.
    - Use of deprecated functions.

**Code Complexity Analysis:**
- The cyclomatic complexity of the `getGL` function was identified as being high, indicating that the function may be difficult to understand and maintain.

**Dependency Analysis:**
- The code uses a number of external dependencies, including React, MUI, and axios. There were no issues identified with any of these dependencies.

**2. Correcting the Code**

**Bugs and Vulnerabilities:**
- No critical or major bugs or vulnerabilities were identified in the code.

**Improvements:**

- **Reduced Cyclomatic Complexity:** The `getGL` function was refactored to reduce its cyclomatic complexity by breaking it down into smaller, more manageable functions.
- **Improved Error Handling:** The `refreshGainerLosers` function was updated to include error handling to prevent the application from crashing in case of an error.
- **Simplified Logic:** The logic for handling the `type` parameter was simplified to eliminate redundancy.
- **Unit Tests:** Unit tests were added to cover the core functionality of the code.
- **Dependency Cleanup:** The `react-onclickoutside` dependency was removed as it was no longer being used.

**3. Detailed Review**

**Errors Found:**
- High cyclomatic complexity in the `getGL` function.
- Lack of error handling in the `refreshGainerLosers` function.
- Redundant code for handling the `type` parameter.
- Missing semi-colons in some places.
- Use of deprecated functions.

**Fixes and Improvements:**
- The cyclomatic complexity of the `getGL` function was reduced by breaking it down into smaller functions.
- Error handling was added to the `refreshGainerLosers` function to prevent crashing.
- The logic for handling the `type` parameter was simplified to eliminate redundancy.
- Missing semi-colons were added.
- Deprecated functions were replaced with their modern equivalents.
- Unit tests were added to cover the core functionality of the code.
- The `react-onclickoutside` dependency was removed as it was no longer being used.

**Reasoning for Changes:**
- Reducing the cyclomatic complexity of the `getGL` function makes the code easier to understand and maintain.
- Adding error handling to the `refreshGainerLosers` function ensures that the application does not crash in case of an error.
- Simplifying the logic for handling the `type` parameter eliminates redundancy and makes the code more concise.
- Adding missing semi-colons improves the reliability of the code.
- Replacing deprecated functions with their modern equivalents ensures that