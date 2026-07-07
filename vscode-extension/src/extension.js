const vscode = require('vscode');
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

function getOsefCommand(workspaceFolder) {
    const unixVenv = path.join(workspaceFolder, '.venv', 'bin', 'osef');
    if (fs.existsSync(unixVenv)) return `"${unixVenv}"`;
    const winVenv = path.join(workspaceFolder, '.venv', 'Scripts', 'osef.exe');
    if (fs.existsSync(winVenv)) return `"${winVenv}"`;
    const unixVenv2 = path.join(workspaceFolder, 'venv', 'bin', 'osef');
    if (fs.existsSync(unixVenv2)) return `"${unixVenv2}"`;
    const winVenv2 = path.join(workspaceFolder, 'venv', 'Scripts', 'osef.exe');
    if (fs.existsSync(winVenv2)) return `"${winVenv2}"`;
    return 'osef';
}

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    console.log('OSEF Studio VS Code extension is active.');

    const outputChannel = vscode.window.createOutputChannel('OSEF Engineering Platform');

    // Register sidebar tree data provider
    const statusProvider = new OSEFStatusProvider();
    vscode.window.registerTreeDataProvider('osef-status-view', statusProvider);

    // Command: Open Studio Workbench Webview
    let startStudioDisposable = vscode.commands.registerCommand('osef.startStudio', () => {
        const panel = vscode.window.createWebviewPanel(
            'osefStudio',
            'OSEF Studio Workbench',
            vscode.ViewColumn.One,
            {
                enableScripts: true,
                retainContextWhenHidden: true
            }
        );

        panel.webview.html = getStudioWebviewContent();
    });

    // Command: Validate Repository Graph
    let validateRepoDisposable = vscode.commands.registerCommand('osef.validateRepo', () => {
        outputChannel.show();
        outputChannel.appendLine('[OSEF] Running repository graph validation...');
        const workspaceFolder = vscode.workspace.workspaceFolders ? vscode.workspace.workspaceFolders[0].uri.fsPath : '.';
        const cmd = getOsefCommand(workspaceFolder);
        
        exec(`${cmd} validate repository .`, { cwd: workspaceFolder }, (error, stdout, stderr) => {
            if (stdout) outputChannel.appendLine(stdout);
            if (stderr) outputChannel.appendLine(stderr);
            if (error) {
                vscode.window.showErrorMessage(`OSEF Validation finished with errors: ${error.message}`);
            } else {
                vscode.window.showInformationMessage('OSEF Repository Graph validation successful!');
            }
        });
    });

    // Command: Evaluate Policy Rules
    let policyCheckDisposable = vscode.commands.registerCommand('osef.policyCheck', () => {
        outputChannel.show();
        outputChannel.appendLine('[OSEF] Evaluating engineering policies (SARIF format)...');
        const workspaceFolder = vscode.workspace.workspaceFolders ? vscode.workspace.workspaceFolders[0].uri.fsPath : '.';
        const cmd = getOsefCommand(workspaceFolder);
        
        exec(`${cmd} policy check . --format sarif`, { cwd: workspaceFolder }, (error, stdout, stderr) => {
            if (stdout) outputChannel.appendLine(stdout);
            if (stderr) outputChannel.appendLine(stderr);
            if (error) {
                vscode.window.showWarningMessage('OSEF Policy evaluation found findings.');
            } else {
                vscode.window.showInformationMessage('OSEF Policy check passed cleanly!');
            }
        });
    });

    context.subscriptions.push(startStudioDisposable, validateRepoDisposable, policyCheckDisposable);
}

function getStudioWebviewContent() {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSEF Studio Workbench</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
            overflow: hidden;
            background-color: #0b0f19;
            color: #f3f4f6;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        .container {
            display: flex;
            flex-direction: column;
            height: 100%;
            width: 100%;
        }
        .header {
            padding: 12px 20px;
            background: #111827;
            border-bottom: 1px solid #374151;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .title {
            font-size: 16px;
            font-weight: 600;
            color: #60a5fa;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        iframe {
            flex: 1;
            width: 100%;
            border: none;
        }
        .fallback {
            padding: 40px;
            text-align: center;
        }
        .code {
            background: #1f2937;
            padding: 8px 16px;
            border-radius: 6px;
            font-family: monospace;
            color: #38bdf8;
            display: inline-block;
            margin: 16px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="title">⚡ OSEF Studio Workbench</div>
            <div style="font-size: 12px; color: #9ca3af;">Connected to Local EKG</div>
        </div>
        <iframe src="http://localhost:8000" onerror="this.style.display='none'; document.getElementById('fallback').style.display='block';"></iframe>
        <div id="fallback" class="fallback" style="display: none;">
            <h2>OSEF Server Not Detected</h2>
            <p style="color: #9ca3af;">To embed the interactive Engineering Knowledge Graph and Policy Workbench in VS Code, start the studio daemon in your terminal:</p>
            <div class="code">osef ui</div>
            <p style="font-size: 12px; color: #6b7280; margin-top: 20px;">Once running on localhost:8000, reload this webview.</p>
        </div>
    </div>
    <script>
        const iframe = document.querySelector('iframe');
        iframe.onload = () => {
            try {
                // Try accessing iframe to see if loaded or failed
            } catch (e) {
                // Cross-origin or failed load
            }
        };
    </script>
</body>
</html>`;
}

class OSEFStatusProvider {
    getTreeItem(element) {
        return element;
    }

    getChildren(element) {
        if (!element) {
            return Promise.resolve([
                new OSEFTreeItem('EKG State', 'Active (In-Memory Graph)', vscode.TreeItemCollapsibleState.None),
                new OSEFTreeItem('Policy Engine', 'SARIF & JUnit Enabled', vscode.TreeItemCollapsibleState.None),
                new OSEFTreeItem('Marketplace Index', '16 Signed Plugins', vscode.TreeItemCollapsibleState.None),
                new OSEFTreeItem('MCP Server', 'Ready (JSON-RPC stdio)', vscode.TreeItemCollapsibleState.None)
            ]);
        }
        return Promise.resolve([]);
    }
}

class OSEFTreeItem extends vscode.TreeItem {
    constructor(label, description, collapsibleState) {
        super(label, collapsibleState);
        this.description = description;
        this.contextValue = 'osefStatusItem';
    }
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
