"""
Package made by psvks. Sudo for WINDOWS!
"""

def sudo(command):
    try:
        rawc = ' '.join(command)
        print(f'rawc: {rawc}')
        ps_command = f"""
            $psi = New-Object System.Diagnostics.ProcessStartInfo
            $psi.FileName = "cmd.exe"
            $psi.RedirectStandardError = $true
            $psi.RedirectStandardOutput = $true
            $psi.UseShellExecute = $false
            $psi.Verb = "runas"
            $psi.Arguments = "/c {rawc}"
            $p = New-Object System.Diagnostics.Process
            $p.StartInfo = $psi
            $p.Start() | Out-Null
            $p.WaitForExit()
            $stdout = $p.StandardOutput.ReadToEnd()
            $stderr = $p.StandardError.ReadToEnd()
            Write-Host "$stdout"
            Write-Host "$stderr"
        """
        result = subprocess.run(["powershell", "-Command", ps_command], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing command with sudo: {e}")
        print(e.output)
    except Exception as e:
        print(f"An error occurred: {e}")


registerCommand('sudo', sudo)
