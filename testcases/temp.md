## New Test Cases

### Global Header and Navigation
#### TC-GlobalHeader-001
- **Test Title:** Verify Global Header Elements
- **Pre-conditions:**
  - User is logged into the OrangeHRM application.
- **Test Steps:**
  1. Navigate to any page within the application.
  2. Verify the presence of the OrangeHRM logo on the top left.
  3. Observe the current page title.
  4. Check for the presence of the "Upgrade" button, user profile section, and help icon.
- **Expected Result:** 
  - All expected elements are present and functional.

#### TC-LeftNavigationPanel-002
- **Test Title:** Verify Left Navigation Panel
- **Pre-conditions:**
  - User is on the OrangeHRM dashboard.
- **Test Steps:**
  1. Observe the highlighted module and vertical orange bar in the navigation.
  2. Test the search functionality using the input field.
  3. Click each navigation menu item and verify the page transitions correctly.
- **Expected Result:** 
  - Navigation is smooth, search returns correct results, and modules transition correctly.

#### TC-Footer-003
- **Test Title:** Verify Footer Information
- **Pre-conditions:**
  - User is on any page within the application.
- **Test Steps:**
  1. Scroll to the bottom of the page.
  2. Verify the copyright information including year and company name.
- **Expected Result:** 
  - The footer is correctly displayed with accurate information.

### Dashboard
#### TC-DashboardWidgets-004
- **Test Title:** Verify Dashboard Widgets
- **Pre-conditions:**
  - User is on the dashboard.
- **Test Steps:**
  1. Check the presence of all widgets including Time at Work, My Actions, Quick Launch, etc.
  2. Verify functionality of each widget by interacting with controls (e.g., punch in/out, quick launch actions).
- **Expected Result:** 
  - Widgets are displayed and functional as expected.

### Admin/User Management
#### TC-UserManagement-005
- **Test Title:** Verify User Management Search and Actions
- **Pre-conditions:**
  - User has access to admin functionalities.
- **Test Steps:**
  1. Navigate to the 'Admin / User Management' section.
  2. Use filters to search users by username, role, and status.
  3. Add a new user and verify record creation.
  4. Edit and delete user functionalities.
- **Expected Result:** 
  - Search filters function correctly; users can be added, modified, and deleted successfully.

### Admin/Edit User
#### TC-EditUser-006
- **Test Title:** Verify Edit User Functionality
- **Pre-conditions:**
  - User is on the Edit User form in Admin.
- **Test Steps:**
  1. Attempt to edit user details including role, username, and status.
  2. Check/Uncheck 'Change Password?' option and verify password fields are revealed.
  3. Cancel and Save changes to validate actions.
- **Expected Result:** 
  - User can be edited as expected; changes to fields work, and optional password change fields display correctly.