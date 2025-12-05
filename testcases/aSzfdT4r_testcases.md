# Testcases for aSzfdT4r

Total Testcases: **10**
This is testcases for sample testing

## TC_JIRA_KAN6_001
**Description:** Verify successful navigation to the new Job Section under the Admin module.

**Priority:** High

**Expected Result:** The system navigates to the Admin -> Job Titles page, and the page title reflects 'Admin / Job Titles'.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Click on 'Admin' in the left navigation panel.
- Click on the new 'Job' section link, which is expected to be present under Admin.

---

## TC_JIRA_KAN6_002
**Description:** Verify successful creation of a new Job Title using valid data.

**Priority:** Critical

**Expected Result:** A new job title is created, saved successfully, and a success message is displayed. The new job title appears in the Job Titles list.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin -> Job
- Click the 'Add New' button.
- Enter 'Senior QA Engineer' into the 'Job Title' input field.
- Enter 'Responsible for creating and maintaining test automation suites for key features.' into the 'Job Description' textarea.
- Enter 'Must possess expertise in Selenium and CI/CD integration.' into the 'Job Specification' textarea.
- Click the 'Save' button.

---

## TC_JIRA_KAN6_003
**Description:** Verify required field validation for 'Job Title' when attempting to save a new job record.

**Priority:** Critical

**Expected Result:** The system prevents saving and displays a validation error message indicating that 'Job Title' is required.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin -> Job
- Click the 'Add New' button.
- Leave the 'Job Title' input field empty.
- Enter dummy text into 'Job Description' field (e.g., 'Test Description').
- Enter dummy text into 'Job Specification' field (e.g., 'Test Spec').
- Click the 'Save' button.

---

## TC_JIRA_KAN6_004
**Description:** Verify required field validation for 'Job Description' when attempting to save a new job record.

**Priority:** High

**Expected Result:** The system prevents saving and displays a validation error message indicating that 'Job Description' is required.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin -> Job
- Click the 'Add New' button.
- Enter 'Test Job' into the 'Job Title' input field.
- Leave the 'Job Description' textarea empty.
- Enter dummy text into 'Job Specification' field (e.g., 'Test Spec').
- Click the 'Save' button.

---

## TC_JIRA_KAN6_005
**Description:** Verify the 'Cancel' action discards new job creation and returns to the previous screen.

**Priority:** High

**Expected Result:** The changes are discarded, and the user is returned to the Job Titles list view. No new job title is created.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin -> Job
- Click the 'Add New' button.
- Enter 'Temporary Role' into the 'Job Title' input field.
- Click the 'Cancel' button.

---

## TC_JIRA_KAN6_006
**Description:** Verify successful editing and saving of an existing Job Title.

**Priority:** High

**Expected Result:** The existing job title's details (Title, Description, Specification) are updated, and a success message confirms the save. The list view reflects the changes.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin -> Job
- Locate an existing job title (e.g., use search if necessary) and click the 'Edit Icon' (pencil icon) next to it.
- Modify the 'Job Title' field to 'Modified Test Title 123'.
- Append text to the 'Job Description' textarea (e.g., ' Updated description.').
- Click the 'Save' button.

---

## TC_JIRA_KAN6_007
**Description:** Verify deletion of an existing Job Title record.

**Priority:** Critical

**Expected Result:** The system deletes the selected job title after presenting a confirmation prompt and receiving affirmative action. The 'Records Found Count' decreases.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin -> Job
- Ensure at least one job title exists for deletion test.
- Locate a non-essential job title and click the 'Delete Icon' (trash can icon).
- Confirm the deletion action when the confirmation prompt appears.

---

## TC_JIRA_KAN6_008
**Description:** Verify the presence and visibility of the mandatory 'User Type' field in the Edit User section.

**Priority:** Critical

**Expected Result:** The User Profile page opens, displaying the new 'User Type' field alongside existing fields.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin / User Management (by clicking 'Admin' in the left navigation panel).
- Click the 'Edit Icon' (pencil icon) next to an existing user record.
- Verify that the 'User Type' field is visible on the 'Admin / Edit User' form.

---

## TC_JIRA_KAN6_009
**Description:** Verify mandatory validation for the new 'User Type' field when attempting to save user modifications.

**Priority:** Critical

**Expected Result:** The system prevents saving the user modification and displays a mandatory field error message specifically for the 'User Type' field.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin / User Management.
- Click the 'Edit Icon' (pencil icon) next to the user 'Jobinsam@674'.
- Change the 'Status Dropdown' value to 'Disabled'.
- Ensure the 'User Type' dropdown is left unselected (or in its default state indicating no selection).
- Click the 'Save Button'.

---

## TC_JIRA_KAN6_010
**Description:** Verify successful modification of user details including selecting a valid value for the mandatory 'User Type' field.

**Priority:** High

**Expected Result:** The user details, including the newly selected 'User Type', are successfully saved, and the user returns to the System Users table view with a success notification.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click the Login button
- Navigate to Admin / User Management.
- Click the 'Edit Icon' (pencil icon) next to the user 'Jobinsam@674'.
- Change the 'Status Dropdown' value to 'Disabled'.
- Select 'ESS' from the newly added 'User Type' dropdown menu.
- Click the 'Save Button'.
- Verify navigation back to the 'Admin / User Management' page and check for a success message.

---

