# 🧹 Automated Disk Sanitiser Using Python
---
### Problem Statement

With the increasing reuse of storage devices, securely removing sensitive data has become critical. Manual deletion does not guarantee data removal, as files can often be recovered. There is a need for an automated solution that safely sanitises disks while ensuring accountability and preventing accidental data loss.

---
### Objectives

* To design an automated disk sanitisation tool
* To securely delete duplicate and unwanted files
* To ensure safety using validation and dry-run mechanisms
* To maintain logs for audit and verification

### Methodology

1. Accept directory or disk path as input
2. Validate path existence and type
3. Traverse directories using recursive traversal
4. Identify duplicate files using checksum comparison
5. Perform sanitisation using overwrite/delete logic
6. Log every critical operation

---
### ⚠️ Warning

This tool permanently deletes data. Use only on test systems or disks intended for sanitisation.

---
### 📌 Overview

* Developed a Python-based disk sanitisation tool to securely remove duplicate and unwanted files
* Implemented checksum-based duplicate detection to ensure accuracy
* Integrated structured logging for auditability and debugging
* Demonstrated strong understanding of file systems, automation, and defensive programming

### ✨ Features

* Duplicate detection using checksums
* Detailed logging
* Recursive directory traversal

---
### How to Run

1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

2. Run in dry-run mode (recommended)

```bash
python disk_sanitiser.py directoryname
```
---
### Logs

All operations are recorded in:

```
logs/sanitiser.log
```
---
### Safety Guidelines

* Always run dry-run first
* Never test on important data
* Review logs before enabling deletion
* Ensure correct path selection

---

## 👤 Author

**Omkar Mahadev Bhargude**

## 📅 Date

Monday, 09 February 2026

## ✅ Final Note

This project emphasizes safe automation, accountability, and professional coding practices when handling destructive operations.


