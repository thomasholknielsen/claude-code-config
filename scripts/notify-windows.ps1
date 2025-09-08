# Simple Windows notification script for Claude Code hooks
# Uses msg command which is always available on Windows

# Read hook input data from standard input
$InputData = [Console]::In.ReadToEnd()

# Get current session directory name
$SessionDir = Split-Path -Leaf (Get-Location)

# Default message
$DefaultMsg = "Task completed successfully"
$Message = $DefaultMsg

# Try to parse JSON input and extract transcript path
try {
    $JsonInput = $InputData | ConvertFrom-Json
    $TranscriptPath = $JsonInput.transcript_path
    
    # Try to get the latest assistant message if transcript exists
    if ($TranscriptPath -and (Test-Path $TranscriptPath)) {
        # Read last 10 lines of transcript
        $LastLines = Get-Content $TranscriptPath -Tail 10 -ErrorAction SilentlyContinue
        
        # Parse each line as JSON and find assistant messages
        $AssistantMessages = @()
        foreach ($Line in $LastLines) {
            try {
                $LineJson = $Line | ConvertFrom-Json
                if ($LineJson.message.role -eq "assistant" -and $LineJson.message.content[0].text) {
                    $AssistantMessages += $LineJson.message.content[0].text
                }
            } catch {
                # Skip lines that aren't valid JSON
            }
        }
        
        # Get the last assistant message
        if ($AssistantMessages.Count -gt 0) {
            $LastMessage = $AssistantMessages[-1]
            # Clean up message: remove newlines, trim to 60 chars
            $CleanMessage = ($LastMessage -replace '\n', ' ') -replace '\s+', ' '
            if ($CleanMessage.Length -gt 60) {
                $Message = $CleanMessage.Substring(0, 60) + "..."
            } else {
                $Message = $CleanMessage
            }
        }
    }
} catch {
    # If JSON parsing fails, use default message
    $Message = $DefaultMsg
}

# Show notification using msg command (always available on Windows)
$NotificationTitle = "Claude Code ($SessionDir)"
$FullMessage = "$NotificationTitle`: $Message"

# Use Windows notification
try {
    # Create a background job to show the message box so it doesn't block
    $Job = Start-Job -ScriptBlock {
        param($Message, $Title)
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.MessageBox]::Show($Message, $Title, [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
    } -ArgumentList $Message, $NotificationTitle
    
    # Don't wait for the job to complete - let it run in background
    Write-Host "Message box notification started in background"
} catch {
    # Fallback to console output if GUI fails
    Write-Host "NOTIFICATION: $FullMessage"
}

# Also write to console for debugging
Write-Host "✅ $NotificationTitle`: $Message"

# Try to focus VS Code if it's running
try {
    $VSCodeProcess = Get-Process "Code" -ErrorAction SilentlyContinue
    if ($VSCodeProcess) {
        # Simple window activation
        Add-Type @"
            using System;
            using System.Runtime.InteropServices;
            public class Win32 {
                [DllImport("user32.dll")]
                public static extern bool SetForegroundWindow(IntPtr hWnd);
            }
"@
        $VSCodeProcess | ForEach-Object {
            [Win32]::SetForegroundWindow($_.MainWindowHandle)
        }
    }
} catch {
    # Silently continue if window activation fails
}