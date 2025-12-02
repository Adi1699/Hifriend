# Testcases for aSzfdT4r

Total Testcases: **10**

## TC_KAN6_LOGIN_001
**Description:** TC_KAN6_LOGIN_001: Verify successful login using provided credentials.

**Priority:** Critical

**Expected Result:** User is successfully logged in, and the Dashboard is displayed as the default landing page.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter 'Admin' into the username input field.
- Enter 'admin123' into the password input field.
- Click the Login button.

---

## TC_KAN6_NAV_002
**Description:** TC_KAN6_NAV_002: Verify navigation to the new 'Job Section' under the Admin module.

**Priority:** High

**Expected Result:** The user is navigated to the 'Admin / User Management' page, and the new 'Job' sub-section is accessible.

### Steps:
- Perform Login (as per TC_KAN6_LOGIN_001).
- Click 'Admin' in the left navigation panel.
- Verify the page title changes to 'Admin / User Management'.
- Locate and click the newly added 'Job' item/link within the Admin section.

---

## TC_KAN6_JOB_003
**Description:** TC_KAN6_JOB_003: Positive scenario: Create a new job title with valid data in all required fields.

**Priority:** High

**Expected Result:** A new Job Title record is successfully created, a success message is displayed, and the new title appears in the Job Titles list.

### Steps:
- Navigate to Admin -> Job (as per TC_KAN6_NAV_002).
- Click the 'Add New Button'.
- Enter 'Senior QA Engineer' into the 'Job Title' input field.
- Enter 'Responsible for automated testing and quality assurance across major releases.' into the 'Job Description' textarea.
- Enter 'Skills: Selenium, Python, Automation Framework development.' into the 'Job Specification' textarea.
- Click the 'Save' button.

---

## TC_KAN6_JOB_004
**Description:** TC_KAN6_JOB_004: Negative scenario: Attempt to save a new job title leaving the mandatory 'Job Title' field empty.

**Priority:** High

**Expected Result:** The system displays a validation error for the 'Job Title' field, and the record is NOT saved. The user remains on the 'Add Job Title' form.

### Steps:
- Navigate to Admin -> Job -> Click 'Add New Button'.
- Enter 'Detailed job requirements for recruitment' into the 'Job Description' textarea.
- Enter 'Must meet all essential specifications' into the 'Job Specification' textarea.
- Ensure the 'Job Title' field is empty.
- Click the 'Save' button.

---

## TC_KAN6_JOB_005
**Description:** TC_KAN6_JOB_005: Positive scenario: Discarding job creation using the 'Cancel' action.

**Priority:** Medium

**Expected Result:** The Job Title creation form is discarded, no changes are saved, and the user returns to the Job Titles list view.

### Steps:
- Navigate to Admin -> Job -> Click 'Add New Button'.
- Enter 'Temporary Test Job' into the 'Job Title' input field.
- Click the 'Cancel' button.
- Verify that the 'Temporary Test Job' does not appear in the list of Job Titles.

---

## TC_KAN6_JOB_006
**Description:** TC_KAN6_JOB_006: Positive scenario: Deleting an existing Job Title record.

**Priority:** High

**Expected Result:** The specific job title record is successfully deleted after confirmation, and a success message is displayed.

### Steps:
- Perform Login (as per TC_KAN6_LOGIN_001).
- Navigate to Admin -> Job.
- Locate a pre-existing Job Title record (e.g., one created in a preceding test if possible, or a known existing entry).
- Click the 'Delete Icon' next to the selected Job Title.
- Confirm the deletion prompt.
- Verify the record is removed from the 'Job Titles' table.

---

## TC_KAN6_JOB_007
**Description:** TC_KAN6_JOB_007: Positive scenario: Editing an existing Job Title successfully.

**Priority:** High

**Expected Result:** The existing Job Title details are updated with the new values, and a success message is displayed on the Job Titles list view.

### Steps:
- Perform Login (as per TC_KAN6_LOGIN_001).
- Navigate to Admin -> Job.
- Click the 'Edit Icon' next to an existing Job Title (e.g., 'Senior QA Engineer').
- Modify the 'Job Description' field to 'Updated description reflecting senior scope changes...'
- Click the 'Save' button.
- Navigate back to the Job Titles list and verify the 'Job Description' is updated.

---

## TC_KAN6_EDIT_008
**Description:** TC_KAN6_EDIT_008: Verify the mandatory 'User Type' field appears correctly when navigating to Edit User.

**Priority:** Critical

**Expected Result:** The user is navigated to the 'Edit User' page (Page title changes to 'Admin'), and the mandatory 'User Type' field is present and selectable.

### Steps:
- Perform Login (as per TC_KAN6_LOGIN_001).
- Navigate to Admin / User Management (via 'Admin' left navigation).
- Click the 'Edit Icon' (pencil) next to an existing user record.
- Verify the page title changes to 'Admin'.
- Verify the presence of the field labeled 'User Type*' indicating it is required.

---

## TC_KAN6_EDIT_009
**Description:** TC_KAN6_EDIT_009: Negative scenario: Attempt to save user modifications while leaving the mandatory 'User Type' field empty.

**Priority:** Critical

**Expected Result:** The system displays a validation error, preventing the save operation, as the mandatory 'User Type' field is left unselected.

### Steps:
- Perform Login (as per TC_KAN6_LOGIN_001).
- Navigate to the 'Edit User' form for any user.
- Keep the 'User Type' dropdown in its default/unselected state (assuming it's not pre-selected if user has no permissions to change).
- Optionally modify a non-conflicting field, e.g., Status dropdown to 'Disabled'.
- Click the 'Save Button'.
- Verify a validation message referencing 'User Type' is displayed and the user details are NOT updated.

---

## TC_KAN6_EDIT_010
**Description:** TC_KAN6_EDIT_010: Positive scenario: Successfully updating user details, ensuring 'User Type' is selected correctly before saving.

**Priority:** High

**Expected Result:** The user modifications are saved successfully, including the selection made in the 'User Type' field, and the user returns to the User Management page.

### Steps:
- Perform Login (as per TC_KAN6_LOGIN_001).
- Navigate to the 'Edit User' form for an existing user.
- Change the 'User Role*' value from the current 'ESS' to 'Admin' (assuming 'Admin' is a selectable role type).
- Select a valid option from the new mandatory 'User Type' dropdown (e.g., 'Standard' or 'Super Admin').
- Ensure 'Change Password?' checkbox is unchecked.
- Click the 'Save Button'.
- Verify navigation back to 'Admin / User Management' page and confirm the updated role and User Type persistence upon reloading the user's edit screen.

---

dsfsdfsdfsdfsdfsdfsdfds