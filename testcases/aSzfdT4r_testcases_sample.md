# Testcases for aSzfdT4r

Total Testcases: **10**

## TC_KAN6_FEAT1_NAV_001
**Description:** TC_KAN6_FEAT1_NAV_001: Verify successful navigation to the new Job Section under Admin module.

**Priority:** High

**Expected Result:** The system navigates to the Admin / User Management page, and the 'Job' sub-section is visible and accessible under Admin.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Click on 'Admin' in the left navigation panel.
- Verify the page title changes to 'Admin / User Management'.
- Locate and verify the existence of the 'Job' navigation link/section under Admin.

---

## TC_KAN6_FEAT1_ADD_002
**Description:** TC_KAN6_FEAT1_ADD_002: Verify that clicking 'Add New Button' in Job Titles opens the creation form.

**Priority:** High

**Expected Result:** A form opens allowing the administrator to input Job Title, Job Description, and Job Specification details.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> Job.
- Click the 'Add New Button'.
- Verify that the form fields 'Job Title', 'Job Description', and 'Job Specification' are displayed.

---

## TC_KAN6_FEAT1_ADD_003
**Description:** TC_KAN6_FEAT1_ADD_003: Verify successful creation of a new Job Title with all required fields filled.

**Priority:** Critical

**Expected Result:** The new Job Title 'Senior QA Engineer' is successfully saved, and a success message is displayed. The job title appears in the Job Titles list.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> Job.
- Click the 'Add New Button'.
- Enter 'Senior QA Engineer' into the 'Job Title' input field.
- Enter 'Responsible for all aspects of QA lifecycle.' into the 'Job Description' input field.
- Enter 'Experience: 5+ years in Selenium WebDriver.' into the 'Job Specification' input field.
- Click the 'Save' button.
- Verify success message stating 'Job title created successfully' or similar.
- Navigate back to the Job Titles list and verify 'Senior QA Engineer' is present.

---

## TC_KAN6_FEAT1_VALIDATION_004
**Description:** TC_KAN6_FEAT1_VALIDATION_004: Verify validation error when attempting to save a new job title with the Job Title field empty.

**Priority:** High

**Expected Result:** An error message indicating required fields are missing is displayed, and the record is not saved.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> Job.
- Click the 'Add New Button'.
- Leave 'Job Title' input field empty.
- Enter dummy text 'Test Desc' into the 'Job Description' input field.
- Enter dummy text 'Test Spec' into the 'Job Specification' input field.
- Click the 'Save' button.
- Verify an error message is displayed indicating that 'Job Title' is required.

---

## TC_KAN6_FEAT1_ACTION_005
**Description:** TC_KAN6_FEAT1_ACTION_005: Verify 'Cancel' button discards changes and closes the form.

**Priority:** Medium

**Expected Result:** The form is closed, all entered data ('QA Tester Draft') is discarded, and the user remains on the Job Titles list.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> Job.
- Click the 'Add New Button'.
- Enter 'QA Tester Draft' into the 'Job Title' input field.
- Click the 'Cancel' button.
- Verify the form is closed and the user is on the Job Titles list.
- Verify 'QA Tester Draft' does not appear in the Job Titles list.

---

## TC_KAN6_FEAT1_EDIT_006
**Description:** TC_KAN6_FEAT1_EDIT_006: Verify ability to edit an existing Job Title and save changes.

**Priority:** High

**Expected Result:** The existing Job Title is updated successfully, and a confirmation message is displayed on the Job Titles list.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> Job.
- In the Job Titles list, click the 'Edit' icon next to an existing job title (e.g., if one exists).
- Modify the 'Job Title' field to 'Updated Job Title Example'.
- Click the 'Save' button.
- Verify success message is displayed.
- Verify the Job Titles list now shows 'Updated Job Title Example' instead of the old name.

---

## TC_KAN6_FEAT1_DELETE_007
**Description:** TC_KAN6_FEAT1_DELETE_007: Verify ability to delete an existing Job Title after confirmation.

**Priority:** High

**Expected Result:** The selected Job Title is removed from the list after confirmation, and the total record count decreases.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> Job.
- If no temporary job exists, use 'Add New Button' to create a test job title 'Temp Job for Deletion' and save.
- In the Job Titles list, click the 'Delete' icon next to the 'Temp Job for Deletion' record.
- Verify the confirmation prompt appears.
- Click 'Confirm/Yes' on the confirmation prompt.
- Verify that 'Temp Job for Deletion' is no longer visible in the Job Titles list.

---

## TC_KAN6_FEAT2_FIELD_008
**Description:** TC_KAN6_FEAT2_FIELD_008: Verify the mandatory presence of the 'User Type' field in the Edit User section.

**Priority:** Critical

**Expected Result:** The 'User Type' field is present, mandatory (indicated by * or equivalent), and defaults to a pre-selected option or requires selection.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin / User Management.
- Click the 'Edit' icon for any existing user record.
- Verify that the page title changes to 'Admin' (as per documentation flow).
- Locate the 'User Type' field on the form.
- Verify that the 'User Type' field is marked as required (e.g., contains a '*').

---

## TC_KAN6_FEAT2_VALIDATION_009
**Description:** TC_KAN6_FEAT2_VALIDATION_009: Verify mandatory validation when attempting to save user edits without selecting the 'User Type' field.

**Priority:** Critical

**Expected Result:** An error message appears requiring selection of 'User Type', and the user details are not saved.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> User Management.
- Click the 'Edit' icon for an existing user.
- Ensure the 'User Type' dropdown remains unselected (or select an option other than the target modification if one defaults).
- Modify another required field, such as 'Employee Name', to 'Test Name Change'.
- Click the 'Save' button.
- Verify an error message is displayed stating 'User Type is required'.
- Verify that 'Test Name Change' was not saved (e.g., by re-editing or viewing the list).

---

## TC_KAN6_FEAT2_SUCCESS_010
**Description:** TC_KAN6_FEAT2_SUCCESS_010: Verify successful update of user details including setting a specific 'User Type'.

**Priority:** High

**Expected Result:** The user details (including the selected User Type) are saved correctly, and the user is returned to the System Users table with a success message.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> User Management.
- Click the 'Edit' icon for an existing user (e.g., user 'Jobinsam@674').
- Select 'Admin' from the 'User Type' dropdown.
- Verify that the existing required fields (User Role, Employee Name, Status, Username) remain valid or update them if necessary to avoid unintended side effects from other validations.
- Click the 'Save' button.
- Verify success message is displayed.
- Re-edit the same user record and verify that 'User Type' is set to 'Admin'.

---

## TC_KAN6_FEAT2_SUCCESS_011
**Description:** TC_KAN6_FEAT2_SUCCESS_010: Verify successful update of user details including setting a specific 'User Type'.

**Priority:** High

**Expected Result:** The user details (including the selected User Type) are saved correctly, and the user is returned to the System Users table with a success message.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button.
- Navigate to Admin -> User Management.
- Click the 'Edit' icon for an existing user (e.g., user 'Jobinsam@674').
- Select 'Admin' from the 'User Type' dropdown.
- Verify that the existing required fields (User Role, Employee Name, Status, Username) remain valid or update them if necessary to avoid unintended side effects from other validations.
- Click the 'Save' button.
- Verify success message is displayed.
- Re-edit the same user record and verify that 'User Type' is set to 'Admin'.

---
