# Testcases for aSzfdT4r

Total Testcases: **10**

## KAN6_F1_NAV_001
**Description:** Verify successful navigation to the newly added 'Job Section' under the Admin module.

**Priority:** High

**Expected Result:** The system successfully navigates to the 'Admin / Job' section, and the 'Job Titles' list view is displayed.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Click 'Admin' in the left navigation panel.
- Verify navigation to the new 'Job' subsection under Admin and check if the 'Job Titles' list is visible.

---

## KAN6_F1_CRUD_002
**Description:** Verify successful creation of a new Job Title using valid, complete data.

**Priority:** High

**Expected Result:** A new job title is successfully saved, and a success message confirming creation is displayed.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin -> Job.
- Click the 'Add New' button.
- Enter 'Software Architect' into the 'Job Title' field.
- Enter 'Designs and oversees software structure.' into the 'Job Description' field.
- Enter 'Expertise in cloud platforms and microservices.' into the 'Job Specification' field.
- Click the 'Save' button.

---

## KAN6_F1_VAL_003
**Description:** Verify validation for the mandatory 'Job Title' field during job creation (Negative Test).

**Priority:** High

**Expected Result:** An error message is displayed indicating that 'Job Title' is a required field, and the record is not saved.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin -> Job -> Click 'Add New Button'.
- Enter 'Detailed system design documents.' into the 'Job Description' field.
- Leave the 'Job Title' field empty.
- Enter 'Proficient in UML' into the 'Job Specification' field.
- Click the 'Save' button.

---

## KAN6_F1_CRUD_004
**Description:** Verify the 'Cancel' action discards changes on the Job Creation form.

**Priority:** Medium

**Expected Result:** The form is closed, and no changes are saved, returning to the Job Titles list view.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin -> Job -> Click 'Add New Button'.
- Enter 'Temporary Role' into the 'Job Title' field.
- Click the 'Cancel' button.
- Verify the system returns to the Job Titles list without adding 'Temporary Role'.

---

## KAN6_F1_CRUD_005
**Description:** Verify editing an existing Job Title record successfully.

**Priority:** High

**Expected Result:** The selected Job Title's details are updated with the new description and specification, and a success message is displayed.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin -> Job.
- Locate an existing Job Title (e.g., 'System Analyst') and click the 'Edit Icon'.
- Modify the 'Job Description' field to 'Analyzes complex business problems new update'.
- Click the 'Save' button.

---

## KAN6_F1_CRUD_006
**Description:** Verify deletion of an existing Job Title record.

**Priority:** High

**Expected Result:** The system prompts for confirmation, and upon confirmation, the Job Title is permanently removed from the list, and a success message is displayed.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin -> Job.
- Locate a pre-created test Job Title (e.g., 'Test Job Deletable') and click the 'Delete Icon'.
- Confirm the deletion prompt.

---

## KAN6_F2_UI_007
**Description:** Verify the successful display and functionality of the mandatory 'User Type' field in the Edit User section.

**Priority:** Critical

**Expected Result:** The Edit User page loads, and the new 'User Type' field is visible and editable/selectable, allowing for selection of a specific type.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin / User Management (As per Documentation Section 3.1).
- Locate any user record and click the 'Edit Icon' (pencil icon).
- Verify that a field labeled 'User Type*' (mandatory) is present among the form fields.
- Open the dropdown for 'User Type' and verify at least one option is available.

---

## KAN6_F2_VAL_008
**Description:** Verify the mandatory validation rule for the 'User Type' field when attempting to save changes without selecting a type (Negative Test).

**Priority:** Critical

**Expected Result:** An error message is displayed indicating that 'User Type' is mandatory, and the Save action is blocked.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin / User Management.
- Locate user 'Jobinsam@674' and click the 'Edit Icon'.
- Ensure the 'User Type' field selection is cleared/defaulted to an empty selection (if possible).
- Change the 'Status' dropdown from 'Enabled' to 'Disabled' (to trigger a save attempt without User Type change).
- Click the 'Save Button' (as documented in Sec 4.3 of page 9).

---

## KAN6_F2_WORKFLOW_009
**Description:** Verify successful update of an existing user, specifically setting the 'User Type' field to a specific value.

**Priority:** High

**Expected Result:** The user details, including the new 'User Type', are successfully updated, and the user is returned to the User Management page with a success confirmation.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin / User Management.
- Locate user 'Jobinsam@674' and click the 'Edit Icon'.
- Select a specific User Type (e.g., 'Admin Type' - assuming this exists) from the 'User Type' dropdown.
- Click the 'Save Button'.
- Verify returning to Admin/User Management and confirming the saved 'User Type' upon re-editing the user.

---

## KAN6_F1_VAL_010
**Description:** Boundary Test: Verify saving a new Job Title when ALL fields (Title, Description, Specification) are empty.

**Priority:** Medium

**Expected Result:** The job creation process is correctly aborted upon attempting to save with all required fields blank.

### Steps:
- Navigate to URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- Enter username as 'Admin'
- Enter password as 'admin123'
- Click on the login button.
- Navigate to Admin -> Job -> Click 'Add New Button'.
- Ensure 'Job Title', 'Job Description', and 'Job Specification' fields are all empty.
- Click the 'Save' button.
- Verify that the system enforces validation (expectedly on 'Job Title' first, or aggregated error) and prevents saving.

---

