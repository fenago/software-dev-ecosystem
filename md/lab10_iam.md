## Lab : Configure IAM policies for secure cloud access

## **Objective**

By the end of this lab, students will:

- Assign IAM Roles to users on their respective VMs.
- Verify IAM permissions using role-based access control (RBAC).
- Enable Just-in-Time (JIT) Access for their VMs.
- Enable Auto-Shutdown for cost and security optimization.
- Understand shared resource visibility in a common resource group.

---

## **Prerequisites**

- All students are using the **same Azure account**.
- Each student has created an **Ubuntu Server VM** prefixed with their name (e.g., `John-VM`).
- Students have an **additional user account** that they will assign IAM permissions to.
- All VMs are in a **shared resource group**, meaning students can see others' VMs but should only modify their own.

---

## **Step 1: Assign "Reader" Role to a User**

1. **Log in** to the [Azure portal](https://portal.azure.com).
2. Go to **Virtual Machines** and locate your VM (e.g., `John-VM`).
3. Click on your VM and go to **Access Control (IAM)**.
4. Click **Add > Add role assignment**.
5. Select **Reader** role.
6. Under **Assign access to**, select **User, group, or service principal**.
7. In **Select Members**, enter the additional user’s email or username.
8. Click **Review + Assign**.

 **Verification:**

- Log in as the assigned user.
- Navigate to the VM and try to **start or stop it**.
- The operation should **fail** since the Reader role only allows viewing the VM.

---

## **Step 2: Upgrade User Role to "Virtual Machine Contributor"**

1. Log back in as the original user (owner of the VM).
2. Navigate to **Virtual Machines** > **Access Control (IAM)**.
3. Remove the **Reader** role for the assigned user.
4. Click **Add > Add role assignment**.
5. Select **Virtual Machine Contributor**.
6. Assign it to the same user.
7. Click **Review + Assign**.

 **Verification:**

- Log back in as the assigned user.
- Try to **start/stop the VM**.
- The operation should now **succeed**, confirming the role allows VM management.

---

## **Step 3: Enable Just-in-Time (JIT) VM Access**

1. Navigate to **Microsoft Defender for Cloud** in the Azure portal.
2. Select **Just-in-time VM access**.
3. Click on your VM and select **Enable JIT on your VMs**.
4. Configure:
   - Select **ports** (22 for SSH access).
   - Allowed IPs: **Only my IP**.
   - **Maximum access time**: 1 hour.
5. Click **Save**.

**Verification:**

- Try SSH access to the VM **without requesting JIT** (it should fail).
- Request JIT access and try again (it should succeed).

---

## **Step 4: Configure Auto-Shutdown for Cost Optimization**

1. Navigate to **Virtual Machines** in the Azure portal.
2. Select your VM.
3. Go to **Auto-shutdown**.
4. Enable auto-shutdown and set a **shutdown time** (e.g., 7:00 PM UTC).
5. Optionally, enter an **email** for shutdown notifications.
6. Click **Save**.

 **Verification:**

- The VM will shut down at the scheduled time automatically.

---

## **Step 5: Review Audit Logs**

1. Navigate to **Monitor > Activity Log**.
2. Apply filters:
   - **Category**: Administrative
   - **Resource Type**: Virtual Machine
   - **Time Range**: Last 24 hours
3. Look for logs related to:
   - **Role Assignments**
   - **JIT Requests**
   - **VM Shutdown events**

 **Verification:**

- Logs should show the actions taken, including IAM role changes and JIT access requests.

---

## **Step 6: Observing Other Students' VMs in the Shared Resource Group**

- Since all students are using the **same Azure account and resource group**, they can see each other's VMs in **Virtual Machines**.
- However, **they can only manage their own VMs** if IAM roles are correctly assigned.

 **Security Best Practices:**

- Ensure IAM roles are assigned only to **authorized users**.
- Use **JIT access** to limit unnecessary SSH/RDP exposure.
- **Review activity logs** to track unauthorized actions.

---

## **Conclusion**

- Assigned IAM roles using RBAC.
- Verified role-based access.
- Enabled Just-in-Time access for secure VM management.
- Configured auto-shutdown for cost efficiency.
- Reviewed logs for security auditing.

