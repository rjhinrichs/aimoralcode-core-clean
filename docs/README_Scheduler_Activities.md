# Scheduler Activities

This folder contains system-level automation tools that support the integrity, synchronization, and recovery of the AI Moral Code research repository.

## Included Script

### `enhanced_backup_with_rotation.bat`

This script performs a daily, automated mirror of the primary AI Moral Code GitHub repository located at:

```
C:\GitHub\aimoralcode-core
```

To a OneDrive-based backup directory:

```
C:\Users\Ran\OneDrive\Backup\aimoralcode-core
```

## Features

- **Automated folder creation**: Ensures all required paths exist before backup begins.
- **File mirroring**: Uses `robocopy` to synchronize all contents (excluding `.git` and lock files).
- **Daily log rotation**: Archives each run in `C:\Scheduler Activities\logs\` with a timestamped filename.
- **Real-time notification**: Displays a system pop-up after successful execution.
- **Safe from path errors**: Prevents silent failures due to missing directories.

## Logging

- Primary log file: `C:\Scheduler Activities\backup_log.txt`
- Archived logs: `C:\Scheduler Activities\logs\backup_log_YYYY-MM-DD.txt`

## Task Scheduler Configuration

- **Task Name**: `Backup GitHub Repo to OneDrive`
- **Schedule**: Daily (or as configured)
- **Script Path**: `C:\Scheduler Activities\enhanced_backup_with_rotation.bat`

## How to Modify

If you move the GitHub repository or backup destination:
- Open the `.bat` file in a text editor
- Update `SOURCE` and `DEST` paths accordingly

---

Maintained by **Randy Hinrichs**  
This scheduler supports the ethical stewardship of AI research by ensuring reproducibility, continuity, and disaster resilience.