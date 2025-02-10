## Lab: Conduct a compliance review for a mock project and document findings

## Lab Overview
In this lab, you’ll practice **conducting a compliance review** for a **fictional or mock project**. You’ll be guided through:

1. **Defining a Mock Scenario** (e.g., a healthcare web application).
2. **Identifying Relevant Regulations** (e.g., GDPR, HIPAA).
3. **Completing a Compliance Checklist** to see where gaps might be.
4. **Creating a Risk Register** to prioritize issues.
5. **Summarizing Your Findings** in a short Compliance Review Report.

All steps include **examples** so that everyone can easily follow along.

---

## Lab Steps

### Step 1: Define Your Mock Project Scenario

1. **Create a simple description** of a project that might handle sensitive or personal data.  
   - **Example**:  
     - **Project Name**: HealthStats Tracker  
     - **Purpose**: A web portal that collects basic patient information (name, age, medical ID, symptoms) and stores it for future analytics.  
     - **Technologies Used**: Web front-end (HTML/JS), a back-end (Python or Node.js), and a database (MySQL or in-memory storage).  
     - **Data Type**: Personal data (name, ID, contact info) and health data (symptoms, diagnoses).

2. **List the stakeholders**:  
   - **Example**:  
     - Product Owner: Dr. Smith (oversees requirements)  
     - Development Team: In-house software engineers  
     - Compliance Officer: Jane Doe (ensures HIPAA/GDPR compliance)

**Your Task**: Write 1–2 paragraphs describing your **mock project**. Make sure to specify which types of sensitive data might be collected or processed.

---

### Step 2: Identify Relevant Regulations & Standards

1. **Decide which regulations apply** to your mock project. Examples:
   - **GDPR**: If you have data from EU residents or handle personal data that falls under EU jurisdiction.
   - **HIPAA**: If your project deals with protected health information (PHI) in a US healthcare context.
   - **PCI-DSS**: If your project processes payments (credit card data).
   - **Industry Best Practices**: ISO 27001 or SOC 2, if relevant.

2. **Write them down** in a bullet list or small table.

**Example**:

| Regulation/Standard | Reason It Applies             |
|---------------------|--------------------------------|
| GDPR               | Potentially collecting EU data |
| HIPAA              | Handling patient health info    |
| OWASP Top 10       | Secure coding best practices   |

**Your Task**: Create a short bullet list (or small table) with the regulations/standards that apply to your scenario, and note **why** they apply.

---

### Step 3: Complete a Compliance Checklist

To avoid confusion, we’ll **simulate** a short portion of the checklist for both **GDPR** and **HIPAA**. You will fill out “Yes,” “No,” “Partial,” or other relevant statuses.

#### 3.1. GDPR Checklist (Example)

Create a simple table (in a Word doc, Google Doc, or Excel/Google Sheet) with the following columns:

| **Requirement**             | **Description**                                         | **Status**  | **Notes**                                    |
|-----------------------------|---------------------------------------------------------|------------|----------------------------------------------|
| Data Minimization           | Collect only data necessary for the purpose            | Partial    | Currently collecting more fields than needed |
| Consent                     | Obtain clear, informed consent for data processing     | No         | No explicit consent checkbox on the form     |
| Right to Erasure (Deletion) | Provide a way for users to request their data be deleted | No         | No mechanism in place to delete records      |
| Data Breach Notification    | Notify authorities and individuals if a breach occurs  | Partial    | Policy is drafted but not fully implemented  |

1. **Pick a few main GDPR items** (data minimization, consent, right to erasure, breach notification) and fill in a column for your scenario’s status.  
2. **Add notes** on why you chose that status.

> **Example** for “Consent” row:  
> - **Status**: No  
> - **Notes**: We have a form that collects patient info, but we haven’t added a checkbox for consent or a privacy notice.

#### 3.2. HIPAA Checklist (Example)

Similarly, create (or extend) your table for **HIPAA**:

| **HIPAA Standard**                | **Description**                                             | **Status** | **Notes**                                           |
|-----------------------------------|-------------------------------------------------------------|-----------|-----------------------------------------------------|
| Privacy Rule                       | Policies to protect PHI & patient rights                   | Partial   | Privacy policy exists, but not easily accessible    |
| Security Rule - Administrative    | E.g., assigned security responsibilities, training         | No        | No designated security official or training         |
| Security Rule - Technical         | Access controls, encryption, unique user IDs               | Partial   | Some encryption in transit, but no unique logins    |
| Breach Notification Rule          | Procedures for notifying patients of a breach              | No        | No documented breach notification plan              |

**Your Task**: Choose at least **4–5 items** from GDPR and/or HIPAA relevant to your mock project. Fill out your **compliance checklist** with a “Yes/No/Partial” status and a short explanatory note.

---

### Step 4: Create a Risk Register

In this step, you’ll **prioritize** each compliance gap or issue. You can do this in a spreadsheet (Excel, Google Sheets) or a table in Word/Docs.

1. **Open a new spreadsheet** or table with the following columns:

| **Risk/Issue**              | **Regulation Affected** | **Likelihood (L/M/H)** | **Impact (L/M/H)** | **Risk Level (L/M/H)** | **Mitigation**                                   | **Owner**    | **Timeline** |
|-----------------------------|-------------------------|------------------------|--------------------|------------------------|---------------------------------------------------|-------------|-------------|
| Example: No Consent Checkbox | GDPR                    | M                      | M                  | M                      | Implement a consent banner + checkbox            | Dev Team     | 2 Weeks      |

2. **Fill it out** for each gap you found in your checklist. For instance:
   - **Issue**: Missing consent mechanism → Affects GDPR.
   - **Likelihood**: Medium → Because if you’re collecting data from EU residents, it’s quite possible you’ll face a compliance check.
   - **Impact**: Medium → Potential fines or user complaints.
   - **Risk Level**: Medium → Because both likelihood and impact are medium.
   - **Mitigation**: “Implement a consent checkbox plus a privacy notice before submission.”
   - **Owner**: “Dev Team” or “Compliance Officer.”
   - **Timeline**: “2 Weeks” or “By next release.”

3. **Add at least 3–5 other items** from your compliance checklist to ensure you have a robust risk register.

> **Example**:  
> - **Risk/Issue**: No mechanism for data deletion → **Regulation**: GDPR Right to Erasure → **Likelihood**: High → **Impact**: High → **Risk Level**: High → **Mitigation**: “Build a ‘Delete My Data’ feature or admin console.” → **Owner**: Dev Team → **Timeline**: 1 Month.

---

### Step 5: Summarize in a Short Compliance Review Report

Now that you have **checklists** and a **risk register**, you’ll create a brief report. This could be a **1–3 page document** or a structured outline in Google Docs/Word.

1. **Introduction**  
   - State the mock project’s name, purpose, and brief overview (1 paragraph).

2. **Regulations in Scope**  
   - List GDPR, HIPAA, etc., and why they apply to your scenario (from Step 2).

3. **Key Findings from the Checklist**  
   - Summarize the biggest gaps. For example:
     - “We lack a consent mechanism (GDPR).”
     - “We have no formal breach notification process (HIPAA).”

4. **Risk Register Highlights**  
   - Insert a quick table with the top 3–5 high-risk items or reference the separate spreadsheet.

5. **Recommendations**  
   - Provide 2–3 immediate action items for the team.
   - Example: “Implement a privacy notice and consent checkbox,” “Establish a formal breach notification policy.”

6. **Conclusion**  
   - 1–2 sentences emphasizing the importance of closing these gaps.

**Your Task**:  
Create this short document (or structured outline). **Include** a small table or mention of the top risks and recommended fixes.

---

## Example Deliverables

Below are simplified **example deliverables** you might produce.

### 1. GDPR/HIPAA Checklist Excerpt

| Requirement               | Description                                              | Status  | Notes                                        |
|---------------------------|----------------------------------------------------------|--------|----------------------------------------------|
| GDPR - Consent            | Clear, informed consent for data processing             | No      | No consent checkbox on the web form          |
| GDPR - Data Minimization  | Only collecting necessary data fields                   | Partial | Collecting “Postal Address” though not needed |
| HIPAA - Security Rule     | Technical safeguards, unique user IDs, encryption       | Partial | Some encryption (HTTPS), but no user IDs      |
| HIPAA - Breach Notification | Official plan for notifying patients of data breaches | No      | No documented process yet                     |

### 2. Risk Register Excerpt

| Risk/Issue                  | Regulation Affected | Likelihood | Impact | Risk Level | Mitigation                                                      | Owner          | Timeline  |
|-----------------------------|---------------------|-----------|--------|-----------|-----------------------------------------------------------------|---------------|-----------|
| No consent mechanism        | GDPR                | M         | M      | M         | Add a checkbox for consent + link to a privacy policy           | Dev Team       | 2 Weeks   |
| No user deletion feature    | GDPR                | H         | H      | H         | Implement data deletion flow in admin console                   | Dev Team       | 1 Month   |
| Lack of breach notification | HIPAA               | L         | H      | M         | Create a documented process + train staff on breach procedures  | Compliance Off | 3 Weeks   |

### 3. Short Report (Outline)

**1. Introduction**  
“HealthStats Tracker is a web-based platform collecting patient data for analytics...We handle sensitive health data, which puts us under GDPR and HIPAA due to potential EU usage and US healthcare context.”

**2. Regulations in Scope**  
“GDPR for EU personal data, HIPAA for US patient health information.”

**3. Key Findings**  
“We found missing consent mechanisms for GDPR and no formal breach notification procedure for HIPAA.”

**4. Risk Register Highlights**  
Refer to or paste the top 3–5 risk items from your table.

**5. Recommendations**  
“Implement a privacy notice and consent form (2 weeks), add user account system with unique IDs and role-based access (1 month).”

**6. Conclusion**  
“Addressing these gaps will reduce legal risk and ensure patient trust. Further training and audits are recommended every quarter.”

---

## Final Submission / Lab Completion

- **Checklist Documents**: Show your filled-in tables (GDPR/HIPAA or other relevant frameworks).
- **Risk Register**: Completed spreadsheet with at least 3–5 risks, plus mitigating actions.
- **Short Compliance Review Report**: 1–3 pages summarizing findings and recommendations.

**Instructor Tip**:  
Encourage students to **screenshot** or **attach** any tables/spreadsheets. Provide **feedback** on whether their risk prioritization and recommended actions are practical and aligned with the regulations.

---

## Summary

By following these steps and referencing the **examples**, you’ll conduct a **full compliance review** of a mock project. You’ve:

- Created a **project scenario** with potentially sensitive data.
- Checked **GDPR/HIPAA** compliance against **real or simulated** checklists.
- Documented **risks** in a structured **risk register**.
- Summarized everything in a **short compliance review report** that highlights necessary fixes.

This process mirrors **real-world** compliance practices, ensuring you understand how to systematically identify, document, and prioritize compliance gaps in a project.
