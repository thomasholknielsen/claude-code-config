# Windows PowerShell helper script for cross-platform user prompt logging.
# Handles Windows-specific operations and calls the main Python logging script.

param()

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Path to the main Python logging script
$PythonScript = Join-Path $ScriptDir "log-prompt.py"

# Ensure the Python script exists
if (-not (Test-Path $PythonScript)) {
    Write-Error "[ERROR] Python logging script not found: $PythonScript"
    exit 1
}

# Create logs directory if it doesn't exist
$LogsDir = Join-Path $env:USERPROFILE ".claude\logs"
if (-not (Test-Path $LogsDir)) {
    try {
        New-Item -ItemType Directory -Path $LogsDir -Force | Out-Null
    }
    catch {
        Write-Warning "[WARNING] Could not create logs directory: $LogsDir"
        # Continue anyway - the Python script will handle fallback
    }
}

# Set proper permissions on logs directory (readable/writable by user only)
if (Test-Path $LogsDir) {
    try {
        # Remove inheritance and set owner permissions only
        $acl = Get-Acl $LogsDir
        $acl.SetAccessRuleProtection($true, $false)

        # Add full control for current user
        $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule(
            [System.Security.Principal.WindowsIdentity]::GetCurrent().Name,
            "FullControl",
            "ContainerInherit,ObjectInherit",
            "None",
            "Allow"
        )
        $acl.SetAccessRule($accessRule)
        Set-Acl -Path $LogsDir -AclObject $acl
    }
    catch {
        # Ignore permission errors - not critical
    }
}

# Read all input from stdin
$inputData = @()
while ($input = Read-Host) {
    $inputData += $input
}

# Convert input array to string
$inputString = $inputData -join "`n"

# Run the Python logging script with the input data
# Try different Python commands in order of preference
$pythonCommands = @("python3", "python", "py")
$exitCode = 1

foreach ($pythonCmd in $pythonCommands) {
    try {
        # Check if the Python command exists
        $null = Get-Command $pythonCmd -ErrorAction Stop

        # Run the Python script
        $process = Start-Process -FilePath $pythonCmd -ArgumentList $PythonScript -NoNewWindow -Wait -PassThru -RedirectStandardInput -

        # Send input to the process
        if ($inputString) {
            $process.StandardInput.WriteLine($inputString)
            $process.StandardInput.Close()
        }

        $exitCode = $process.ExitCode
        break
    }
    catch {
        # Try next Python command
        continue
    }
}

# If no Python command worked, show error
if ($exitCode -eq 1 -and $pythonCommands -notcontains $pythonCmd) {
    Write-Error "[ERROR] Python not found. Please install Python 3 and ensure it's in your PATH."
    exit 1
}

# Exit with the same code as the Python script
exit $exitCode
