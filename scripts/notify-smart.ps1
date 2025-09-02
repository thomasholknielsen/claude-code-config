# ~/.claude/scripts/notify-smart.ps1
# Windows PowerShell notification script for Claude Code hooks

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

# Function to show Windows 10/11 Toast Notification
function Show-ToastNotification {
    param(
        [string]$Title,
        [string]$Message
    )
    
    # Create notification using Windows Runtime
    Add-Type -AssemblyName Windows.Data
    Add-Type -AssemblyName Windows.UI
    
    # XML template for the toast notification with activation
    $XmlTemplate = @"
<toast activationType="protocol" launch="vscode:">
    <visual>
        <binding template="ToastGeneric">
            <text>$Title</text>
            <text>$Message</text>
        </binding>
    </visual>
    <audio src="ms-winsoundevent:Notification.Default"/>
</toast>
"@
    
    try {
        # Use Windows.UI.Notifications for Windows 10/11
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
        [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom, ContentType = WindowsRuntime] | Out-Null
        
        $XmlDoc = New-Object Windows.Data.Xml.Dom.XmlDocument
        $XmlDoc.LoadXml($XmlTemplate)
        
        $Toast = [Windows.UI.Notifications.ToastNotification]::new($XmlDoc)
        
        # Create notifier for PowerShell
        $AppId = "Microsoft.PowerShell"
        $Notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($AppId)
        $Notifier.Show($Toast)
    } catch {
        # Fallback to BurntToast module if available
        if (Get-Module -ListAvailable -Name BurntToast) {
            Import-Module BurntToast
            New-BurntToastNotification -Text $Title, $Message -Sound Default
        } else {
            # Final fallback: Use msg command (basic, no click action)
            msg * "/TIME:5 Claude Code ($SessionDir): $Message"
        }
    }
}

# Try to activate VS Code if it's running
function Activate-VSCode {
    try {
        # Get VS Code process
        $VSCodeProcess = Get-Process "Code" -ErrorAction SilentlyContinue
        if ($VSCodeProcess) {
            # Bring VS Code window to foreground
            Add-Type @"
                using System;
                using System.Runtime.InteropServices;
                public class Win32 {
                    [DllImport("user32.dll")]
                    public static extern bool SetForegroundWindow(IntPtr hWnd);
                    [DllImport("user32.dll")]
                    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
                }
"@
            $VSCodeProcess | ForEach-Object {
                [Win32]::ShowWindow($_.MainWindowHandle, 9) # SW_RESTORE
                [Win32]::SetForegroundWindow($_.MainWindowHandle)
            }
        }
    } catch {
        # Silently fail if we can't activate VS Code
    }
}

# Show the notification
$NotificationTitle = "✅ Claude Code ($SessionDir)"
Show-ToastNotification -Title $NotificationTitle -Message $Message

# Note: The toast notification XML includes activationType="protocol" and launch="vscode:"
# This should open VS Code when clicked, but depends on VS Code protocol handler being registered