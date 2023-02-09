
$file = Get-Content file.txt

while ($true) {
    [System.Windows.Clipboard]::SetText('')
    $prompt = Read-Host -Prompt 'Enter Prompt And/OR copy content:'
    $paste_clipboard = [System.Windows.Clipboard]::GetText()
    $prompt += "`n$paste_clipboard"
    $url = 'https://api.openai.com/v1/completions'
    $headers = @{
        'Content-Type' = 'application/json'
        'Authorization' = "Bearer $file"
    }
    $data = @{
        'model' = 'text-davinci-003'
        'prompt' = $prompt
        'temperature' = 0.3
        'max_tokens' = 521
        'top_p' = 1
        'frequency_penalty' = 0
        'presence_penalty' = 0
    }
    $data = $data | Convertto-json
    $response = Invoke-WebRequest -Uri $url -Headers $headers -Body $data -Method Post -WarningAction SilentlyContinue

    $data = ConvertFrom-Json -InputObject $response.Content

    try {
        Write-Host $data.choices[0].text
    }
    catch {
        Write-Host $response.Content
    }
}
