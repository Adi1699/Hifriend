### Generated Test Cases

**Test Case: Add New Job Title**
- **Precondition:** User must have admin access.
- **Steps:**
  1. Navigate to [Login Page](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
  2. Login using username `Admin` and password `admin123`.
  3. Click on `Admin` in the left navigation panel.
  4. Click on `Job` from the dropdown options.
  5. Click on `Add New` button.
  6. Fill out the form fields: `Job Title`, `Job Description`, `Job Specification`.
  7. Click `Save`.
- **Expected Outcome:** Job title is saved. A success message appears.

**Test Case: Edit User with User Type Field**
- **Precondition:** User must be logged in as admin.
- **Steps:**
  1. Navigate to [Login Page](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
  2. Login using username `Admin` and password `admin123`.
  3. Navigate to `Admin / User Management`.
  4. Locate user and click `Edit`.
  5. Verify existence of `User Type` field.
  6. Select appropriate user type.
  7. Click `Save`.
- **Expected Outcome:** User details are updated with the selected user type.